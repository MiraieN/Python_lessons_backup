from tkinter import *
from tkinter import ttk

root = Tk()
window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-alpha', 0.8)
root.attributes('-topmost', 1)  # stay at top
# root.iconbitmap('2.ico')
root.title("Calculator")

expression = ""


def out_add(text):
    global expression
    expression += text
    label_out.config(text=expression)


def process():
    global expression
    label_out.config(text=eval(expression))
    expression = ""


if __name__ == '__main__':

    label_out = Label(text="", font=("Calibri", 16, "bold"))

    # button_1 = tk.Button(text="1", font=("Calibri", 16, "bold"), command=lambda: out_add("1"))
    # button_2 = tk.Button(text="2", font=("Calibri", 16, "bold"), command=lambda: out_add("2"))
    # button_3 = tk.Button(text="3", font=("Calibri", 16, "bold"), command=lambda: out_add("3"))
    # button_4 = tk.Button(text="4", font=("Calibri", 16, "bold"), command=lambda: out_add("4"))
    # button_5 = tk.Button(text="5", font=("Calibri", 16, "bold"), command=lambda: out_add("5"))
    # button_6 = tk.Button(text="3", font=("Calibri", 16, "bold"), command=lambda: out_add("3"))
    # button_7 = tk.Button(text="3", font=("Calibri", 16, "bold"), command=lambda: out_add("3"))
    # button_8 = tk.Button(text="3", font=("Calibri", 16, "bold"), command=lambda: out_add("3"))
    # button_9 = tk.Button(text="3", font=("Calibri", 16, "bold"), command=lambda: out_add("3"))

    labelframe = LabelFrame(root)
    canvas = Canvas(labelframe)
    canvas.grid()

    labelframe.grid()

    s = ttk.Style()
    s.configure('my.TButton', font=("Calibri", 14, "bold"))

    label_out.grid(row=0, column=1, pady=200)


    def createButton(c):
        ttk.Button(canvas, text=str(c), style="my.TButton",
                   command=lambda: out_add(str(c))).grid(row=roww, column=columnn, pady=2, ipadx=1, ipady=15)


    # Create Button widget in Canvas
    c = 1
    for roww in range(1, 4):
        for columnn in range(1, 4):
            createButton(c)
            c += 1

    calculate = Button(text="=", command=process)
    calculate.grid()

root.mainloop()
