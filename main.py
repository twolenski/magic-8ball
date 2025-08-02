import random, tkinter as tk

responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

window = tk.Tk()
window.title("Trist's Magic 8-Ball!")
window.geometry("300x200")
window.resizable(False, False)
window.configure(bg="black")

title_label = tk.Label(window, 
                       text="This is Trist's Magic 8-Ball!", 
                       font=("Arial",16), 
                       fg="White",
                       bg="black",
                       width=35, 
                       height=0)

answer_label = tk.Label(window, 
                        text="",
                        font=("Arial",12),
                        fg="White",
                        bg="black",
                        width=35, 
                        height=4)

def on_click():
    chosen_number = random.randint(0,19)
    answer_label.config(text=responses[chosen_number])

my_button = tk.Button(window, 
                      text="Shake", 
                      command=on_click,
                      font=("Arial",12),
                      fg="White",
                      bg="black",
                      width=35, 
                      height=2)

title_label.pack()
answer_label.pack()
my_button.pack(pady=25)
window.mainloop()


