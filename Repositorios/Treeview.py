from tkinter import ttk, Scrollbar, RIGHT, Y


class Treeview(ttk.Treeview):
    def __init__(self, parent, colunas, data, width):
        super().__init__(parent, columns=colunas, show="headings")

        for col in colunas:
            self.heading(col, text=col)
            self.column(col, width=width)

        self.pack(expand=True, fill="both")

        self.tag_configure('oddrow', background="white")
        self.tag_configure('evenrow', background="lightblue")
        count = 0

        for i in data:
            if count % 2 == 0:
                self.insert(parent='', index='end', iid=count, text='',
                               values=data[count] or '',
                               tags=('evenrow',))
            else:
                self.insert(parent='', index='end', iid=count, text='',
                               values=data[count] or '',
                               tags=('oddrow',))
            count += 1

    def atualizar(self, data):
        for item in self.get_children():
            self.delete(item)
        for d in data:
            self.insert("", "end", values=(d[0], d[1]))