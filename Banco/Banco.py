import os
import psycopg2
import inspect
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()

comandos_criacao = [
    """
    CREATE TABLE IF NOT EXISTS curso (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS disciplina (
        codigo TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        semestre INTEGER NOT NULL,
        id_curso INTEGER NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES curso(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS aluno (
        matricula SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        id_curso INTEGER NOT NULL,
        senha TEXT NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES curso(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS inscricao (
        id SERIAL PRIMARY KEY,
        sim1 REAL,
        sim2 REAL,
        av REAL,
        avs REAL,
        nf REAL,
        situacao TEXT,
        matricula_aluno INTEGER NOT NULL,
        codigo_disciplina TEXT NOT NULL,
        FOREIGN KEY (matricula_aluno) REFERENCES aluno(matricula),
        FOREIGN KEY (codigo_disciplina) REFERENCES disciplina(codigo)
    );
    """
]


def get_conn():
    engine = create_engine(os.getenv('CONN'))
    return engine.connect()

class Banco:
    _instance = None

    def __init__(self):
        self.__conn = psycopg2.connect(
            dbname= os.getenv('DB_NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )
        self.__cursor = self.__conn.cursor()
        self.create_tables()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create_tables(self):
        for comando in comandos_criacao:
            self.execute(comando)

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