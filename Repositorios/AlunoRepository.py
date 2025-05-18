from Banco.Banco import Banco
from Models.Aluno import Aluno

class AlunoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def create_aluno(self, aluno: Aluno):
        self.banco.execute("INSERT INTO aluno (matricula, nome, id_curso) VALUES(?, ?, ?)",
                          (aluno.matricula, aluno.nome, aluno.id_curso))

    def get_alunos(self) -> tuple:
        return self.banco.select("SELECT * FROM aluno", ())

    def get_aluno_by_matricula(self, matricula: int) -> tuple:
        return self.banco.select("SELECT * FROM aluno WHERE matricula = ?", (matricula,))

    def update_aluno(self, nome: str, matricula: int):
        self.banco.execute("UPDATE aluno SET nome = ? WHERE matricula = ?",
                           (nome, matricula))
    def get_matriculas(self):
        return self.banco.select("SELECT matricula FROM aluno", ())

    def delete_aluno(self, matricula: int) -> None:
        self.banco.execute("DELETE FROM aluno WHERE matricula = ?", (matricula,))