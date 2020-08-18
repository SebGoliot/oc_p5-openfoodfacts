import mysql.connector as db_connector
from mysql.connector.connection import MySQLConnection
from controller.data_scraper import DataScraper
from settings import *

class DbManager():

    def __init__(self):
        self._db_instance = MySQLConnection()


    @property
    def db_instance(self):
        """Get a connection to the db"""

        if not self._db_instance.is_connected():
            self._db_instance = db_connector.connect(**MYSQL_CONFIG)
        return self._db_instance


    def create_db(self):
        """Creates the database and tables from an sql file"""

        sql_statement = ''
        for line in open(SQL_FILE):
            if line[:2] != '--':
                sql_statement += line
            if ';' in line:
                self.db_instance.cursor().execute(sql_statement)
                sql_statement = ''


