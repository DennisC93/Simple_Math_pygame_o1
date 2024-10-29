import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Information", "Button clicked!")

def create_ui():
    root = tk.Tk()
    root.title("Simple UI")

    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
