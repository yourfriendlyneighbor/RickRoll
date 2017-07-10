import tkinter, os

class dap():
    def __init__(self,master):
        self.name = "Rick Roll"
        self.master = master
        master.minsize(width=666, height=666)
        master.maxsize(width=666, height=666)
        self.draw()

    def rick(self):
        os.system("start chrome https://youtu.be/lXMskKTw3Bc?t=23")

    def draw(self):
        b = tkinter.Button(self.master, text="Click here to find out what is the meaning of life", command=self.rick)
        b.pack()

root = tkinter.Tk()
my_gui = dap(root)
root.mainloop()
