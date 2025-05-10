import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class Banco:
    _instance = None

    def __init__(self):
        self.conn = psycopg2.connect(
                host=os.getenv("HOST"),
                port=os.getenv("PORT"),
                database=os.getenv("BCD"),
                user=os.getenv("USER"),
                password=os.getenv("SENHA")
        )
        self.cursor = self.conn.cursor()
        self.conn.commit()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def execute(self, sql, params=()):
        self.cursor.execute(sql, params)
        self.conn.commit()

    def select(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()