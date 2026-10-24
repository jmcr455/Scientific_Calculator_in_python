import tkinter as tk
from Scientific_calculator import calculator  

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("360x560")
window.resizable(False, False)

# Entry box (Display)
entry_box = tk.Entry(window, font=("Arial", 20), justify="right", bd=5, relief=tk.SUNKEN)
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10, sticky="we")

# Function to add text when clicking buttons
def button_click(value):
    current = entry_box.get()
    entry_box.delete(0, tk.END)
    entry_box.insert(0, current + str(value))

# Function to clear the display
def button_clear():
    entry_box.delete(0, tk.END)

# Function to remove the last character (Backspace)
def button_backspace():
    current = entry_box.get()
    if current:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, current[:-1])

# Calculation function when pressing "="
def button_equal_action():
    expression = entry_box.get()
    if not expression.strip():
        return
    
    resultado = calculator(expression)
    
    entry_box.delete(0, tk.END)
    entry_box.insert(0, str(resultado))

# Configuration and creation of buttons
buttons = [
    ('C', 1, 0), ('⌫', 1, 1), ('(', 1, 2), (')', 1, 3),
    ('√', 2, 0), ('^', 2, 1), ('/', 2, 2), ('*', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('+', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('=', 5, 3),
    ('0', 6, 0), ('.', 6, 1)
]

# Rendering the buttons dynamically
for item in buttons:
    text, row, col = item
    
    if text == '=':
        btn = tk.Button(window, text=text, font=("Arial", 14), bg="#4CAF50", fg="white", 
                        command=button_equal_action)
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew", ipadx=10, ipady=15, padx=3, pady=3)
        continue
    elif text == 'C':
        btn = tk.Button(window, text=text, font=("Arial", 14), bg="#f44336", fg="white", 
                        command=button_clear)
    elif text == '⌫':
        btn = tk.Button(window, text=text, font=("Arial", 14), bg="#ff9800", fg="white", 
                        command=button_backspace)
    else:
        btn = tk.Button(window, text=text, font=("Arial", 14), bg="#f0f0f0", 
                        command=lambda t=text: button_click(t))
    
    btn.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=15, padx=3, pady=3)

# Configuring proportional resizing for rows and columns
for i in range(7):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()