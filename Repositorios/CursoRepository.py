from Banco.Banco import Banco
from Models.Curso import Curso

class CursoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()