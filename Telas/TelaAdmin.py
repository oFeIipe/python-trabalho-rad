import tkinter as tk
from tkinter import ttk, messagebox

from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository


class TelaAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()
        self.dict_cursos = dict(self.curso_repository.get_cursos())

        self.controller = controller

        ttk.Label(self, text=f"Bem vindo ADM", font=("Arial", 16, "bold")).grid(row=0, column=1,
                                                                                            columnspan=3, pady=10,
                                                                                            padx=10)

    def montar_tela(self):
        pass

    def deslogar(self):
       from Telas.TelaLogin import TelaLogin
       self.controller.geometry("300x200")
       self.controller.mostrar_tela(TelaLogin)