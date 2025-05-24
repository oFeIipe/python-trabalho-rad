import tkinter as tk
from tkinter import ttk, messagebox

from Models.Aluno import Aluno
from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository


class TelaAluno(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()
        self.dict_cursos = dict(self.curso_repository.get_cursos())

        self.controller = controller

    def montar_tela(self):
        pass

    def atualiza_dados(self):

        matricula = self.controller.dados_compartilhados["matricula"].get()
        self.grid_columnconfigure(1, weight=1)

        aluno = self.aluno_repository.get_aluno_by_matricula(matricula)
        ttk.Label(self, text=f"Bem vindo {aluno[0][1]}!", font=("Arial", 16, "bold")).grid(row=0, column=0,
                                                                            pady=10,
                                                                            padx=10)
        ttk.Button(self, text="Sair", width=5, command=self.deslogar).place(x=670, y=10)

    def deslogar(self):
       from Telas.TelaLogin import TelaLogin
       self.controller.geometry("300x200")
       self.controller.mostrar_tela(TelaLogin)