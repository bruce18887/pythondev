from  tkintertable import *
#print(data)

class TestApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('800x500+200+100')
        self.main.title('Test')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        table = TableCanvas(f)
        # table.importCSV('test.csv')

        table.show()
        table.load('test.table')
        return

app=TestApp()
app.mainloop()
