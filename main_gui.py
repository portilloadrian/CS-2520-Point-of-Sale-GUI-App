import tkinter as tk
from tkinter import ttk

def on_click():
    # Changes the label text when the button is pressed
    label.config(text="Button Clicked!")

# 1. Initialize the main window application
root = tk.Tk()
root.title("Point of Sale Application")
root.geometry("500x500")

# 2. Create modern themed widgets
label = ttk.Label(root, text="Welcome to Point of Sale Application", font=("Arial", 14))
label.pack(pady=10)

button = ttk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# 3. Start the event loop to keep the window open
root.mainloop()
