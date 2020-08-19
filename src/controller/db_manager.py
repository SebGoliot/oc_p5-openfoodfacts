import mysql.connector as db_connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from controller.data_scraper import DataScraper
from settings import *

class DbManager():

    def __init__(self):
        self._db_instance = MySQLConnection()
        self._db_cursor = MySQLCursor()


    @property
    def db_instance(self):
        """Get a connection to the db"""

        if not self._db_instance.is_connected():
            self._db_instance = db_connector.connect(**MYSQL_CONFIG)
        return self._db_instance


    def create_db(self):
        """Creates the database and tables from an sql file"""

        cursor = self.db_instance.cursor()
        sql_statement = ''

        for line in open(SQL_FILE):
            if line[:2] != '--':
                sql_statement += line
            if ';' in line:
                cursor.execute(sql_statement)
                sql_statement = ''

        self._db_instance.database = DB_NAME
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
        query = f"SELECT * FROM Categories WHERE name ='%s';" % category
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

