import tkinter as tk

window = tk.Tk()
window.minsize(width=500,height=500)
window.title("Mile to Km Converter")

def calculate():
    a = int(text.get())
    km = a*1.6
    km_ans.config(text=round(km))



calculate_button = tk.Button(text="Calculate",command= calculate)
calculate_button.grid(column=2, row=2)

label = tk.Label(text="is equal to")
label.grid(column=0, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=3, row=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=0)

text = tk.Entry()
text.grid(column=2, row=0)
text.focus()

km_ans = tk.Label(text="0")
km_ans.grid(column=2, row=1)





window.mainloop()

