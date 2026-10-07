import tkinter as tk
from Scientific_calculator import calculator  

window = tk.Tk()
window.title("Calculator")
window.geometry("900x500")

entry_box = tk.Entry(window, font=("Arial", 18), width=30)
entry_box.pack(pady=20)

def button_equal_action():
    expression = entry_box.get()
    
    resultado = calculator(expression)
    
    entry_box.delete(0, tk.END)
    entry_box.insert(0, str(resultado))

equal = tk.Button(window, text="=", command=button_equal_action)

equal.pack(side=tk.LEFT)

window.mainloop()