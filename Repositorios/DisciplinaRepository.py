from Banco.Banco import Banco
from Models.Disciplina import Disciplina

class DisciplinaRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_disciplinas_by_aluno(self, matricula: int):
        return self.banco.select('''SELECT d.codigo, d.nome, d.ano, d.semestre
                FROM disciplina d
                JOIN aluno a ON d.id_curso = a.id_curso
                WHERE a.matricula = ?
                AND d.codigo NOT IN (
                    SELECT i.codigo_disciplina
                    FROM inscricao i
                    WHERE i.matricula_aluno = a.matricula)''', (matricula,))
    def get_disciplinas_by_curso(self, id: int):
        return self.banco.select('''SELECT d.codigo, d.nome, c.nome, d.ano, d.semestre
            FROM 
                disciplina AS d
            JOIN
                curso c ON d.id_curso = c.id
            WHERE d.id_curso = ?''', (id,))

    def get_disciplinas(self):
        return self.banco.select('''SELECT d.codigo, d.nome, c.nome, d.ano, d.semestre
        FROM 
            disciplina AS d
        JOIN
            curso c ON d.id_curso = c.id''', ())

    def adicionar_disciplina(self, disciplina: Disciplina):
        self.banco.execute("INSERT INTO disciplina (codigo, nome, id_curso, ano, semestre) VALUES (?, ?, ?, ?, ?)",
                           (disciplina.codigo, disciplina.nome, disciplina.id_curso, disciplina.ano, disciplina.semestre))

    def get_by_curso_id(self, id: int):
        return self.banco.select("SELECT codigo, nome FROM disciplina WHERE id_curso = ?", (id,))

    def get_all_to_dict(self):
        return self.banco.select("SELECT codigo, nome FROM disciplina", ())

    def editar(self, codigo: str, nome: str, ano: int, semestre: int):
        self.banco.execute("UPDATE disciplina SET nome = ?, ano = ?, semestre = ? WHERE codigo = ?",
                           (nome, ano, semestre, codigo))

    def remove(self, codigo: str):
        self.banco.execute("DELETE FROM disciplina WHERE codigo = ?", (codigo,))
        self.banco.execute("DELETE FROM inscricao WHERE codigo_disciplina = ?", (codigo,))

    def get_disciplina_by_name(self, nome: str):
        return self.banco.select("SELECT codigo FROM disciplina WHERE nome = ?", (nome,))