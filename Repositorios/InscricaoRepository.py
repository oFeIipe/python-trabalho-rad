from Banco.Banco import Banco
from Models.Inscricao import Inscricao
from Models.Nota import Nota

class InscricaoRepository:
    def __init__(self):
        self.banco = Banco.get_instance()

    def insert_inscricao(self, inscricao: Inscricao):
        self.banco.execute('''INSERT INTO inscricao (matricula_aluno, codigo_disciplina) 
        VALUES (?, ?)''', (inscricao.aluno, inscricao.disciplina))

    def get_inscricoes(self):
        return self.banco.select('''SELECT 
        i.id,
        i.sim1,
        i.sim2,
        i.av,
        i.avs,
        i.nf,
        i.situacao,
        a.nome,
        d.nome
        FROM 
            inscricao As i
        JOIN
            disciplina as d ON d.codigo = i.codigo_disciplina
        JOIN
            aluno As a ON i.matricula_aluno = a.matricula''')

    def get_inscricoes_by_curso(self, id: int):
        return self.banco.select('''SELECT 
        i.id,
        i.sim1,
        i.sim2,
        i.av,
        i.avs,
        i.nf,
        i.situacao,
        a.nome,
        d.nome
        FROM 
            inscricao As i
        JOIN
            disciplina as d ON d.codigo = i.codigo_disciplina
        JOIN
            aluno AS a ON i.matricula_aluno = a.matricula
        WHERE d.id_curso = ?''', (id,))

    def insert_nota(self, nota: Nota, id: int):
        self.banco.execute('''UPDATE inscricao 
            SET 
                sim1 = ?,
                sim2 = ?,
                av = ?,
                avs = ?,
                nf = ?,
                situacao = ?
            WHERE
                id = ?''',(nota.sim1, nota.sim2, nota.av, nota.avs, nota.nf, nota.situacao, id))

    def get_inscricoes_by_aluno(self, matricula: int):
        return self.banco.select('''SELECT 
        d.nome,
        i.sim1,
        i.sim2,
        i.av,
        i.avs,
        i.nf,
        i.situacao
        FROM 
            inscricao As i
        JOIN
            disciplina as d ON d.codigo = i.codigo_disciplina
        JOIN
            aluno As a ON i.matricula_aluno = a.matricula
        WHERE 
            i.matricula_aluno = ?''', (matricula,))

    def get_inscricoes_by_disciplina(self, codigo: str):
        return self.banco.select('''SELECT 
               i.id,
               i.sim1,
               i.sim2,
               i.av,
               i.avs,
               i.nf,
               i.situacao,
               a.nome,
               d.nome
               FROM 
                   inscricao As i
               JOIN
                   disciplina as d ON d.codigo = i.codigo_disciplina
               JOIN
                   aluno AS a ON i.matricula_aluno = a.matricula
               WHERE d.codigo = ?''', (codigo,))

    def cancela_inscricao(self, matricula: int, codigo: str):
        self.banco.execute("DELETE FROM inscricao WHERE matricula_aluno = ? AND codigo_disciplina = ?", (matricula, codigo))