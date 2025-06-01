import tkinter as tk
from tkinter import ttk
from Banco.Banco import Banco
from Repositorios.AlunoRepository import AlunoRepository
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
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.dados_compartilhados = {
            "matricula": tk.IntVar()
        }

        self.frames = {}

        for Tela in (TelaLogin,TelaCadastro, TelaAluno, TelaAdmin):
            frame = Tela(parent=container, controller=self)
            self.frames[Tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(TelaLogin)

    def mostrar_tela(self, tela):
        frame = self.frames[tela]

        self.estilo()

        if hasattr(frame, "atualiza_dados"):
            frame.atualiza_dados()
        if hasattr(frame, "atualizar") :
            frame.atualizar()
        frame.tkraise()

    def estilo(self):

        self.style.theme_use('default')

        self.style.configure("Treeview",
                             background="#D3D3D3",
                             foreground="black",
                             rowheight=25,
                             fieldbackground="#D3D3D3")

        self.style.map('Treeview',
                       background=[('selected', "#347083")])

if __name__ == "__main__":
    app = App()
    app.mainloop()
    Banco.get_instance().close()