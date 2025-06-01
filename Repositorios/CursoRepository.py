from Banco.Banco import Banco
from Models.Curso import Curso
from Repositorios.DisciplinaRepository import DisciplinaRepository

class CursoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()
        self.disciplina_repository = DisciplinaRepository()

    def get_cursos(self):
        return self.banco.select("SELECT * FROM curso", ())

    def insert_curso(self, curso: Curso):
        self.banco.execute("INSERT INTO curso (nome) VALUES(%s)", (curso.nome,))

    def editar(self, id: int, nome: str):
        self.banco.execute("UPDATE curso SET nome = %s WHERE id = %s", (nome, id))

    def remove(self, id: int):
        self.banco.execute("DELETE FROM curso WHERE id = %s", (id,))
        self.banco.execute("DELETE FROM disciplina WHERE id_curso = %s", (id,))
        self.banco.execute("DELETE FROM aluno WHERE id_curso = %s", (id,))
        codigos = [codigo[0] for codigo in self.disciplina_repository.get_disciplinas_by_curso(id)]
        for codigo in codigos:
            self.banco.execute("DELETE inscricao WHERE codigo_disciplina = %s", (codigo,))
