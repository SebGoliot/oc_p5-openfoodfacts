import mysql.connector as db_connector
from openfoodfacts.controller.data_scraper import DataScraper
from openfoodfacts.settings import *


class DbManager():

    def __init__(self):
        self._db_instance = None

    @property
    def db_instance(self):
        """Get a connection to the db"""

        if not self._db_instance:
            self._db_instance = db_connector.connect(**MYSQL_CONFIG)
            try:
                self._db_instance.database = DB_NAME
            except:
                print('Base de données introuvable !\n'
                    'Veuillez patienter...')
                self.create_db(populate=True)
        return self._db_instance

    def create_db(self, drop=False, populate=False):
        """Creates the database and tables"""

        cursor = self.db_instance.cursor()
        sql_statement = ''

        if drop:
            cursor.execute(f'DROP DATABASE `{DB_NAME}`')

        for line in open(SQL_FILE):
            if line[:2] != '--':
                sql_statement += line
            if ';' in line:
                cursor.execute(sql_statement)
                sql_statement = ''

        if populate:
            self._populate_db()

    def _populate_db(self):
        """Getting data from listed categories to DB"""

        cursor = self.db_instance.cursor()

        for each in CATEGORIES:
            query = "INSERT INTO Categories (name) VALUES ('%s');" % each
            cursor.execute(query)
            self.db_instance.commit()

            data = DataScraper.get_api_category(each)
            self._add_data_to_db(data)

    def _add_data_to_db(self, payload):
        """Puts data payloads to DB"""

        cursor = self.db_instance.cursor()

        category = payload['category']
        query = "SELECT id FROM Categories WHERE name ='%s';" % category
        cursor.execute(query)
        category_id = cursor.fetchone()[0]

        for each in payload['content']:
            query = ("INSERT INTO Products "
                "(name, category, nutriscore, stores)"
                "VALUES (%s, %s, %s, %s);")
            values = [
                each['product_name'],
                category_id,
                each['nutriscore'],
                each['stores']
            ]
            cursor.execute(query, values)

        self.db_instance.commit()

    def get_categories(self):
        cursor = self.db_instance.cursor()
        query = "SELECT id, name FROM Categories;"
        cursor.execute(query)
        return cursor.fetchall()

    def add_favorite(self, fav_id, subst_id):
        cursor = self.db_instance.cursor()
        query = ("INSERT INTO Favorites"
            "(product_id, substitued_id)"
            "VALUES (%s, %s);")
        cursor.execute(query, (fav_id, subst_id))
        self.db_instance.commit()

    def get_favorites(self):
        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Favorites;"
        cursor.execute(query)
        return cursor.fetchall()

    def get_products_from_category(self, category_id, limit=75):
        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Products WHERE category = %s LIMIT %s;"
        cursor.execute(query, (category_id, limit))
        return cursor.fetchall()

    def find_product(self, search):
        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Products WHERE name LIKE %s;"
        cursor.execute(query, ('%'+search+'%',))
        return cursor.fetchall()

    def get_product_from_id(self, product_id):
        cursor = self.db_instance.cursor()
        query = "SELECT * FROM Products WHERE id = %s;"
        cursor.execute(query, (product_id,))
        return cursor.fetchone()
