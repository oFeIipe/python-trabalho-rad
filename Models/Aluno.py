from abc import ABC
from datetime import datetime
from random import randint

from Models.Pessoa import Pessoa

class Aluno(Pessoa, ABC):
    def __init__(self, nome: str, id_curso: int) -> None:
        super().__init__(nome)
        self.id_curso = id_curso

    def gerar_matricula(self):
        date = datetime.now()
        return date.strftime("%Y%m") + str(randint(111111, 999999))