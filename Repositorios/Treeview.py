from tkinter import ttk

class Treeview(ttk.Treeview):
    def __init__(self, parent, colunas, data, width, row=0):
        super().__init__(parent, columns=colunas, show="headings")

        for col, w in zip(colunas, width):
            self.heading(col, text=col)
            self.column(col, width=w)

        self.grid(column=0, row=row, sticky="nsew")

        self.tag_configure('oddrow', background="white")
        self.tag_configure('evenrow', background="lightblue")

        self.preencher(data)

    def preencher(self, data):
        count = 0
        for i in data:
            if count % 2 == 0:
                self.insert(parent='', index='end', iid=count, text='',
                            values=self.validar_dado(data[count]) or '',
                            tags=('evenrow',))
            else:
                self.insert(parent='', index='end', iid=count, text='',
                            values=self.validar_dado(data[count]) or '',
                            tags=('oddrow',))
            count += 1

    def validar_dado(self, values):
        return [val if val is not None else "" for val in values]
    
    def atualizar(self, data):
        for item in self.get_children():
            self.delete(item)

        self.preencher(data)