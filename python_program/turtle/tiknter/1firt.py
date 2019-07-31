import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title(" python gui use by sk")



#win.resizable(0,0)
win.mainloop()
def clickMe():
    action.configure(text="** click me")
    aLabel.configure(foreground="red")

action = ttk.Button(win,text = "click me",command =ClickMe)    

tkk.Label(win,text = "A Label").grid(column =0, row=0)
