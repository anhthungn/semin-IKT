import tkinter as tk

def update_display(value):
    # Update the display with the pressed button's value
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

def clear_display():
    # Clear the display
    display.delete(0, tk.END)

def calculate():
    # Evaluate the expression in the display and show the result
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Display for the calculator
display = tk.Entry(root, width=30, font=("Arial", 16), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), command=calculate)
        btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=5, pady=5)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), command=clear_display)
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), command=lambda t=text: update_display(t))
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure grid to make buttons expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()