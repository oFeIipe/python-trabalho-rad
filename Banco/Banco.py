# banco.py
import psycopg2
import os
from dotenv import load_dotenv
import inspect

load_dotenv()

class Banco:
    _instance = None

    def __init__(self):
        self.__conn = psycopg2.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("BCD"),
            user=os.getenv("USER"),
            password=os.getenv("SENHA")
        )
        self.__cursor = self.__conn.cursor()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def execute(self, sql, params=()):
        try:
            self.__cursor.execute(sql, params)
            self.__conn.commit()
        except psycopg2.DatabaseError as e:
            caller = inspect.stack()[1].function
            print(f"Erro causado por: {caller}")
            print("ERRO DE CONECTIVIDADE:", e)

    def select(self, sql, params=()):
        try:
            self.__cursor.execute(sql, params)
            return self.__cursor.fetchall()
        except psycopg2.DatabaseError as e:
            caller = inspect.stack()[1].function
            print(f"Erro causado por: {caller}")
            print("ERRO DE CONECTIVIDADE:", e)
            return []

    def close(self):
        self.__cursor.close()
        self.__conn.close()
