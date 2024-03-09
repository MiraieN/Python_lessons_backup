import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login window")

window_width = 240
window_height = 100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-alpha', 0.8)
# root.attributes('-topmost', 1)    # stay at top
root.iconbitmap('2.ico')


def f(text):
    global globaltxt
    # labelName['text'] += "a"
    globaltxt += text
    loginInput.set(globaltxt)


globaltxt = ""
loginInput = tk.StringVar()
passInput = tk.StringVar()

labelName = tk.Label(text="Username:")
labelPass = tk.Label(text="Password:")
loginEntry = tk.Entry(textvariable=loginInput, width=25)
passEntry = tk.Entry(textvariable=passInput, width=25)
sendButton = tk.Button(text="Login", width=8, command=lambda: f("a"))

labelName.grid(row=0, column=0, padx=10, pady=6, sticky="w")
loginEntry.grid(row=0, column=1, sticky="E")
labelPass.grid(row=1, column=0, padx=10, pady=6)
passEntry.grid(row=1, column=1, sticky="E")
sendButton.grid(row=2, column=1, sticky="E")


root.mainloop()
