from tkinter import ttk, Tk

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela Login")
        self.geometry("300x200")
        self.criar_widgets()

    def criar_widgets(self):
        self.text_label = ttk.Label(text="Faça login ou matricula-se", font=("Arial", 16, "bold"))
        self.text_label.grid(row=0, column=0, columnspan=3)
        self.login_label = ttk.Label(text="Matrícula:")
        self.login_label.grid(row=1, column=0, columnspan=1)
        self.login_input = ttk.Entry()
        self.login_input.grid(row=1, column=1, columnspan=2)


if __name__ == "__main__":
    tela = Login()
    tela.mainloop()