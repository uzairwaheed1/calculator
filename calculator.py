import tkinter as tk

def click(button):
    current = display.get()
    if button == "C":
        display.delete(0, tk.END)
    elif button == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, button)

root = tk.Tk()
root.title("Calculator")

buttons = [
    '7', '8', '9', '+', 'C',
    '4', '5', '6', '-', ' ',
    '1', '2', '3', '*', ' ',
    '0', '.', '=', '/', ' '
]

# create a text entry to show the user input and results
display = tk.Entry(root, font=("Helvetica", 16), borderwidth=1, relief=tk.RAISED, justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=5)

# create buttons using the 'buttons' list
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: click(x)
    tk.Button(root, text=button, height=3, width=6, font=("Helvetica", 16), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.mainloop()
