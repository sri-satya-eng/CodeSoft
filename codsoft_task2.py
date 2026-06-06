import tkinter as tk
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("1920x1080")
        self.root.resizable(True,True)
        self.expression = ""
        self.input_text = tk.StringVar()

        # Display field
        self.input_frame = tk.Frame(self.root, height=50, bg="lightgrey")
        self.input_frame.pack(fill="both")
        self.input_field = tk.Entry(
            self.input_frame,
            textvariable=self.input_text,
            font=("Arial", 20),
            bd=0,
            justify="right",
            bg="lightgrey",
        )
        self.input_field.pack(fill="both", ipadx=8, ipady=15)

        # Buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        row, col = 0, 0

        for btn in buttons:
            action = lambda x=btn: self.click(x)
            tk.Button(
                self.buttons_frame,
                text=btn,
                width=8,
                height=3,
                font=("Arial", 14),
                command=action
            ).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, item):
        if item == "C":
            self.expression = ""
            self.input_text.set("")

        elif item == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""

        else:
            self.expression += str(item)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()