import tkinter as tk
from tkinter import ttk, messagebox

from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository


class TelaAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()

        self.grid_columnconfigure(0, weight=1)
        self.controller = controller

        self.notebook = ttk.Notebook(self)

        self.notebook.grid(column=0, row=1, pady=30)

        self.curso_frame = ttk.Frame(self.notebook, height=275, width=720)
        self.disciplina_frame = ttk.Frame(self.notebook, height=275, width=720)
        self.inscricoes_frame = ttk.Frame(self.notebook, height=275, width=720)

        self.notebook.add(self.curso_frame, text="Curso")
        self.notebook.add(self.disciplina_frame, text="Disciplina")
        self.notebook.add(self.inscricoes_frame, text="Inscrições")

        ttk.Button(self, text="Sair", width=5, command=self.deslogar).place(x=670, y=20)

    def montar_tela(self):
        pass

    def deslogar(self):
       from Telas.TelaLogin import TelaLogin
       self.controller.geometry("300x200")
       self.controller.mostrar_tela(TelaLogin)