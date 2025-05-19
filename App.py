import tkinter as tk

from Telas.TelaCadastro import TelaCadastro
from Telas.TelaLogin import TelaLogin

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Notas - Login")
        self.geometry("300x200")

        self.dados_compartilhados = {
            "matricula": tk.StringVar()
        }

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for Tela in (TelaLogin,TelaCadastro):
            frame = Tela(parent=container, controller=self)
            self.frames[Tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(TelaLogin)

    def mostrar_tela(self, tela):
        frame = self.frames[tela]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()