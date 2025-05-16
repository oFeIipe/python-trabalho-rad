from Banco.Banco import Banco
from Models.Aluno import Aluno

class AlunoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def create_aluno(self, aluno: Aluno):
        self.banco.execute("INSERT INTO aluno (matricula, nome, id_curso) VALUES(%s, %s, %s)",
                          (aluno.matricula, aluno.nome, aluno.id_curso))
    def get_alunos(self) -> tuple:
        return self.banco.select("SELECT * FROM aluno", ())

    def get_aluno_by_matricula(self, matricula: str) -> tuple:
        return self.banco.select("SELECT * FROM aluno WHERE matricula = %s", (matricula,))

    def update_aluno(self, aluno: Aluno):
        self.banco.execute("UPDATE aluno SET nome = %s WHERE matricula = %s",
                           (aluno.nome, aluno.matricula))