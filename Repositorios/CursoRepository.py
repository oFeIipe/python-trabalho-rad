from Banco.Banco import Banco
from Models.Curso import Curso

class CursoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_cursos(self):
        return self.banco.select("SELECT * FROM curso", ())