from abc import ABC
from datetime import datetime
from random import randint

from Models.Pessoa import Pessoa

class Professor(Pessoa, ABC):
    def __init__(self,nome: str) -> None:
        super().__init__(nome)

    def gerar_matricula(self):
        date = datetime.now()
        return date.strftime("%Y%m") + str(randint(1111, 9999))