import tkinter as tk
from tkinter import ttk
import random
import string


class MyPasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x250")
        self.configure(bg="purple")

        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self, text="Password Generator", font=("Arial", 18, "bold"), foreground="white",
                                background="purple")
        title_label.pack(pady=10)

        username_label = ttk.Label(self, text="Username:", foreground="white", background="purple")
        username_label.pack()

        self.username_var = tk.StringVar()
        username_entry = ttk.Entry(self, textvariable=self.username_var)
        username_entry.pack(pady=5)

        length_label = ttk.Label(self, text="Password Length:", foreground="white", background="purple")
        length_label.pack()

        self.length_var = tk.StringVar()
        length_entry = ttk.Entry(self, textvariable=self.length_var)
        length_entry.pack(pady=5)

        generate_button = ttk.Button(self, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)
        generate_button.configure(style="TButton")

        self.password_label = ttk.Label(self, text="", foreground="white", background="purple", font=("Arial", 14))
        self.password_label.pack()

        self.style = ttk.Style()
        self.style.configure("TButton", foreground="black", background="#3498DB")

    def generate_password(self):
        length = int(self.length_var.get())
        if length <= 0:
            self.password_label.config(text="Please enter a valid length", foreground="red")
            return

        complexity = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(complexity) for _ in range(length))
        self.password_label.config(text=generated_password, foreground="white")


if __name__ == '__main__':
    app = MyPasswordGenerator()
    app.mainloop()
