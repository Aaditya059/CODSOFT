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
root.geometry("312x330")
root.resizable(0, 0)

input_text = tk.StringVar()
input_frame = tk.Frame(root, width=312, height=50, highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="light blue", bd=5)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Create a function to create buttons more easily
def create_button(text, row, column, command=None):
    button = tk.Button(btns_frame, text=text, fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", command=command)
    button.grid(row=row, column=column, padx=1, pady=1)

create_button("C", 0, 0, btn_clear)
create_button("/", 0, 3, lambda: btn_click("/"))
create_button("7", 1, 0, lambda: btn_click(7))
create_button("8", 1, 1, lambda: btn_click(8))
create_button("9", 1, 2, lambda: btn_click(9))
create_button("*", 1, 3, lambda: btn_click("*"))
create_button("4", 2, 0, lambda: btn_click(4))
create_button("5", 2, 1, lambda: btn_click(5))
create_button("6", 2, 2, lambda: btn_click(6))
create_button("-", 2, 3, lambda: btn_click("-"))
create_button("1", 3, 0, lambda: btn_click(1))
create_button("2", 3, 1, lambda: btn_click(2))
create_button("3", 3, 2, lambda: btn_click(3))
create_button("+", 3, 3, lambda: btn_click("+"))
create_button("0", 4, 0, lambda: btn_click(0))
create_button(".", 4, 2, lambda: btn_click("."))
create_button("=", 4, 3, calculate)

root.mainloop()
