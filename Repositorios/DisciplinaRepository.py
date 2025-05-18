from Banco.Banco import Banco
from Models.Disciplina import Disciplina

class DisciplinaRepository:
    def __init__(self):
        self.banco = Banco.get_instance()