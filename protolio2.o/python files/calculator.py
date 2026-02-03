import tkinter as tk
import math

# ---------- Functions ----------
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        expr = expr.replace("^", "**")
        result = eval(expr, {
            "__builtins__": None,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        })
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

# ---------- Window ----------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("360x500")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.X, padx=10, pady=10)

# ---------- Buttons ----------
buttons = [
    "7","8","9","/","sqrt",
    "4","5","6","*","^",
    "1","2","3","-","log",
    "0",".","=","+","ln",
    "sin","cos","tan","pi","C"
]

frame = tk.Frame(root)
frame.pack()

row = col = 0
for btn in buttons:
    action = (
        calculate if btn == "=" else
        clear if btn == "C" else
        lambda b=btn: click(b)
    )

    tk.Button(
        frame, text=btn, width=6, height=2,
        font=("Arial", 12), command=action
    ).grid(row=row, column=col, padx=4, pady=4)

    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()
