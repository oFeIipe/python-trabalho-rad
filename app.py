from Models.Aluno import Aluno
from Repositorios.AlunoRepository import AlunoRepository

repository = AlunoRepository()



aluno = Aluno("Felipe Corsa de Carvalho", 1)

print(type(aluno.nome), type(aluno.matricula), type(aluno.id_curso))

repository.update_aluno(aluno)

select = repository.get_alunos()

print(select)