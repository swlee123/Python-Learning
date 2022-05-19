import tkinter

# layout manager place() grid() and pack()
# cannot mix grid and pack

def button_click():
    my_label.config(text=input.get())


# some basic labels, buttons, entries
window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.grid(column = 0,row = 0)
my_label.config(padx=20,pady=20)
# pad 好像是空间这样
# precise

# config a particular label
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Buttons

my_button = tkinter.Button(text="Click Me", command = button_click)
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command = button_click)
new_button.grid(column=2, row=0)
# Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=3)


window.mainloop()