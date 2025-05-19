import tkinter as tk
from tkinter import ttk, Tk, messagebox


from Telas.TelaCadastro import TelaCadastro


class TelaLogin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Faça login ou matricule-se", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        ttk.Label(self, text="Matrícula:").grid(row=1, column=0, padx=10, pady=10, sticky="E")

        self.entry_matricula = ttk.Entry(self, textvariable=controller.dados_compartilhados["matricula"])
        self.entry_matricula.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        ttk.Button(self, text="Entrar", width=15, command=self.entrar_tela_inicial).grid(row=2, column=0, padx=10, pady=20)

        ttk.Button(self, text="Matricular-se", width=15, command=self.entrar_cadastro_aluno).grid(row=2, column=1, padx=10, pady=20)

    def entrar_tela_inicial(self):
        matricula = self.controller.dados_compartilhados["matricula"].get()

        if len(matricula) < 4:
            messagebox.showerror("ERRO", "Matrícula inválida!")
            return

        print(f"Matrícula digitada: {matricula}")

    def entrar_cadastro_aluno(self):
        self.controller.geometry("230x200")
        self.controller.mostrar_tela(TelaCadastro)