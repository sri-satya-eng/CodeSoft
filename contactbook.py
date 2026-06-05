import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name and phone:
        contacts.append(f"{name} - {phone}")
        update_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Fill all fields")

def delete_contact():
    try:
        selected = listbox.curselection()[0]
        contacts.pop(selected)
        update_list()
    except:
        messagebox.showerror("Error", "Select a contact")

def update_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, contact)

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")

tk.Label(root, text="Contact Book",
         font=("Arial", 16, "bold")).pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)
name_entry.insert(0, "Name")

phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)
phone_entry.insert(0, "Phone")

tk.Button(root, text="Add Contact",
          command=add_contact).pack(pady=5)

tk.Button(root, text="Delete Contact",
          command=delete_contact).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

root.mainloop()