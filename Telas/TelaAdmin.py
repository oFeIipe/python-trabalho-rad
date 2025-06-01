import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import ttk, messagebox
from Banco.Banco import Banco, get_conn
from Models.Curso import Curso
from Models.Disciplina import Disciplina
from Models.Nota import Nota
from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository
from Repositorios.DisciplinaRepository import DisciplinaRepository
from Repositorios.InscricaoRepository import InscricaoRepository
from Repositorios.Treeview import Treeview
import pandas as pd

class TelaAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()
        self.disciplina_repository = DisciplinaRepository()
        self.inscricao_repository = InscricaoRepository()
        self.banco = Banco.get_instance()

        self.clicked_filter = False

        self.dict_cursos = dict(self.curso_repository.get_cursos())
        self.dict_disciplinas = dict(self.disciplina_repository.get_all_to_dict())
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller

        self.notebook = ttk.Notebook(self, width=1180)

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

        ttk.Button(self, text="Gerar relatório", width=15, command=self.gerar_relatorio).place(x=950, y=10)
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
        colunas = ['id', 'nome']
        data = self.curso_repository.get_cursos()
        width = [300, 600]

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

        colunas = ['codigo', 'nome', 'nome_curso', 'ano', 'semestre']
        width = [150, 250, 250, 90, 80]

        data = self.disciplina_repository.get_disciplinas()

        self.tree_disciplina = Treeview(frame_tree, colunas, data, width)

        ttk.Label(frame_entrys, text="Nome: ").grid(row=0, column=0, sticky="W")
        self.nome_disciplina_entry = ttk.Entry(frame_entrys, width=20)
        self.nome_disciplina_entry.grid(row=1, column=0, pady=5)

        ttk.Label(frame_entrys, text="Código: ").grid(row=0, column=1, sticky="W")
        self.codigo_entry = ttk.Entry(frame_entrys, width=20)
        self.codigo_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame_entrys, text="Ano: ").grid(row=2, column=0, sticky="W")
        self.ano_entry = ttk.Entry(frame_entrys, width=20)
        self.ano_entry.grid(row=3, column=0, pady=5)

        ttk.Label(frame_entrys, text="Semetre: ").grid(row=2, column=1, sticky="W")
        self.semestre_entry = ttk.Entry(frame_entrys, width=20)
        self.semestre_entry.grid(row=3, column=1, pady=5)

        selected_key = tk.StringVar()


        ttk.Label(frame_entrys, text="Curso").grid(row=4, column=0, sticky="W")
        self.combobox_curso_disciplina = ttk.Combobox(frame_entrys, textvariable=selected_key,values=list(self.dict_cursos.values()),
                                     state="readonly")
        self.combobox_curso_disciplina.grid(row=5, column=0, pady=5, padx=10, sticky="nsew")



        ttk.Button(frame_entrys, text="Adicionar", command=self.adicionar_disciplina).grid(row=6, column=0, pady=10)
        ttk.Button(frame_entrys, text="Filtrar", command=self.filtrar_disciplina_curso).grid(row=6, column=1,pady=10)
        ttk.Button(frame_entrys, text="Editar", command=self.editar_disciplina).grid(row=7, column=0, pady=10)
        ttk.Button(frame_entrys, text="Excluir", command=self.exluir_disciplina).grid(row=7, column=1, pady=10)

        self.tree_disciplina.bind("<<TreeviewSelect>>", self.on_disciplina_select)


    def draw_inscricoes_frame(self):

        frame_entrys = ttk.Frame(self.inscricoes_frame, padding=10)
        frame_entrys.grid(row=0, column=0, sticky="NSW")

        frame_tree = ttk.Frame(self.inscricoes_frame, padding=10)
        frame_tree.grid(row=0, column=1, sticky="NSE")

        colunas = ['id', 'sim1', 'sim2', 'av', 'avs', 'nf', 'situacao', 'Nome Aluno', 'Disciplina']

        data = self.inscricao_repository.get_inscricoes()
        width = [20, 80, 80, 80, 80, 80, 130, 170, 200]

        self.tree_inscricao = Treeview(frame_tree, colunas, data, width)

        self.inscricoes_frame.grid_columnconfigure(0, weight=1)
        self.inscricoes_frame.grid_columnconfigure(1, weight=3)
        self.inscricoes_frame.grid_rowconfigure(0, weight=1)

        selected_key = tk.StringVar()
        selected_key2 = tk.StringVar()

        ttk.Label(frame_entrys, text="Curso").grid(row=0, column=0, sticky="W")
        self.combobox_curso_inscricao = ttk.Combobox(frame_entrys, textvariable=selected_key,
                                           values=list(self.dict_cursos.values()),
                                           state="readonly")
        self.combobox_curso_inscricao.grid(row=1, column=0, pady=5, padx=10)

        ttk.Label(frame_entrys, text="SIM1: ").grid(row=4, column=0, sticky="W")
        self.sim1_entry = ttk.Entry(frame_entrys, width=12)
        self.sim1_entry.grid(row=5, column=0, pady=5, padx=10, sticky="W")

        ttk.Label(frame_entrys, text="SIM2: ").grid(row=4, column=1, sticky="W")
        self.sim2_entry = ttk.Entry(frame_entrys, width=12)
        self.sim2_entry.grid(row=5, column=1, pady=5, sticky="W")

        ttk.Label(frame_entrys, text="AV: ").grid(row=6, column=0, sticky="W")
        self.av_entry = ttk.Entry(frame_entrys, width=12)
        self.av_entry.grid(row=7, column=0, pady=5, padx=10, sticky="W")

        ttk.Label(frame_entrys, text="AVS: ").grid(row=6, column=1, sticky="W")
        self.avs_entry = ttk.Entry(frame_entrys, width=12)
        self.avs_entry.grid(row=7, column=1, pady=5, sticky="W")

        ttk.Button(frame_entrys, text="Adicionar", command=self.adicionar_nota).grid(row=8, column=0, pady=10, sticky="W")
        ttk.Button(frame_entrys, text="Filtrar por curso", command=self.filtrar_inscricao_curso).grid(row=8, column=1, pady=10, sticky="W")


        ttk.Label(frame_entrys, text="Disciplina").grid(row=2, column=0, sticky="W")
        self.combobox_disciplina_inscricao = ttk.Combobox(frame_entrys, textvariable=selected_key2,
                                                          values=list(self.dict_disciplinas.values()),
                                                          state="readonly")
        self.combobox_disciplina_inscricao.grid(row=3, column=0, pady=5, padx=10)
        ttk.Button(frame_entrys, text="Filtrar por disciplina", command=self.filtrar_inscricao_disciplina).grid(row=9,
                                                                                                           column=0,
                                                                                                           pady=10,
                                                                                                           sticky="W")

        self.tree_inscricao.bind('<<TreeviewSelect>>', self.on_inscricao_select)


    def on_curso_select(self, event):
        selected_item = self.tree_curso.focus()
        if selected_item:
            values = self.tree_curso.item(selected_item, 'values')
            if values:
                self.name_curso_entry.delete(0, tk.END)
                self.name_curso_entry.insert(0, values[1])

    def on_disciplina_select(self, event):
        selected_item = self.tree_disciplina.focus()
        if selected_item:
            values = self.tree_disciplina.item(selected_item, 'values')
            if values:
                self.codigo_entry.delete(0, tk.END)
                self.nome_disciplina_entry.delete(0, tk.END)
                self.combobox_curso_disciplina.delete(0, tk.END)
                self.ano_entry.delete(0, tk.END)
                self.semestre_entry.delete(0, tk.END)
                self.codigo_entry.insert(0, values[0])
                self.nome_disciplina_entry.insert(0, values[1])
                self.combobox_curso_disciplina.insert(0, values[2])
                self.ano_entry.insert(0, values[3])
                self.semestre_entry.insert(0, values[4])

    def on_inscricao_select(self, event):
        selected_item = self.tree_inscricao.focus()

        if selected_item:
            value = self.tree_inscricao.item(selected_item, 'values')
            if value:
                self.sim1_entry.delete(0, tk.END)
                self.sim2_entry.delete(0, tk.END)
                self.av_entry.delete(0, tk.END)
                self.avs_entry.delete(0, tk.END)

                self.sim1_entry.insert(0, value[1])
                self.sim2_entry.insert(0, value[2])
                self.av_entry.insert(0, value[3])
                self.avs_entry.insert(0, value[4])

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

    def adicionar_disciplina(self):
        nome = self.nome_disciplina_entry.get()
        id_curso = int({v: k for k, v in self.dict_cursos.items()}.get(self.combobox_curso_disciplina.get()))
        codigo = self.codigo_entry.get()
        ano = self.ano_entry.get() or int(datetime.now().strftime("%Y"))
        semestre = self.semestre_entry.get() or 1 if int(datetime.now().strftime("%m")) <= 6 else 2

        if len(nome) > 7 and id_curso and len(codigo) > 3:
            self.disciplina_repository.adicionar_disciplina(Disciplina(codigo, nome, id_curso, ano, semestre))
            data = self.disciplina_repository.get_disciplinas()
            self.tree_disciplina.atualizar(data)
            self.atualizar()
            self.nome_disciplina_entry.delete(0, tk.END)
            self.combobox_curso_disciplina.delete(0, tk.END)
            self.codigo_entry.delete(0, tk.END)
            messagebox.showinfo("SUCESSO!", "Disciplina adicionada!")
            return
        messagebox.showerror("ERRO!", "Não foi possível adicionar a disciplina")

    def adicionar_nota(self):
        selected_item = self.tree_inscricao.focus()

        if selected_item:
            values = self.tree_inscricao.item(selected_item, 'values')

            sim1 = float(self.sim1_entry.get()) if self.sim1_entry.get() != "" else 0
            sim2 = float(self.sim2_entry.get()) if self.sim2_entry.get() != "" else 0
            av = float(self.av_entry.get()) if self.av_entry.get() != "" else 0
            avs = float(self.avs_entry.get()) if self.avs_entry.get() != "" else 0

            nota = Nota(sim1, sim2, av, avs)

            self.inscricao_repository.insert_nota(nota, values[0])
            data = self.inscricao_repository.get_inscricoes()
            self.tree_inscricao.atualizar(data)
            self.atualizar()

            self.sim1_entry.delete(0, tk.END)
            self.sim2_entry.delete(0, tk.END)
            self.av_entry.delete(0, tk.END)
            self.avs_entry.delete(0, tk.END)

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

    def editar_disciplina(self):
        selected_item = self.tree_disciplina.focus()

        if selected_item:
            values = self.tree_disciplina.item(selected_item, 'values')
            nome = self.nome_disciplina_entry.get()
            ano = self.ano_entry.get() or int(datetime.now().strftime("%Y"))
            semestre = self.semestre_entry.get() or 1 if int(datetime.now().strftime("%m")) <= 6 else 2
            self.disciplina_repository.editar(values[0], nome, ano, semestre)
            self.nome_disciplina_entry.delete(0, tk.END)
            data = self.disciplina_repository.get_disciplinas()
            self.tree_disciplina.atualizar(data)
            self.atualizar()
            messagebox.showinfo("SUCESSO!", "Disciplina editada!")
            return
        messagebox.showerror("ERRO!", "Não foi editar a disciplina")

    def exluir_disciplina(self):
        selected_item = self.tree_disciplina.focus()

        if selected_item:
            values = self.tree_disciplina.item(selected_item, 'values')
            self.disciplina_repository.remove(values[0])
            data = self.disciplina_repository.get_disciplinas()
            self.tree_disciplina.atualizar(data)
            self.atualizar()
            messagebox.showinfo("SUCESSO!", "Disciplina removida!")
            return
        messagebox.showerror("ERRO!", "Não foi possível remover a disciplina")

    def exluir_curso(self):
        selected_item = self.tree_curso.focus()
        if selected_item:
            values = self.tree_curso.item(selected_item, 'values')
            resposta = messagebox.askyesno("AVISO!", f"Curso você deseja realmente remover {values[1]}?")
            if resposta:
                self.curso_repository.remove(values[0])
                data = self.curso_repository.get_cursos()
                self.tree_curso.atualizar(data)
                self.dict_cursos = dict(self.curso_repository.get_cursos())
                self.atualizar()
                return
            else:
                return
        messagebox.showerror("ERRO!", "Não foi possível remover o curso")

    def atualizar(self):
        self.draw_disciplina_frame()
        self.draw_curso_frame()
        self.draw_inscricoes_frame()

    def filtrar_disciplina_curso(self):
        try:
            id_curso = int({v: k for k, v in self.dict_cursos.items()}.get(self.combobox_curso_disciplina.get()))

            if id_curso:
                data = self.disciplina_repository.get_disciplinas_by_curso(id_curso)
                self.atualizar()
                self.tree_disciplina.atualizar(data)
                return
        except Exception as e:
            data = self.disciplina_repository.get_disciplinas()
            self.atualizar()
            self.tree_disciplina.atualizar(data)

    def filtrar_inscricao_curso(self):
        try:
            id_curso = int({v: k for k, v in self.dict_cursos.items()}.get(self.combobox_curso_inscricao.get()))

            if id_curso:
                data = self.inscricao_repository.get_inscricoes_by_curso(id_curso)
                self.clicked_filter = True
                self.dict_disciplinas = self.adiciona_dados_combobox_disciplinas(id_curso)
                self.atualizar()
                self.tree_inscricao.atualizar(data)
                return
        except Exception as e:
            data = self.inscricao_repository.get_inscricoes()
            self.dict_disciplinas = dict(self.disciplina_repository.get_all_to_dict())
            self.atualizar()
            self.tree_inscricao.atualizar(data)

    def filtrar_inscricao_disciplina(self):
        try:
            codigo = {v: k for k, v in self.dict_disciplinas.items()}.get(self.combobox_disciplina_inscricao.get())

            if codigo:
                data = self.inscricao_repository.get_inscricoes_by_disciplina(codigo)
                self.atualizar()
                self.tree_inscricao.atualizar(data)
                return
        except Exception as e:
            data = self.inscricao_repository.get_inscricoes()
            self.dict_disciplinas = dict(self.disciplina_repository.get_all_to_dict())
            self.atualizar()
            self.tree_inscricao.atualizar(data)

    def adiciona_dados_combobox_disciplinas(self, id_curso):
        return dict(self.disciplina_repository.get_by_curso_id(id_curso))

    def deslogar(self):
       from Telas.TelaLogin import TelaLogin
       self.atualizar()
       self.controller.geometry("300x200")
       self.controller.mostrar_tela(TelaLogin)

    def gerar_relatorio(self):
        Path("Relatorios").mkdir(parents=True, exist_ok=True)

        with pd.ExcelWriter('Relatorios/dados_completos.xlsx', engine='openpyxl') as writer:
            conn = get_conn()
            pd.read_sql('SELECT * FROM aluno', conn).to_excel(writer, sheet_name='Alunos', index=False)
            pd.read_sql('SELECT * FROM curso', conn).to_excel(writer, sheet_name='Cursos', index=False)
            pd.read_sql('SELECT * FROM disciplina', conn).to_excel(writer, sheet_name='Disciplinas', index=False)
            pd.read_sql('SELECT * FROM inscricao', conn).to_excel(writer, sheet_name='Inscrições', index=False)