from Banco.Banco import Banco
from Models.Inscricao import Inscricao
from Models.Nota import Nota

class InscricaoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_inscricoes(self):
        return self.banco.select("SELECT * FROM inscricao")

    def get_columns_names(self):
        return self.banco.select("PRAGMA table_info(inscricao)")