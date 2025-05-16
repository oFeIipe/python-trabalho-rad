from Banco.Banco import Banco
from Models.Aluno import Aluno
from Repositorios.AlunoRepository import AlunoRepository

banco = Banco.get_instance()

banco.create_tables()