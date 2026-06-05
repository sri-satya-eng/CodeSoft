import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text=password)
    except:
        messagebox.showerror("Error", "Enter a valid number")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=10)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()