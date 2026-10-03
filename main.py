import calculator
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
window = tk.Tk()       # Hauptfenster erzeugen
window.title("Calculator") # Fenstertitel
window.geometry("400x700")
window.resizable(False,False)

style = ttk.Style(window)
style.theme_use("clam")

font = tkfont.Font(family="Helvetica", size=12)
window.option_add("*Font", font)


eingabe = ttk.Entry(window)
eingabe.grid(row = 0, column=0, columnspan=5, padx=10, pady=10, sticky="we")
output_label = ttk.Label(window, text="Ausgabe erscheint hier")
output_label.grid(row=1, column=0, columnspan=5, padx=10, pady=5)

was_calculated=False

def enter(input):
    global was_calculated
    if was_calculated == True:
        eingabe.delete(0, tk.END)
        output_label.config(text="")
        was_calculated = False
    eingabe.insert(tk.END, input)
def clear():
    eingabe.delete(0, tk.END)
    output_label.config(text="")
def compute():
    global was_calculated
    input = eingabe.get()
    input=input.replace("﹣", "~")
    output = calculator.calculator(input)
    output_label.config(text=output)
    was_calculated = True


# Spalten gleichmäßig mitwachsen lassen
for col in range(4):
    window.grid_columnconfigure(col, weight=1)

#alle buttons hinzufügen
btn_open_br = ttk.Button(window, text="(", command=lambda: enter("("))
btn_open_br.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

btn_close_br = ttk.Button(window, text=")", command=lambda: enter(")"))
btn_close_br.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

btn_clear = ttk.Button(window, text="C", command=clear)
btn_clear.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

btn_pl = ttk.Button(window, text="+", command=lambda: enter("+"))
btn_pl.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

# Reihe 2
btn_one = ttk.Button(window, text="1", command=lambda: enter("1"))
btn_one.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

btn_two = ttk.Button(window, text="2", command=lambda: enter("2"))
btn_two.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

btn_three = ttk.Button(window, text="3", command=lambda: enter("3"))
btn_three.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

btn_min = ttk.Button(window, text="-", command=lambda: enter("-"))
btn_min.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

# Reihe 3
btn_four = ttk.Button(window, text="4", command=lambda: enter("4"))
btn_four.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

btn_five = ttk.Button(window, text="5", command=lambda: enter("5"))
btn_five.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

btn_six = ttk.Button(window, text="6", command=lambda: enter("6"))
btn_six.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

btn_mul = ttk.Button(window, text="*", command=lambda: enter("*"))
btn_mul.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

# Reihe 4
btn_seven = ttk.Button(window, text="7", command=lambda: enter("7"))
btn_seven.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

btn_eight = ttk.Button(window, text="8", command=lambda: enter("8"))
btn_eight.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

btn_nine = ttk.Button(window, text="9", command=lambda: enter("9"))
btn_nine.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

btn_div = ttk.Button(window, text="/", command=lambda: enter("/"))
btn_div.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

# Reihe 5
btn_neg = ttk.Button(window, text="﹣", command=lambda: enter("﹣"))
btn_neg.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

btn_zero = ttk.Button(window, text="0", command=lambda: enter("0"))
btn_zero.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

btn_dot = ttk.Button(window, text=".", command=lambda: enter("."))
btn_dot.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

btn_equals = ttk.Button(window, text="=", command=compute)
btn_equals.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

for r in range(1, 7):  # Zeilen 1 bis 5
    window.grid_rowconfigure(r, weight=1)

window.mainloop()      # GUI starten