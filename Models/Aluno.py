import re
from datetime import datetime
from random import randint
import hashlib


def gerar_hesh(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

class Aluno:
    def __init__(self, nome: str, id_curso: int, senha: str) -> None:
        self.nome = nome
        self.id_curso = id_curso
        self.matricula = None
        self.senha = gerar_hesh(senha)
        self.gerar_matricula()
        self.format_name()

    def format_name(self):
        self.nome = re.sub("[0-9!@#$%¨&*(){}_-]", "", self.nome)
        self.nome = self.nome.strip()
        self.nome = self.nome.split()
        self.nome = " ".join(self.nome)
        self.nome = self.nome.capitalize()

    def gerar_matricula(self):
        date = datetime.now()
        self.matricula =  date.strftime("%Y") + str(randint(10000, 99999))