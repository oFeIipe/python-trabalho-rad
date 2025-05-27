import tkinter as tk
from tkinter import ttk
from Banco.Banco import Banco
from Models.Curso import Curso
from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository
from Telas.TelaAdmin import TelaAdmin
from Telas.TelaAluno import TelaAluno
from Telas.TelaCadastro import TelaCadastro
from Telas.TelaLogin import TelaLogin

aluno_repository = AlunoRepository()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Notas - Login")
        self.geometry("300x200")

        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview",
                             background="#D3D3D3",
                             foreground="black",
                             rowheight=25,
                             fieldbackground="#D3D3D3")

        self.style.map('Treeview',
                       background=[('selected', "#347083")])

        self.dados_compartilhados = {
            "matricula": tk.IntVar()
        }

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for Tela in (TelaLogin,TelaCadastro, TelaAluno, TelaAdmin):
            frame = Tela(parent=container, controller=self)
            self.frames[Tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(TelaLogin)

    def mostrar_tela(self, tela):
        frame = self.frames[tela]

        if hasattr(frame, "atualiza_dados"):
            frame.atualiza_dados()
        frame.tkraise()

cursos = [
    "Agronomia",
    "Arquitetura e Urbanismo",
    "Artes Cênicas",
    "Artes Visuais",
    "Biomedicina",
    "Biologia",
    "Ciências Contábeis",
    "Ciências Econômicas",
    "Cinema",
    "Design Gráfico",
    "Design de Produto",
    "Educação Física",
    "Engenharia Aeronáutica",
    "Engenharia Ambiental",
    "Engenharia de Alimentos",
    "Engenharia de Computação",
    "Engenharia de Controle e Automação",
    "Engenharia de Software",
    "Engenharia Eletrônica",
    "Engenharia Mecânica",
    "Engenharia Mecatrônica",
    "Engenharia Química",
    "Estatística",
    "Farmácia",
    "Filosofia",
    "Física",
    "Fisioterapia",
    "Fonoaudiologia",
    "Gastronomia",
    "Geografia",
    "Geologia",
    "Gestão de Recursos Humanos",
    "História",
    "Jogos Digitais",
    "Jornalismo",
    "Letras",
    "Logística",
    "Marketing",
    "Matemática",
    "Medicina Veterinária",
    "Nutrição",
]

if __name__ == "__main__":
    app = App()
    app.mainloop()

