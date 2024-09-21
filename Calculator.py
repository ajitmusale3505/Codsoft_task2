# calculator

import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="black")  # Set the background color to black

# Create a StringVar to hold the text entered in the entry widget
entry_text = tk.StringVar()

# Create an entry widget for displaying calculations
entry = ttk.Entry(root, textvariable=entry_text, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Style configuration
style = ttk.Style()
style.theme_use('clam')

# Style for number buttons
style.configure("TButton", foreground="black", background="white", font=("Arial", 14), relief="flat")
style.map("TButton", background=[("active", "lightgrey")])

# Function to update the entry widget with the pressed button's text
def button_click(text):
    current_text = entry_text.get()
    entry_text.set(current_text + text)

# Function to clear the entry widget
def clear_entry():
    entry_text.set("")

# Function to evaluate the expression in the entry widget
def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(result)
    except Exception as e:
        entry_text.set("Error")

# Function to handle key presses
def key_press(event):
    key = event.keysym
    if key in "0123456789":
        button_click(key)
    elif key in ["plus", "minus", "slash", "asterisk"]:
        button_click({"plus": "+", "minus": "-", "slash": "/", "asterisk": "*"}[key])
    elif key == "Return":
        calculate()
    elif key == "BackSpace":
        entry_text.set(entry_text.get()[:-1])
    elif key == "Escape":
        clear_entry()

# Define button texts in a 2D list for easy layout management
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

# Create and place buttons using a loop
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            button = ttk.Button(root, text=text, command=calculate)
        else:
            button = ttk.Button(root, text=text, command=lambda t=text: button_click(t))
        button.grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

# Add a clear button
clear_button = ttk.Button(root, text="AC", command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

# Configure grid to make buttons expand and fill space
root.grid_rowconfigure(0, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Bind key presses to the key_press function
root.bind("<KeyPress>", key_press)

# Start the Tkinter event loop
root.mainloop()