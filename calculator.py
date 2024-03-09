# calculator with button blinks
from tkinter import *

root = Tk()

# root.title("Paint")
# root.geometry("410x500+450+150")


window_width = 410
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
# root.attributes('-alpha', 0.8)
root.attributes('-topmost', 1)  # stay at top

root['bg'] = 'snow'
root.resizable(False, False)

var = StringVar()
global_txt = ""


def var_add_text(txt):
    if txt == "=":
        equals()
        return None
    if txt == "C":
        clear()
        return None
    if var.get() == "Error":
        var.set("")
    global global_txt
    print(txt, global_txt)
    if txt in "+-*/" and global_txt[-1] in "+-*/":
        return
    global_txt += txt
    var.set(global_txt)


def blink_in(txt):
    global buts
    buts[txt]['bg'] = "red"


def blink_out(event):
    global buts
    for k, v in buts.items():
        if buts[k]['bg'] == "red":
            buts[k]['bg'] = 'snow'


def val():
    def button(txt, row, col):
        global buts
        buts[txt] = Button(text=txt, command=lambda: var_add_text(txt), bg="snow")
        buts[txt].grid(row=row, column=col, ipadx=30, ipady=30, padx=10, pady=5)
        buts[txt].bind('<Motion>', lambda x: blink_in(txt))

    values = ("9", "8", "7", "+", "6", "5", "4", "*", "3", "2", "1", "-", "0", "/", "=", "C")
    row = 1
    col = 0
    for i in values:
        button(i, row, col)
        if col == 3:
            row += 1
            col = 0
        else:
            col += 1


def equals():
    global global_txt
    try:
        expression = eval(global_txt)
        var.set(expression)
    except (SyntaxError, ZeroDivisionError):
        global_txt = ""
        var.set("Error")


def clear():
    global global_txt
    global_txt = ""
    var.set(global_txt)


lbl_out = Label()
lbl_out.place(x=0, y=0, width=window_width, height=window_height)
lbl_out.bind("<Motion>", blink_out)

buts = {}
val()

lbl_1 = Entry(textvariable=var, font=("Roboto", 15, "bold"), fg="black")
lbl_1.grid(row=0, column=0, columnspan=6, ipady=35, ipadx=80)


mainloop()