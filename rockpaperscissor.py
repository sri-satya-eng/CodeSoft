import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user):
    computer = random.choice(choices)

    if user == computer:
        result = "Tie!"
    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    output.config(
        text=f"You: {user}\nComputer: {computer}\n{result}"
    )

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

tk.Label(root, text="Rock Paper Scissors",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="Rock",
          command=lambda: play("Rock")).pack(pady=5)

tk.Button(root, text="Paper",
          command=lambda: play("Paper")).pack(pady=5)

tk.Button(root, text="Scissors",
          command=lambda: play("Scissors")).pack(pady=5)

output = tk.Label(root, text="", font=("Arial", 12))
output.pack(pady=20)

root.mainloop()