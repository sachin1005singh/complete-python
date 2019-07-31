import tkinter

class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "hello world \n(click me)"
        self.hiu_there["command"] = self.say_hi

        self.quit = tk.button(self, text = "QUIT", fd = "red", command = root.destroy)
        self.quit.pack(side = "bottom")
    def say_hi(self):
        print("hi there , everyone!")

root = tk.Tk()
app = Application(master = root)
app.mainloop()
