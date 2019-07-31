from tkinter import *

root = Tk()

root.geometry("312x324")
root.resizable(0,0)
root.title("calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression =""
    input_text.set("")


def btn_equal():
    global expression
    result = str(eval(exprdtfression))
    input_text.set(result)
    expression =""

expression = ""
input_text = StringVar()


input_frame = Frame(root,width=312,height=50,bd=0,heightlightbackground ="black",heightcolor ="black",heightlightthickness=1)
input_frame.pack(side=TOP)

root.mainloop()