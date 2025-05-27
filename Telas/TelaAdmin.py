import tkinter as tk
from tkinter import ttk, messagebox

from Models.Curso import Curso
from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository
from Repositorios.DisciplinaRepository import DisciplinaRepository
from Repositorios.InscricaoRepository import InscricaoRepository
from Repositorios.Treeview import Treeview


class TelaAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()
        self.disciplina_repository = DisciplinaRepository()
        self.inscricao_repository = InscricaoRepository()

        self.grid_columnconfigure(0, weight=1)
        self.controller = controller

        self.notebook = ttk.Notebook(self)

        self.notebook.grid(column=0, row=1, pady=30)

        self.curso_frame = ttk.Frame(self.notebook)
        self.disciplina_frame = ttk.Frame(self.notebook)
        self.inscricoes_frame = ttk.Frame(self.notebook)

        self.draw_curso_frame()
        self.draw_disciplina_frame()
        self.draw_inscricoes_frame()

        self.notebook.add(self.curso_frame, text="Curso")
        self.notebook.add(self.disciplina_frame, text="Disciplina")
        self.notebook.add(self.inscricoes_frame, text="Inscrições")


        ttk.Button(self, text="Sair", width=5, command=self.deslogar).place(x=1060, y=10)


        self.notebook.bind("<<NotebookTabChanged>>", self.ajustar_tamanho_aba)


        self.after(100, self.ajustar_tamanho_aba)

    def ajustar_tamanho_aba(self, event=None):
        aba_atual = self.notebook.select()
        frame = self.notebook.nametowidget(aba_atual)

        frame.update_idletasks()
        width = frame.winfo_reqwidth()
        height = frame.winfo_reqheight() + 100


        self.controller.geometry(f"{width}x{height}")

    def draw_curso_frame(self):

        frame_entrys = ttk.Frame(self.curso_frame, padding=10)
        frame_entrys.grid(row=0, column=0, sticky="NSW")

        frame_tree = ttk.Frame(self.curso_frame, padding=10)
        frame_tree.grid(row=0, column=1, sticky="NSE")


        ttk.Label(frame_entrys, text="Nome: ").grid(row=0, column=0, sticky="W")
        nome_curso_entry = ttk.Entry(frame_entrys, width=20)
        nome_curso_entry.grid(row=1, column=0, pady=5)


        ttk.Button(frame_entrys, text="Adicionar", command=lambda: self.criar_curso(nome_curso_entry, tree)).grid(row=2,
                                                                                                                  column=0,
                                                                                                                  pady=5)
        ttk.Button(frame_entrys, text="Editar", command=lambda: self.editar_curso(nome_curso_entry, tree)).grid(row=3,
                                                                                                                column=0,
                                                                                                                pady=5)

        colunas = [column[1] for column in self.curso_repository.get_columns_names()]
        data = self.curso_repository.get_cursos()
        tree = Treeview(frame_tree, colunas, data)

        #self.treeview_curso = tree

    def atualiza_view_cursos(self):
        self.controller.geometry("300x200")

    def draw_disciplina_frame(self):
        frame_entrys = ttk.Frame(self.disciplina_frame, padding=10)
        frame_entrys.grid(row=0, column=0, sticky="NSW")

        frame_tree = ttk.Frame(self.disciplina_frame, padding=10)
        frame_tree.grid(row=0, column=1, sticky="NSE")

        self.disciplina_frame.grid_columnconfigure(0, weight=1)
        self.disciplina_frame.grid_columnconfigure(1, weight=3)
        self.disciplina_frame.grid_rowconfigure(0, weight=1)

        ttk.Label(frame_entrys, text="Nome: ").grid(row=0, column=0, sticky="W")
        nome_disciplina_entry = ttk.Entry(frame_entrys, width=20)
        nome_disciplina_entry.grid(row=1, column=0, pady=5)

        ttk.Button(frame_entrys, text="Adicionar").grid(row=3, column=0, pady=10)

        colunas = [column[1] for column in self.disciplina_repository.get_columns_names()]

        data = self.disciplina_repository.get_disciplinas()

        Treeview(frame_tree, colunas, data)

    def draw_inscricoes_frame(self):

        frame_entrys = ttk.Frame(self.inscricoes_frame, padding=10)
        frame_entrys.grid(row=0, column=0, sticky="NSW")

        frame_tree = ttk.Frame(self.inscricoes_frame, padding=10)
        frame_tree.grid(row=0, column=1, sticky="NSE")

        colunas = [column[1] for column in self.inscricao_repository.get_columns_names()]
        data = self.inscricao_repository.get_inscricoes()

        Treeview(frame_tree, colunas, data)

    def criar_curso(self, nome_entry, tree):
        if len(nome_entry.get()) > 3:
            self.curso_repository.insert_curso(Curso(nome_entry.get()))
            data = self.curso_repository.get_cursos()
            tree.atualizar(data)
            nome_entry.delete(0, tk.END)
            messagebox.showinfo("SUCESSO", "Curso adicionada")
            return
        messagebox.showerror("ERRO", "Insira uma quantidade de caracteres válidos")

    def deslogar(self):
       from Telas.TelaLogin import TelaLogin
       self.controller.geometry("300x200")
       self.controller.mostrar_tela(TelaLogin)