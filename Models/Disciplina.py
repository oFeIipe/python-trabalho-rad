class Disciplina:
    def __init__(self, codigo: str, nome: str, id_curso: int, ano: int, semestre: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self.id_curso = id_curso
        self.ano = ano
        self.semestre = semestre