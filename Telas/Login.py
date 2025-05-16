from tkinter import ttk, Tk, Entry

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela Login")
        self.geometry("400x250")
        self.criar_widgets()

    def criar_widgets(self):
        self.login_input = Entry()
        self.login_input.pack()

if __name__ == "__main__":
    tela = Login()
    tela.mainloop()