from Banco.Banco import Banco
from Models.Disciplina import Disciplina

class DisciplinaRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_disciplinas_by_curso(self, id_curso: int):
        return self.banco.select('''SELECT d.codigo, d.nome, c.nome
                FROM 
                    disciplina AS d
                JOIN
                    curso AS c 
                ON 
                    d.id_curso = c.id
                WHERE   
                    c.id = ?''', (id_curso,))

    def get_disciplinas(self):
        return self.banco.select('''SELECT d.codigo, d.nome, c.nome
        FROM 
            disciplina AS d
        JOIN
            curso c ON d.id_curso = c.id''', ())

    def get_columns_names(self):
        return self.banco.select("PRAGMA table_info(disciplina)")

    def adicionar_disciplina(self, disciplina: Disciplina):
        self.banco.execute("INSERT INTO disciplina (codigo, nome, id_curso) VALUES (?, ?, ?)",
                           (disciplina.codigo, disciplina.nome, disciplina.id_curso))

    def editar(self, codigo: str, nome: str):
        self.banco.execute("UPDATE disciplina SET nome = ? WHERE codigo = ?",
                           (nome, codigo))

    def remove(self, codigo: str):
        self.banco.execute("DELETE FROM disciplina WHERE codigo = ?", (codigo,))