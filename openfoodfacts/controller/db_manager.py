import mysql.connector as db_connector
from openfoodfacts.controller.data_scraper import DataScraper
from openfoodfacts.settings import *
from os import path


class DbManager:
    """This class is responsible of the database management"""

    def __init__(self):
        self._db_instance = None

    @property
    def db_instance(self):
        """Get an instance of a connection to the DB """

        if not self._db_instance:
            try:
                self._db_instance = db_connector.connect(**MYSQL_CONFIG)
            except db_connector.errors.InterfaceError:
                print(
                    "Impossible de se connecter à la base de données\n"
                    "Vérifiez qu'une instance de mysql est bien lancée et "
                    "est correctement configurée"
                )
                exit(0)
            try:
                self._db_instance.database = DB_NAME
            except:
                print(
                    "Base de données introuvable !\n"
                    "Veuillez patienter pendant sa création..."
                )
                self.create_db(populate=True)
        return self._db_instance

    def create_db(self, drop=False, populate=False):
        """Creates the database and tables """

        cursor = self.db_instance.cursor()
        sql_statement = ""

        if drop:
            cursor.execute(f"DROP DATABASE `{DB_NAME}`")

        sql_file_path = path.dirname(path.dirname(path.abspath(__file__)))
        for line in open(path.join(sql_file_path, SQL_FILE)):
            if line[:2] != "--":
                sql_statement += line
            if ";" in line:
                cursor.execute(sql_statement)
                sql_statement = ""

        if populate:
            self._populate_db()

    def _populate_db(self):
        """Populating the DB from the categories in settings file """

        cursor = self.db_instance.cursor()

        for each in CATEGORIES:
            query = "INSERT INTO Categories (name) VALUES ('%s');" % each
            cursor.execute(query)
            self.db_instance.commit()

            data = DataScraper.get_api_category(each)
            self._add_data_to_db(data)

    def _add_data_to_db(self, payload):
        """Puts data payloads to DB """

        cursor = self.db_instance.cursor()

        category = payload["category"]
        query = "SELECT id FROM Categories WHERE name ='%s';" % category
        cursor.execute(query)
        category_id = cursor.fetchone()[0]

        for each in payload["content"]:
            query = (
                "INSERT INTO Products "
                "(name, category, nutriscore, stores)"
                "VALUES (%s, %s, %s, %s);"
            )
            values = [
                each["product_name"],
                category_id,
                each["nutriscore"],
                each["stores"],
            ]
            cursor.execute(query, values)

        self.db_instance.commit()

    def get_categories(self):
        """Returns the categories from DB """

        cursor = self.db_instance.cursor()
        query = "SELECT id, name FROM Categories;"
        cursor.execute(query)
        return cursor.fetchall()

    def add_favorite(self, fav_id, subst_id):
        """Adds a favorite to DB """

        cursor = self.db_instance.cursor()
        query = (
            "INSERT INTO Favorites"
            "(product_id, substitued_id)"
            "VALUES (%s, %s);"
        )
        cursor.execute(query, (fav_id, subst_id))
        self.db_instance.commit()

    def get_favorites(self):
        """Get favorites from DB """

        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Favorites;"
        cursor.execute(query)
        return cursor.fetchall()

    def get_products_from_category(self, category_id, limit=75):
        """Returns a list of product from DB, found by category """

        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Products WHERE category = %s LIMIT %s;"
        cursor.execute(query, (category_id, limit))
        return cursor.fetchall()

    def find_product(self, search):
        """Returns a product from DB, found by name """

        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Products WHERE name LIKE %s;"
        cursor.execute(query, ("%" + search + "%",))
        return cursor.fetchall()

    def get_product_from_id(self, product_id):
        """Returns a product from DB, found by id """

        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Products WHERE id = %s;"
        cursor.execute(query, (product_id,))
        return cursor.fetchone()
