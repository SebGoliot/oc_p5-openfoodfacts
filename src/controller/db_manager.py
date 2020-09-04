import mysql.connector as db_connector
from controller.data_scraper import DataScraper
from model.product import Product
from settings import *


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
            print(f'inserting category {each}')
            query = f"INSERT INTO Categories (name) VALUES ('%s');" % each
            cursor.execute(query)
            self.db_instance.commit()

            data = DataScraper.get_api_category(each)
            self._add_data_to_db(data)

    def _add_data_to_db(self, payload):
        """Puts data payloads to DB"""

        cursor = self.db_instance.cursor()

        category = payload['category']
        query = f"SELECT id FROM Categories WHERE name ='%s';" % category
        cursor.execute(query)
        category_id = cursor.fetchone()[0]

        for each in payload['content']:
            query = f"""INSERT INTO Products
                (name, category, nutriscore, stores)
                VALUES (%s, %s, %s, %s);"""
            values = [
                each['product_name'],
                category_id,
                each['nutriscore'],
                each['stores']
            ]
            print(f'inserting item {values[0]}')
            cursor.execute(query, values)

        self.db_instance.commit()

    def get_categories(self):
        cursor = self.db_instance.cursor()
        query = "SELECT id, name FROM Categories;"
        cursor.execute(query)
        return cursor.fetchall()
