from tkinter import *
import random
number = (random.randint(1, 100))
window = Tk()
window.title("Number Guessing Game")
window.geometry("500x250")

guess_count = 0
def check():
    guessed_number = entry.get()
    global guess_count
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
        guess_count += 1
        guessed_number= int(guessed_number)
        if guessed_number < number:
            result.config(text=f"{guessed_number} is Too low!", fg='#ff6f61')
        elif guessed_number > number:
            result.config(text=f"{guessed_number} is Too high!", fg='#ff6f61')
        else:
            if guess_count < 3:
                feedback = "You are too good! 🎯"
            elif guess_count < 6:
                feedback = "You are good! 👍"
            else:
                feedback = "Nice try! 😊"

            result.config(text=f"Correct! 🎉 You guessed it in {guess_count} tries.\n{feedback}",fg='#ff6f61')
    else:
        result.config(text="Please enter a number",fg='#ff6f61')
    entry.delete(0, END)

def retry():
    global number, guess_count
    number = random.randint(1, 100)
    guess_count = 0
    result.config(text="", fg='#2cd4d9')
    entry.delete(0, END) 

title = Label(window, text="Guess a number (1-100)", font=("Segoe UI", 20,"bold"))
title.pack(pady=10)

entry = Entry(window,)
entry.pack()

button = Button(window, text="Check", command=check)
button.pack(pady=10)

retry_button = Button(window, text="Retry", command=retry, bg='#0ef6cc', fg='#1e1e2f', activebackground='#2cd4d9')
retry_button.pack()

result = Label(window, text="")
result.pack()

window.configure(bg='#1e1e2f')
title.config(bg='#1e1e2f', fg='#f5f5f5')
entry.config(bg='#2a2a3d', fg='#f5f5f5')
button.config(bg='#0ef6cc', fg='#1e1e2f', activebackground='#2cd4d9')
result.config(bg='#1e1e2f', fg='#2cd4d9')

window.mainloop()