import sqlite3
import os
from dotenv import load_dotenv
import inspect


load_dotenv()

comandos_criacao = [
    """
    CREATE TABLE IF NOT EXISTS curso (
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS professor (
        matricula INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS disciplina (
        codigo TEXT PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        matricula_professor INTEGER NOT NULL,
        FOREIGN KEY (matricula_professor) REFERENCES professor(matricula)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS aluno (
        matricula INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        id_curso INTEGER NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES curso(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS curso_professor (
        id INTEGER PRIMARY KEY NOT NULL,
        matricula_professor INTEGER NOT NULL,
        id_curso INTEGER NOT NULL,
        FOREIGN KEY (matricula_professor) REFERENCES professor(matricula),
        FOREIGN KEY (id_curso) REFERENCES curso(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS curso_disciplina (
        id INTEGER PRIMARY KEY NOT NULL,
        codigo_disciplina TEXT NOT NULL,
        id_curso INTEGER NOT NULL,
        FOREIGN KEY (codigo_disciplina) REFERENCES disciplina(codigo),
        FOREIGN KEY (id_curso) REFERENCES curso(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS inscricao (
        id INTEGER PRIMARY KEY NOT NULL,
        ano INTEGER NOT NULL,
        semestre INTEGER NOT NULL,
        simulado_1 REAL,
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




class Banco:
    _instance = None

    def __init__(self):
        '''self.__conn = psycopg2.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("BCD"),
            user=os.getenv("USER"),
            password=os.getenv("SENHA")
        )'''
        self.__conn = sqlite3.connect('escola.db')
        self.__cursor = self.__conn.cursor()

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
        except sqlite3.DatabaseError as e:
            caller = inspect.stack()[1].function
            print(f"Erro causado por: {caller}")
            print("ERRO DE CONECTIVIDADE:", e)

    def select(self, sql, params=()):
        try:
            self.__cursor.execute(sql, params)
            return self.__cursor.fetchall()
        except sqlite3.DatabaseError as e:
            caller = inspect.stack()[1].function
            print(f"Erro causado por: {caller}")
            print("ERRO DE CONECTIVIDADE:", e)
            return []

    def close(self):
        self.__cursor.close()
        self.__conn.close()