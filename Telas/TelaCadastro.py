import tkinter as tk
from tkinter import ttk, messagebox

from Models.Aluno import Aluno
from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository



class TelaCadastro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()
        self.dict_cursos = dict(self.curso_repository.get_cursos())
        selected_key = tk.StringVar()

        self.controller = controller



        ttk.Label(self, text="Cadastro", font=("Arial", 16, "bold")).grid(row=0, column=1,
                                                                                            columnspan=3, pady=10,
                                                                                            padx=10)

        ttk.Label(self, text="Nome:").grid(row=1, column=0, padx=10, pady=10, sticky="E")

        self.entry_nome = ttk.Entry(self, width=23)
        self.entry_nome.grid(row=1, column=1, pady=10, sticky="W")

        ttk.Label(self, text="Senha:").grid(row=2, column=0, padx=10, pady=10, sticky="E")

        self.entry_senha = ttk.Entry(self, width=23, show="*")
        self.entry_senha.grid(row=2, column=1, pady=10, sticky="W")


        ttk.Label(self, text="Curso:").grid(row=3, column=0, padx=10, pady=10, sticky="E")
        self.combobox = ttk.Combobox(self, textvariable=selected_key, values=list(self.dict_cursos.values()), state="readonly")
        self.combobox.grid(row=3, column=1, pady=10, sticky="W")



        ttk.Button(self, text="<-", width=5, command=self.voltar).grid(row=0, column=0)
        ttk.Button(self, text="Confirmar", width=15, command=self.criar_aluno).grid(row=4, column=0,  columnspan=3, pady=20, sticky="N")


    def criar_aluno(self):
        from Telas.TelaAluno import TelaAluno
        try:
            nome = self.entry_nome.get()
            id_curso = int({v: k for k, v in self.dict_cursos.items()}.get(self.combobox.get()))
            senha = self.entry_senha.get()

            aluno = Aluno(nome, id_curso, senha)

            self.aluno_repository.create_aluno(aluno)

        except Exception:
            messagebox.showerror("ERRO", "Não foi possível fazer o cadastro")
        else:
            messagebox.showinfo("Bem-vindo", f"Seu cadastro foi realizado com sucesso!\nSua Matricula é: {aluno.matricula}")
            self.controller.dados_compartilhados["matricula"].set(aluno.matricula)

            self.controller.geometry("770x450")
            self.controller.mostrar_tela(TelaAluno)
            self.limpar_tela()

    def atualizar(self):
        self.controller.title("Cadastro")
        self.dict_cursos = dict(self.curso_repository.get_cursos())
        self.combobox.config(values=list(self.dict_cursos.values()))

    def limpar_tela(self):
        self.entry_senha.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.combobox.delete(0, tk.END)

    def voltar(self):
       from Telas.TelaLogin import TelaLogin
       self.limpar_tela()
       self.controller.geometry("300x200")
       self.controller.mostrar_tela(TelaLogin)