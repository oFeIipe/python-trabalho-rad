from Banco.Banco import Banco
from Models.Inscricao import Inscricao
from Models.Nota import Nota

class InscricaoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_inscricoes(self):
        return self.banco.select('''SELECT 
            ano,
            semestre,
            simulado_1,
            sim2,
            av,
            avs,
            nf,
            situacao,
            a.nome AS nome_aluno,
            d.nome AS nome_disciplina
        FROM 
            inscricao i
        JOIN 
            aluno a ON i.matricula_aluno = a.matricula
        JOIN 
            disciplina d ON i.codigo_disciplina = d.codigo;''')

    def get_columns_names(self):
        return self.banco.select("PRAGMA table_info(inscricao)")