from Banco.Banco import Banco
from Models.Inscricao import Inscricao
from Models.Nota import Nota

class InscricaoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def get_inscricoes(self):
        return self.banco.select("SELECT ano, semestre, sim1, sim2, av, avs, nf, situacao, matricula_aluno, codigo_disciplina FROM inscricao")

    '''def get_inscricoes(self):
        return self.banco.select('SELECT 
            i.ano,
            i.semestre,
            i.sim1,
            i.sim2,
            i.av,
            i.avs,
            i.nf,
            i.situacao,
            a.nome AS nome_aluno,
            d.nome AS nome_disciplina
        FROM 
            inscricao i
        JOIN 
            aluno a ON i.matricula_aluno = a.matricula
        JOIN 
            disciplina d ON i.codigo_disciplina = d.codigo;')'''

    def insert_nota(self, nota: Nota, matricula: int, codigo: str):
        self.banco.select('''UPDATE inscricao 
            SET 
                sim1 = ?,
                sim2 = ?,
                av = ?,
                avs = ?,
                nf = ?,
                situacao = ?
            WHERE
                matricula_aluno = ?
            AND
                codigo_disciplina = ?''',(nota.sim1, nota.sim2, nota.av, nota.avs, nota.nf, nota.situacao, matricula, codigo))
