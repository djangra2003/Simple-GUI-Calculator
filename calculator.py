from tkinter import *
from tkinter import messagebox
import pyperclip

FOREGROUND = "#ffffff"
BASE = "#828282"
DARK = "#717171"
DARKER = "#5C5C5C"
BUTTON_FONT = ("Arial", 14, "bold")
LABEL_FONT = ("Arial", 24, "bold")

"""
Status: Very buggy....
What am I gonna do about it? Hopefully fix it
"""

class Application(Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.resizable(width=False, height=False)
        self.iconbitmap("")
        self.config(bg="#474747")

        def on_enter(event):
            event.widget.config(bg=DARK)
        def on_leave(event):
            event.widget.config(bg=BASE)
        def on_release(event):
            event.widget.config(bg=DARK)

        calculation_entry = Entry(self, fg=FOREGROUND, bg="#474747", width=10, font=LABEL_FONT, border=0, justify=RIGHT)
        calculation_entry.pack()

        copy_text = Label(self, text="Your calculation seems rather long... Copy to clipboard?", wraplength=200, fg="#ffffff", bg="#474747")

        num_pad = Frame(self, bg="#474747")
        num_pad.pack(padx=8, pady=8)

        def append_to_calculation(event, value):
            event.widget.config(bg=DARKER)
            calculation_entry.config(font=LABEL_FONT, width=10, justify=RIGHT)
            current_string = calculation_entry.get()
            new_string = str(current_string) + str(value)
            calculation_entry.delete(0, END)
            calculation_entry.insert(0, new_string)
            return "break"

        def calculate(event):
            try:
                event.widget.config(bg=DARKER)
                calculation_string = str(calculation_entry.get()).replace("^","**").replace("x","*").replace("÷","/")
                calculation = eval(calculation_string)
                calculation_entry.delete(0, END)
                calculation_entry.insert(0, calculation)
                if len(str(calculation)) > 10:
                    button_copy.pack()
                    copy_text.pack()
                elif len(str(calculation)) < 10:
                    button_copy.pack_forget()
                    copy_text.pack_forget()
            except ZeroDivisionError:
                calculation_entry.delete(0, END)
                calculation_entry.config(font=("Arial", 18, "bold"), width=19, justify=CENTER)
                calculation_entry.insert(0, "Zero Division Error")
            except SyntaxError:
                calculation_entry.delete(0, END)
                calculation_entry.config(font=("Arial", 18, "bold"), width=12, justify=CENTER)
                calculation_entry.insert(0, "Syntax Error")
            except OverflowError:
                calculation_entry.delete(0, END)
                calculation_entry.config(font=("Arial", 18, "bold"), width=14, justify=CENTER)
                calculation_entry.insert(0, "OverFlow Error")

            return "break"
        
        def clear(event):
            event.widget.config(bg=DARKER)
            calculation_entry.config(font=LABEL_FONT, width=10, justify=RIGHT)
            calculation_entry.delete(0, END)
            button_copy.pack_forget()
            copy_text.pack_forget()
            return "break"

        def switch_sign(event):      
            event.widget.config(bg=DARKER)
            calculate(event)
            current_string = calculation_entry.get()
            calculation_entry.delete(0, END)
            calculation_entry.insert(0, f"-({current_string})")
            return "break"
    
        def copy(event):
            event.widget.config(bg=DARKER)
            string = calculation_entry.get()
            pyperclip.copy(string)
            return "break"

        button_one = Button(num_pad, text="1", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_two = Button(num_pad, text="2", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_three = Button(num_pad, text="3", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_four = Button(num_pad, text="4", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_five = Button(num_pad, text="5", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_six = Button(num_pad, text="6", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_seven = Button(num_pad, text="7", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_eight = Button(num_pad, text="8", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_nine = Button(num_pad, text="9", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_zero = Button(num_pad, text="0", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)

        button_add = Button(num_pad, text="+", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_subtract = Button(num_pad, text="-", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_multiply = Button(num_pad, text="x", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_divide = Button(num_pad, text="÷", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_power = Button(num_pad, text="^", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_square = Button(num_pad, text="^2", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_decimal = Button(num_pad, text=".", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)

        button_equals = Button(num_pad, text="=", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_clear = Button(num_pad, text="Clr", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)
        button_pos_neg = Button(num_pad, text="±", bg=BASE, fg=FOREGROUND, font=BUTTON_FONT, relief=FLAT, height=2, width=4)

        button_copy = Button(self, text="Copy", font=("Arial", 8, "bold"), bg=BASE, fg=FOREGROUND, relief=FLAT)

        button_pos_neg.grid(row=0, column=0, padx=2, pady=2)
        button_square.grid(row=0, column=1, padx=2, pady=2)
        button_power.grid(row=0, column=2, padx=2, pady=2)
        button_divide.grid(row=0, column=3, padx=2, pady=2)
        button_seven.grid(row=1, column=0, padx=2, pady=2)
        button_eight.grid(row=1, column=1, padx=2, pady=2)
        button_nine.grid(row=1, column=2, padx=2, pady=2)
        button_multiply.grid(row=1, column=3, padx=2, pady=2)
        button_four.grid(row=2, column=0, padx=2, pady=2)
        button_five.grid(row=2, column=1, padx=2, pady=2)
        button_six.grid(row=2, column=2, padx=2, pady=2)
        button_subtract.grid(row=2, column=3, padx=2, pady=2)
        button_one.grid(row=3, column=0, padx=2, pady=2)
        button_two.grid(row=3, column=1, padx=2, pady=2)
        button_three.grid(row=3, column=2, padx=2, pady=2)
        button_add.grid(row=3, column=3, padx=2, pady=2)
        button_clear.grid(row=4, column=0, padx=2, pady=2)
        button_zero.grid(row=4, column=1, padx=2, pady=2)
        button_decimal.grid(row=4, column=2, padx=2, pady=2)
        button_equals.grid(row=4, column=3, padx=2, pady=2)
        
        button_one.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=1))
        button_two.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=2))
        button_three.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=3))
        button_four.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=4))
        button_five.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=5))
        button_six.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=6))
        button_seven.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=7))
        button_eight.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=8))
        button_nine.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=9))
        button_zero.bind("<Button-1>", lambda e: append_to_calculation(event=e, value=0))
        button_add.bind("<Button-1>", lambda e: append_to_calculation(event=e, value="+"))
        button_subtract.bind("<Button-1>", lambda e: append_to_calculation(event=e, value="-"))
        button_multiply.bind("<Button-1>", lambda e: append_to_calculation(event=e, value="x"))
        button_divide.bind("<Button-1>", lambda e: append_to_calculation(event=e, value="÷"))
        button_decimal.bind("<Button-1>", lambda e: append_to_calculation(event=e, value="."))
        button_power.bind("<Button-1>", lambda e: append_to_calculation(event=e, value="^"))
        button_square.bind("<Button-1>", lambda e: append_to_calculation(event=e, value="^2"))

        button_equals.bind("<Button-1>", lambda e: calculate(event=e))
        button_clear.bind("<Button-1>", lambda e: clear(event=e))
        button_pos_neg.bind("<Button-1>", lambda e: switch_sign(event=e))

        button_copy.bind("<Button-1>", lambda e: copy(event=e))

        buttons_list = [button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight, button_nine, button_zero, button_add, button_subtract, button_multiply, button_divide, button_equals, button_clear, button_decimal, button_power, button_square, button_pos_neg, button_copy]
        for button in buttons_list:
            button.bind("<Enter>", lambda e: on_enter(event=e))
            button.bind("<Leave>", lambda e: on_leave(event=e))
            button.bind("<ButtonRelease-1>", on_release)

if __name__ == '__main__':
    app = Application()
    app.mainloop()
