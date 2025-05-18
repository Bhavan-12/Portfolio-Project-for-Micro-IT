from tkinter import *

def press(key):
    entry.insert(END, key)

def clear():
    entry.delete(0, END)

def calculate():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(END, str(result))

window = Tk()
window.geometry("270x350")
window.title("Calculator")
window.resizable(False, False)

entry = Entry(window, relief=GROOVE, font=("Arial", 20), justify="right")
entry.pack(fill=BOTH, padx=10, pady=10, ipady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

for values in buttons:
    frame = Frame(window,bg="white")
    frame.pack(expand=True, fill=BOTH)
    for value in values:
        if value == '=':
            btn = Button(frame, text=value, font=("Arial", 16), command=calculate,bg="#17fc03")
        else:
            btn = Button(frame, text=value, font=("Arial", 16), command=lambda v=value: press(v),bg="black",fg="white")
        btn.pack(side=LEFT, expand=True, fill=BOTH, padx=2, pady=2)

clear_btn = Button(window, text="Clear", font=("Arial", 16), bg="red", fg="white", command=clear)
clear_btn.pack(fill=BOTH, padx=10, pady=(5, 10))

window.mainloop()
