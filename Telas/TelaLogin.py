import tkinter as tk
from tkinter import ttk, messagebox

from Models.Aluno import gerar_hesh
from Repositorios.AlunoRepository import AlunoRepository
from Telas.TelaAdmin import TelaAdmin
from Telas.TelaAluno import TelaAluno


class TelaLogin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.aluno_repository = AlunoRepository()

        ttk.Label(self, text="Login", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        ttk.Label(self, text="Matrícula:").grid(row=1, column=0, padx=10, pady=10, sticky="E")

        self.entry_matricula = ttk.Entry(self)
        self.entry_matricula.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        ttk.Label(self, text="Senha:").grid(row=2, column=0, padx=10, pady=10, sticky="E")

        self.entry_senha = ttk.Entry(self)
        self.entry_senha.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        ttk.Button(self, text="Entrar", width=15, command=self.entrar_tela_inicial).grid(row=3, column=0, padx=10, pady=20)

        ttk.Button(self, text="Matricular-se", width=15, command=self.entrar_cadastro_aluno).grid(row=3, column=1, padx=10, pady=20)

    def entrar_tela_inicial(self):
        matricula = self.entry_matricula.get()
        senha = self.entry_senha.get()

        if len(matricula) < 4:
            messagebox.showerror("ERRO", "Matrícula inválida!")
            return

        if matricula == "admin" and senha == "admin":
            self.controller.geometry("1125x350")
            self.controller.mostrar_tela(TelaAdmin)
            self.limpar_tela()

        elif self.verifica_login(int(matricula), senha):
            self.controller.dados_compartilhados["matricula"].set(int(matricula))
            self.controller.geometry("720x330")
            self.controller.mostrar_tela(TelaAluno)
            self.limpar_tela()
        else:
            messagebox.showerror("ERRO", "Matrícula ou senha inválidas!")

    def verifica_login(self, matricula: int, senha: str):
        aluno = self.aluno_repository.get_aluno_by_matricula(matricula)

        senha_hash = gerar_hesh(senha)
        senha_aluno = aluno[0][3]

        return senha_hash == senha_aluno
    def limpar_tela(self):
        self.entry_senha.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)

    def entrar_cadastro_aluno(self):
        from Telas.TelaCadastro import TelaCadastro
        self.controller.geometry("230x230")
        self.controller.mostrar_tela(TelaCadastro)