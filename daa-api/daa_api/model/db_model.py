import psycopg2
from dotenv import load_dotenv
import os
from flask import jsonify
from daa_api import logger

import json


class PostgresSingleton:

    __instance = None
    def __init__(self) -> None:
        try:
            load_dotenv(os.path.join(os.getcwd(), '.env'))
            self.host = os.getenv('PGHOST')
            self.user = os.getenv('PGUSER')
            self.password = os.getenv('PGPASSWORD')
            self.dbname = os.getenv('PGDATABASE')
            self.port = os.getenv('PGPORT')
            print(self.host, self.user, self.password, self.dbname, self.port)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PostgresSingleton.__instance == None:
            PostgresSingleton.__instance = PostgresSingleton()
        return PostgresSingleton.__instance
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(host=self.host, user=self.user, password=self.password, dbname=self.dbname, port=self.port)
            self.cur = self.conn.cursor()
            print("Connected to Postgres")
        except Exception as e:
            logger.error(f'Error connecting to Postgres: {e}')
            return None
        
    def disconnect(self):
        try:
            self.cur.close()
            self.conn.close()
            print("Disconnected from Postgres")
        except Exception as e:
            print("Error disconnecting from Postgres: ", e)
            return None
        
    def execute(self, query, params=None):
        try:
            self.cur.execute(query, params)
            self.conn.commit()
        except Exception as e:
            logger.error(f'Error executing query: {e}')
            self.conn.rollback()
            raise e
    
    def fetchOne(self):
        try:
            return self.cur.fetchone()
        except Exception as e:
            #print("Error fetching one: ", e)
            return None
        
    def fetchAll(self):
        try:
            return self.cur.fetchall()
        except Exception as e:
            #print("Error fetching all: ", e)
            return None