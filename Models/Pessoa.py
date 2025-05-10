import re
from abc import abstractmethod, ABC

class Pessoa(ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.matricula = self.gerar_matricula()
        self.format_name()

    def format_name(self):
        self.nome = re.sub("[0-9!@#$%¨&*(){}_-]", "", self.nome)
        self.nome = self.nome.strip()
        self.nome = self.nome.split()
        self.nome = " ".join(self.nome)
        self.nome = self.nome.capitalize()

    @abstractmethod
    def gerar_matricula(self):
        pass