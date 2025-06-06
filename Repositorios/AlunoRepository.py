from Banco.Banco import Banco
from Models.Aluno import Aluno

class AlunoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def create_aluno(self, aluno: Aluno):
        self.banco.execute("INSERT INTO aluno (matricula, nome, id_curso, senha) VALUES(?, ?, ?, ?)",
                          (aluno.matricula, aluno.nome, aluno.id_curso, aluno.senha))

    def get_aluno_by_matricula(self, matricula: int) -> tuple:
        return self.banco.select("SELECT * FROM aluno WHERE matricula = ?", (matricula,))

    def update_aluno(self, nome: str, matricula: int, senha: str):
        self.banco.execute("UPDATE aluno SET nome = ?, senha = ?  WHERE matricula = ?",
                           (nome, senha, matricula))

    def update_nome(self, nome: str, matricula: int):
        self.banco.execute("UPDATE aluno SET nome = ?  WHERE matricula = ?",
                           (nome, matricula))

    def delete_aluno(self, matricula: int) -> None:
        self.banco.execute("DELETE FROM aluno WHERE matricula = ?", (matricula,))
        self.banco.execute("DELETE FROM inscricao WHERE matricula_aluno = ?", (matricula,))