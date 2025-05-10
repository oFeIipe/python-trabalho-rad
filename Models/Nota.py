class Nota:
    def __init__(self, sim1: float, sim2: float, av: float, avs: float) -> None:
        self.sim1 = sim1 or None
        self.sim2 = sim2 or None
        self.av = av or None
        self.avs = avs or None
        self.nf = self.calc_nf()
        self.situacao = self.get_situacao()

    def calc_nf(self):
        prova = self.av if self.av > self.avs else self.avs
        nota = prova + self.sim1 + self.sim2
        return round(nota, 2)

    def get_situacao(self):
        return "Aprovado" if self.nf >= 6 else "Reprovado"