import re
from datetime import datetime
from random import randint

class Aluno():
    def __init__(self, nome: str, id_curso: int) -> None:
        self.nome = nome
        self.id_curso = id_curso
        self.matricula = self.gerar_matricula()
        self.format_name()

    def format_name(self):
        self.nome = re.sub("[0-9!@#$%¨&*(){}_-]", "", self.nome)
        self.nome = self.nome.strip()
        self.nome = self.nome.split()
        self.nome = " ".join(self.nome)
        self.nome = self.nome.capitalize()

    def gerar_matricula(self):
        date = datetime.now()
        return date.strftime("%Y%m") + str(randint(111111, 999999))