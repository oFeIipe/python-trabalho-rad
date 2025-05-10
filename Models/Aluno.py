from abc import ABC
from datetime import datetime
from random import randint

from Models.Pessoa import Pessoa

class Aluno(Pessoa, ABC):
    def __init__(self, nome: str, curso_id: int) -> None:
        super().__init__(nome)
        self.curso = curso_id

    def gerar_matricula(self):
        date = datetime.now()
        return date.strftime("%Y%m") + str(randint(111111, 999999))