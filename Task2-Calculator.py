import tkinter as tk

def btn_click(number):
    current = input_text.get()
    input_text.set(current + str(number))

def btn_clear():
    input_text.set("")

def calculate():
    try:
        result = eval(input_text.get())
        input_text.set(str(result))
    except:
        input_text.set("Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("330x300")
root.resizable(0, 0)

input_text = tk.StringVar()
input_frame = tk.Frame(root, width=330, height=50, highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('Arial', 18), textvariable=input_text, width=28, bd=5)
input_field.grid(row=0, column=0, columnspan=4)
input_field.pack(ipady=10)

btns_frame = tk.Frame(root, width=330, height=272.5, bg="grey")
btns_frame.pack()

def create_button(text, row, column, command=None, columnspan=1):  # Added columnspan parameter
    button = tk.Button(btns_frame, text=text, width=6, height=2, bd=0, cursor="hand2", command=command, font=('Arial', 14))
    button.grid(row=row, column=column, columnspan=columnspan, padx=1, pady=1)


#create_button("C", 1, 0, btn_clear, columnspan=3)
create_button("/", 1, 3, lambda: btn_click("/"))
create_button("7", 2, 0, lambda: btn_click(7))
create_button("8", 2, 1, lambda: btn_click(8))
create_button("9", 2, 2, lambda: btn_click(9))
create_button("*", 2, 3, lambda: btn_click("*"))
create_button("4", 3, 0, lambda: btn_click(4))
create_button("5", 3, 1, lambda: btn_click(5))
create_button("6", 3, 2, lambda: btn_click(6))
create_button("-", 3, 3, lambda: btn_click("-"))
create_button("1", 4, 0, lambda: btn_click(1))
create_button("2", 4, 1, lambda: btn_click(2))
create_button("3", 4, 2, lambda: btn_click(3))
create_button("+", 4, 3, lambda: btn_click("+"))
#create_button("0", 5, 0, lambda: btn_click(0))
create_button(".", 5, 2, lambda: btn_click("."))
create_button("=", 5, 3, calculate)

def create_button1(text, row, column, command=None, columnspan=1):
    button = tk.Button(btns_frame, text=text, width=27, height=2, bd=0, cursor="hand2", command=command, font=('Arial', 14))
    button.grid(row=row, column=column, columnspan=columnspan, padx=1, pady=1)

create_button1("C", 1, 0, btn_clear, columnspan=3)


def create_button2(text, row, column, command=None, columnspan=2):
    button = tk.Button(btns_frame, text=text, width=16, height=2, bd=0, cursor="hand2", command=command, font=('Arial', 14))
    button.grid(row=row, column=column, columnspan=columnspan, padx=1, pady=1)

create_button2("0", 5, 0, btn_clear, columnspan=2)

root.mainloop()
