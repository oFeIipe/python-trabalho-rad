import sqlite3
import inspect

comandos_criacao = [
    """
    CREATE TABLE IF NOT EXISTS curso (
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS disciplina (
        codigo TEXT PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        semestre INTEGER NOT NULL,
        id_curso INTEGER NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES curso(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS aluno (
        matricula INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        id_curso INTEGER NOT NULL,
        senha TEXT NOT NULL,
        FOREIGN KEY (id_curso) REFERENCES curso(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS inscricao (
        id INTEGER PRIMARY KEY NOT NULL,
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


class Banco:
    _instance = None

    def __init__(self):
        self.__conn = sqlite3.connect('escola.db')
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

    def get_conn(self):
        return self.__conn

    def close(self):
        self.__cursor.close()
        self.__conn.close()