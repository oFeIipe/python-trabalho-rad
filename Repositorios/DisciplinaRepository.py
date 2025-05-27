from Banco.Banco import Banco
from Models.Disciplina import Disciplina

class DisciplinaRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_disciplinas(self):
        return self.banco.select("SELECT * FROM disciplina")

    def get_by_curso(self, curso_id: int):
        return self.banco.select("SELECT * FROM disciplina WHERE curso_id = ?", (curso_id,))

    def get_columns_names(self):
        return self.banco.select("PRAGMA table_info(disciplina)")

    def adicionar_disciplina(self, disciplina: Disciplina):
        self.banco.execute("INSERT INTO disciplina (codigo, nome, id_curso) VALUES (?, ?, ?)",
                           (disciplina.codigo, disciplina.nome, disciplina.id_curso))