from Banco.Banco import Banco
from Models.Curso import Curso

class CursoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_cursos(self):
        return self.banco.select("SELECT * FROM curso", ())

    def get_columns_names(self):
        return self.banco.select("PRAGMA table_info(curso)")

    def insert_curso(self, curso: Curso):
        self.banco.execute("INSERT INTO curso (nome) VALUES(?)", (curso.nome,))