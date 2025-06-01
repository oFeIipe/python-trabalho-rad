import tkinter as tk
from tkinter import ttk, messagebox

from Models.Aluno import gerar_hesh
from Models.Inscricao import Inscricao
from Repositorios.AlunoRepository import AlunoRepository
from Repositorios.CursoRepository import CursoRepository
from Repositorios.DisciplinaRepository import DisciplinaRepository
from Repositorios.InscricaoRepository import InscricaoRepository
from Repositorios.Treeview import Treeview


class TelaAluno(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()
        self.inscricao_repository = InscricaoRepository()
        self.disciplina_repository = DisciplinaRepository()

        self.dict_cursos = dict(self.curso_repository.get_cursos())

        self.controller = controller

        self.notebook = ttk.Notebook(self, width=770)
        self.notebook.grid(column=0, row=1, pady=30)

        self.notas_frame = ttk.Frame(self.notebook)
        self.disciplinas_frame = ttk.Frame(self.notebook)
        self.aluno_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.notas_frame, text="Notas")
        self.notebook.add(self.disciplinas_frame, text="Disciplinas")
        self.notebook.add(self.aluno_frame, text="Aluno")

        self.label_bem_vindo = ttk.Label(self, text="", font=("Arial", 16, "bold"))
        self.label_bem_vindo.grid(row=0, column=0, pady=10, padx=10)

        self.botao_sair = ttk.Button(self, text="Sair", width=5, command=self.deslogar)
        self.botao_sair.place(x=680, y=10)

        self.clicked_bool = False
    def atualiza_dados(self):
        self.grid_columnconfigure(1, weight=1)

        self.matricula = self.controller.dados_compartilhados["matricula"].get()
        self.aluno = self.aluno_repository.get_aluno_by_matricula(self.matricula)

        self.label_bem_vindo.config(text=f"Bem vindo {self.aluno[0][1]}!")

        self.draw_disciplinas_frame()
        self.draw_notas_frame()
        self.draw_aluno_frame()

    def draw_notas_frame(self):
        frame_label = ttk.Frame(self.notas_frame, padding=10)
        frame_label.grid(row=0, column=0, sticky='nsew')

        frame_tree = ttk.Frame(self.notas_frame, padding=10)
        frame_tree.grid(row=1, column=0, sticky='nsew')

        self.notas_frame.grid_rowconfigure(0, weight=1)
        self.notas_frame.grid_rowconfigure(1, weight=2)
        self.notas_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(frame_label, text="Suas Notas", font=("Arial", 12, "bold")).grid(row=0, column=0,
                                                                            pady=10,
                                                                            padx=10, sticky="nsew")
        colunas = ['Nome Disciplina', 'sim1', 'sim2', 'av', 'avs', 'nf', 'Situação']
        data = self.inscricao_repository.get_inscricoes_by_aluno(self.matricula)
        width = [250, 80, 80, 80, 80, 80, 100]

        if len(data) > 0:
            self.tree_notas = Treeview(frame_tree, colunas, data, width, row=1)
            ttk.Button(frame_label, text="Cancelar inscricao", command=self.cancelar_inscricao).grid(row=0, column=1,
                                                                                                     padx=520,
                                                                                                     sticky="nsew")
        else:
            ttk.Label(frame_tree, text="Você não está matriculado em nenhuma disciplina",
                      font=("Arial", 12, "bold")).grid(row=1, column=0, pady=10, padx=10, sticky="nsew")


    def draw_disciplinas_frame(self):

        frame_label = ttk.Frame(self.disciplinas_frame, padding=10)
        frame_label.grid(row=0, column=0, sticky='nsew')

        frame_tree = ttk.Frame(self.disciplinas_frame, padding=10)
        frame_tree.grid(row=1, column=0, sticky='nsew')

        self.disciplinas_frame.grid_rowconfigure(0, weight=1)
        self.disciplinas_frame.grid_rowconfigure(1, weight=2)
        self.disciplinas_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(frame_label, text="Disciplinas", font=("Arial", 12, "bold")).grid(row=0, column=0,
                                                                                   pady=10,
                                                                                   padx=10, sticky="nsew")


        colunas = ['Código', 'Nome', 'Ano', 'Semestre']
        data = self.disciplina_repository.get_disciplinas_by_aluno(self.matricula)
        width = [160, 300, 145, 145]

        if len(data) > 0:
            self.tree_disciplina = Treeview(frame_tree, colunas, data, width, row=1)
            ttk.Button(frame_label, text="Matricular-se", command=self.matricular_disciplina).grid(row=0, column=1,
                                                                                                   padx=550)
        else:
            ttk.Label(frame_tree, text="Você não possui disciplinas disponíveis", font=("Arial", 12, "bold")).grid(row=1, column=0,
                                                                                                       pady=10,
                                                                                                       padx=10,
                                                                                                       sticky="nsew")

    def draw_aluno_frame(self):
        frame_label = ttk.Frame(self.aluno_frame, padding=10)
        frame_label.grid(row=0, column=0, sticky='nsew')

        frame_entrys = ttk.Frame(self.aluno_frame, padding=10)
        frame_entrys.grid(row=1, column=0, sticky='nsew')

        self.aluno_frame.grid_rowconfigure(0, weight=1)
        self.aluno_frame.grid_rowconfigure(1, weight=2)
        self.aluno_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(frame_label, text="Área do aluno", font=("Arial", 12, "bold")).grid(row=0, column=0,
                                                                                    pady=10,
                                                                                    padx=10, sticky="nsew")

        ttk.Label(frame_entrys, text="Matricula: ").grid(row=0, column=0, sticky="NW", padx=10)
        self.matricula_entry = ttk.Entry(frame_entrys)
        self.matricula_entry.insert(0, self.matricula)
        self.matricula_entry.grid(row=1, column=0, padx=10)
        self.matricula_entry.config(state='readonly')

        ttk.Label(frame_entrys, text="Nome: ").grid(row=0, column=1, sticky="NW", padx=10)
        self.nome_aluno_entry = ttk.Entry(frame_entrys)
        self.nome_aluno_entry.grid(row=1, column=1, padx=10)
        self.nome_aluno_entry.insert(0, self.aluno[0][1])
        self.nome_aluno_entry.config(state='disabled')



        ttk.Button(frame_entrys, text="Habilitar Edição", command=self.clicked).grid(row=2, column=0, pady=30, sticky="NW")
        ttk.Button(frame_entrys, text="Cancelar matrícula", command=self.cancelar_matricula).grid(row=2, column=1, pady=30, sticky="NW")

        if self.clicked_bool:
            ttk.Button(frame_entrys, text="Editar dados", command=self.editar_dados).grid(row=2, column=2,
                                                                                                      pady=30,
                                                                                                      sticky="NW")
            self.nome_aluno_entry.config(state="enabled")
            ttk.Label(frame_entrys, text="Senha atual: ").grid(row=0, column=2, sticky="NW", padx=10)
            self.senha_entry = ttk.Entry(frame_entrys, show="*")
            self.senha_entry.grid(row=1, column=2, padx=10)


            ttk.Label(frame_entrys, text="Nova senha: ").grid(row=0, column=3, sticky="NW", padx=10)
            self.nova_senha = ttk.Entry(frame_entrys, show="*")
            self.nova_senha.grid(row=1, column=3, padx=10)


    def clicked(self):
        self.clicked_bool = not self.clicked_bool
        self.draw_aluno_frame()

    def cancelar_matricula(self):
        resposta = messagebox.askyesno("ATENÇÃO", "Deseja mesmo cancelar sua matrícula?")
        if resposta:
            self.aluno_repository.delete_aluno(self.matricula)
            self.deslogar()

    def cancelar_inscricao(self):
        selected_item = self.tree_notas.focus()

        if selected_item:
            values = self.tree_notas.item(selected_item, 'values')
            resposta = messagebox.askyesno("ATENÇÃO", f"Deseja mesmo cancelar sua inscrição na disciplina {values[0].upper()}?")
            if resposta:
                codigo = self.disciplina_repository.get_disciplina_by_name(values[0])
                self.inscricao_repository.cancela_inscricao(self.matricula, codigo[0][0])
                self.atualizar()


    def editar_dados(self):
        try:
            senha = self.senha_entry.get()
            nova_senha = self.nova_senha.get()
            nome = self.nome_aluno_entry.get()

            if not senha or not nova_senha:
                self.aluno_repository.update_nome(nome, self.matricula)
                messagebox.showinfo("SUCESSO", "Nome atualizado com sucesso")
                self.clicked_bool = False
                self.atualiza_dados()
                return

            if self.verifica_senha(senha):
                self.aluno_repository.update_aluno(nome, self.matricula, gerar_hesh(nova_senha))
                messagebox.showinfo("SUCESSO", "Senha atualizada com sucesso")
                messagebox.showinfo("info", "Redireciondando para a tela de Login")
                self.deslogar()
                self.clicked_bool = False
            else:
                messagebox.showerror("ERRO", "Senha atual não corresponde")

        except Exception:
            messagebox.showerror("ERRO", "Não foi possível editar seus dados")

    def matricular_disciplina(self):
        selected_item = self.tree_disciplina.focus()

        if selected_item:
            values = self.tree_disciplina.item(selected_item, 'values')
            resposta = messagebox.askyesno("Atenção", f"Você deseja se matricular na disciplina {values[1].upper()}?")

            if not resposta:
                return
            self.inscricao_repository.insert_inscricao(Inscricao(self.matricula, values[0]))
            self.atualizar()
            messagebox.showinfo("SUCESSO", "Matricula feita com sucesso!")
        else:
            messagebox.showinfo("Aviso", 'Selecione uma disciplina')

    def verifica_senha(self, senha):
        senha_hash = gerar_hesh(senha)
        senha_aluno = self.aluno[0][3]

        return senha_hash == senha_aluno

    def atualizar(self):
        self.draw_aluno_frame()
        self.draw_notas_frame()
        self.draw_disciplinas_frame()

    def deslogar(self):
        from Telas.TelaLogin import TelaLogin
        self.controller.geometry("300x200")
        self.controller.mostrar_tela(TelaLogin)