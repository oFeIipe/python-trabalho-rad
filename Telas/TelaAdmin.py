import tkinter as tk
from tkinter import ttk, messagebox

from Models.Curso import Curso
from Models.Disciplina import Disciplina
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

        self.dict_cursos = dict(self.curso_repository.get_cursos())

        self.grid_columnconfigure(0, weight=1)
        self.controller = controller

        self.notebook = ttk.Notebook(self, width=1125)

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


    def draw_curso_frame(self):

        frame_entrys = ttk.Frame(self.curso_frame, padding=10)
        frame_entrys.grid(row=0, column=0, sticky="NSW")

        frame_tree = ttk.Frame(self.curso_frame, padding=10)
        frame_tree.grid(row=0, column=1, sticky="NSE")

        self.curso_frame.grid_columnconfigure(0, weight=2)
        self.curso_frame.grid_columnconfigure(1, weight=3)
        self.curso_frame.grid_rowconfigure(0, weight=1)

        ttk.Label(frame_entrys, text="Nome: ").grid(row=0, column=0, sticky="W")
        self.name_curso_entry = ttk.Entry(frame_entrys, width=20)
        self.name_curso_entry.grid(row=1, column=0, pady=5)


        ttk.Button(frame_entrys, text="Adicionar", command=self.adicionar_curso).place(y=120)
        ttk.Button(frame_entrys, text="Editar", command=self.editar_curso).place(y=160)
        ttk.Button(frame_entrys, text="Excluir", command=self.exluir_curso).place(y=200)
        colunas = [column[1] for column in self.curso_repository.get_columns_names()]
        data = self.curso_repository.get_cursos()
        width = int(800 / len(colunas))

        self.tree_curso = Treeview(frame_tree, colunas, data, width)

        self.tree_curso.bind("<<TreeviewSelect>>", self.on_curso_select)




    def draw_disciplina_frame(self):
        frame_entrys = ttk.Frame(self.disciplina_frame, padding=10)
        frame_entrys.grid(row=0, column=0, sticky="NSW")

        frame_tree = ttk.Frame(self.disciplina_frame, padding=10)
        frame_tree.grid(row=0, column=1, sticky="NSE")

        self.disciplina_frame.grid_columnconfigure(0, weight=1)
        self.disciplina_frame.grid_columnconfigure(1, weight=3)
        self.disciplina_frame.grid_rowconfigure(0, weight=1)

        colunas = [column[1] for column in self.disciplina_repository.get_columns_names()]
        width = int(800 / len(colunas))

        data = self.disciplina_repository.get_disciplinas()

        tree = Treeview(frame_tree, colunas, data, width)

        ttk.Label(frame_entrys, text="Nome: ").grid(row=0, column=0, sticky="W")
        nome_disciplina_entry = ttk.Entry(frame_entrys, width=20)
        nome_disciplina_entry.grid(row=1, column=0, pady=5)

        ttk.Label(frame_entrys, text="Código: ").grid(row=0, column=1, sticky="W")
        codigo_entry = ttk.Entry(frame_entrys, width=20)
        codigo_entry.grid(row=1, column=1, pady=5)

        selected_key = tk.StringVar()

        ttk.Label(frame_entrys, text="Curso").grid(row=2, column=0, sticky="W")
        combobox_curso = ttk.Combobox(frame_entrys, textvariable=selected_key,values=list(self.dict_cursos.values()),
                                     state="readonly")
        combobox_curso.grid(row=3, column=0, pady=5, padx=10, sticky="W")

        ttk.Button(frame_entrys, text="Adicionar", command=lambda: self.adicionar_disciplina(nome_disciplina_entry, combobox_curso, codigo_entry, tree)).grid(row=3, column=1, pady=10)
        ttk.Button(frame_entrys, text="Excluir", command=lambda: self.exluir_disciplina(tree)).grid(row=5, column=1, pady=10)


    def draw_inscricoes_frame(self):

        frame_entrys = ttk.Frame(self.inscricoes_frame, padding=10)
        frame_entrys.grid(row=0, column=0, sticky="NSW")

        frame_tree = ttk.Frame(self.inscricoes_frame, padding=10)
        frame_tree.grid(row=0, column=1, sticky="NSE")

        self.inscricoes_frame.grid_columnconfigure(0, weight=1)
        self.inscricoes_frame.grid_columnconfigure(1, weight=3)
        self.inscricoes_frame.grid_rowconfigure(0, weight=1)

        ttk.Label(frame_entrys, text="Nome: ").grid(row=0, column=0, sticky="W")
        nome_disciplina_entry = ttk.Entry(frame_entrys, width=20)
        nome_disciplina_entry.grid(row=1, column=0, pady=5)

        ttk.Button(frame_entrys, text="Adicionar").grid(row=3, column=0, pady=10)

        colunas = [column[1] for column in self.inscricao_repository.get_columns_names()]
        data = self.inscricao_repository.get_inscricoes()
        width = int(900 / len(colunas))

        Treeview(frame_tree, colunas, data, width)

    def on_curso_select(self, event):
        selected_item = self.tree_curso.focus()
        if selected_item:
            values = self.tree_curso.item(selected_item, 'values')
            if values:
                self.name_curso_entry.delete(0, tk.END)
                self.name_curso_entry.insert(0, values[1])

    def adicionar_curso(self):
        if len(self.name_curso_entry.get()) > 3:
            self.curso_repository.insert_curso(Curso(self.name_curso_entry.get()))
            data = self.curso_repository.get_cursos()
            self.tree_curso.atualizar(data)
            self.dict_cursos = dict(self.curso_repository.get_cursos())
            self.atualizar()
            self.name_curso_entry.delete(0, tk.END)
            messagebox.showinfo("SUCESSO!", "Curso adicionada!")
            return
        messagebox.showerror("ERRO!", "Não foi possível adicionar o curso")

    def adicionar_disciplina(self, nome_entry, curso_entry, codigo_entry, tree):
        nome = nome_entry.get()
        id_curso = int({v: k for k, v in self.dict_cursos.items()}.get(curso_entry.get()))
        codigo = codigo_entry.get()

        if len(nome) > 7 and id_curso and len(codigo) > 3:
            self.disciplina_repository.adicionar_disciplina(Disciplina(codigo, nome, id_curso))
            data = self.disciplina_repository.get_disciplinas()
            tree.atualizar(data)
            self.atualizar()
            nome_entry.delete(0, tk.END)
            curso_entry.delete(0, tk.END)
            codigo_entry.delete(0, tk.END)
            messagebox.showinfo("SUCESSO!", "Disciplina adicionada!")
            return
        messagebox.showerror("ERRO!", "Não foi possível adicionar a disciplina")

    def editar_curso(self):
        selected_item = self.tree_curso.focus()

        if selected_item:
            values = self.tree_curso.item(selected_item, 'values')
            self.curso_repository.editar(values[0], self.name_curso_entry.get())
            self.name_curso_entry.delete(0, tk.END)
            data = self.curso_repository.get_cursos()
            self.tree_curso.atualizar(data)
            self.atualizar()
            messagebox.showinfo("SUCESSO!", "Curso editado!")
            return
        messagebox.showerror("ERRO!", "Não foi editar o curso")

    def exluir_disciplina(self, tree):
        selected_item = tree.focus()

        if selected_item:
            values = tree.item(selected_item, 'values')
            self.disciplina_repository.remove(values[0])
            data = self.disciplina_repository.get_disciplinas()
            tree.atualizar(data)
            self.atualizar()
            messagebox.showinfo("SUCESSO!", "Disciplina removida!")
            return
        messagebox.showerror("ERRO!", "Não foi possível remover a disciplina")

    def exluir_curso(self):
        selected_item = self.tree_curso.focus()
        if selected_item:
            values = self.tree_curso.item(selected_item, 'values')
            self.curso_repository.remove(values[0])
            data = self.curso_repository.get_cursos()
            self.tree_curso.atualizar(data)
            self.atualizar()
            messagebox.showinfo("SUCESSO!", "Curso removido!")
            return
        messagebox.showerror("ERRO!", "Não foi possível remover o curso")

    def atualizar(self):
        self.draw_disciplina_frame()
        self.draw_curso_frame()
        self.draw_inscricoes_frame()


    def deslogar(self):
       from Telas.TelaLogin import TelaLogin
       self.controller.geometry("300x200")
       self.controller.mostrar_tela(TelaLogin)