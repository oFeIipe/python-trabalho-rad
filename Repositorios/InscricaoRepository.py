from Banco.Banco import Banco
from Models.Inscricao import Inscricao
from Models.Nota import Nota

class InscricaoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()