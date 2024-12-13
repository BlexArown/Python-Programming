import tkinter as tk
from tkinter import messagebox

points = {
    "A": 1,
    "E": 1,
    "I": 1,
    "L": 1,
    "N": 1,
    "O": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10
}

def count_points():
    user_input = word_entry.get()

    result = 0
    for letter in user_input.upper():
        if letter in points.keys():
            result += points[letter]
        else:
            output["text"] = ""
            word_entry.delete(0, tk.END)
            messagebox.showerror("Ошибка", "В вашем слове неверный символ.")
            break
    else:
        output["text"] = str(result)

window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Эрудит")

frame = tk.Frame(master=window)
frame.rowconfigure([0,1,2,3,4], minsize=15)
frame.columnconfigure([0,1,2], minsize=10)
frame.pack(padx=10, pady=10)

word_label = tk.Label(master=frame, text="Введите своё слово на eng language:")
word_label.grid(row=0, column=0, sticky="w")
word_entry = tk.Entry(master=frame)
word_entry.grid(row=0, column=2, sticky="we")

button = tk.Button(master=frame, text="Проверить", bg="green", fg="white", command=count_points)
button.grid(row=2, column=0, columnspan=3, sticky="ew")

output_label = tk.Label(master=frame, text="Результат:")
output_label.grid(row=4, column=0, sticky="w")
output = tk.Label(master=frame, relief="sunken", borderwidth=1)
output.grid(row=4, column=2, sticky="we")



window.mainloop()   
