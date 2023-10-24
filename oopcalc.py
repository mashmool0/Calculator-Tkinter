import tkinter as tk
from tkinter.messagebox import showinfo


class Calculator(tk.Tk):
    calcultaion = ''

    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # self.geometry('400x420')
        # self.resizable(0, 0)
        self.title('Calculatro')
        self.text_result = tk.Text(
            self, height=1.5, width=20, font=('Arial', 20), foreground='blue', bg='red')
        self.text_result.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Call funtions
        self.button_calc()

    def add_to_text(self, symbol):
        Calculator.calcultaion += str(symbol)
        self.text_result.delete(1.0, 'end')
        self.text_result.insert(1.0, Calculator.calcultaion)

    def clear_text(self):
        Calculator.calcultaion = ''
        self.text_result.delete(1.0, 'end')

    def eval_calculation(self, symbol):
        try:
            result = eval(str(symbol))
            Calculator.calcultaion = str(result)
            self.text_result.delete(1.0, 'end')
            self.text_result.insert(1.0, result)
        except:
            self.text_result.delete(1.0, 'end')
            self.text_result.insert(1.0, 'Error')

    def delete_one(self):
        Calculator.calcultaion = Calculator.calcultaion[:-1]
        self.text_result.delete(1.0, 'end')
        self.text_result.insert(1.0, Calculator.calcultaion)

    def button_calc(self):
        # button list
        button = [
            (1, 0, '1'), (1, 1, '2'), (1, 2, '3'), (1, 3, '/'),
            (2, 0, '4'), (2, 1, '5'), (2, 2, '6'), (2, 3, '*'),
            (3, 0, '7'), (3, 1, '8'), (3, 2, '9'), (3, 3, '+'),
            (4, 0, '0'), (4, 1, '('), (4, 2, ')'), (4, 3, '-')


        ]

        for (row, col, text) in button:
            btn = tk.Button(self, text=text, command=lambda t=text: self.add_to_text(
                t), width=5, font=('Arial', 20), bg='green', fg='white')
            btn.grid(row=row, column=col, padx=5, pady=5)

        # another button
        btn_C = tk.Button(self, text='C', command=lambda: self.clear_text(), font=(
            'Arial', 20), width=5, bg='blue', fg='white')
        btn_C.grid(row=5, column=0)

        btn_equl = tk.Button(self, text='=', command=lambda: self.eval_calculation(
            Calculator.calcultaion), font=('Arial', 20), width=5, bg='blue', fg='white')
        btn_equl.grid(row=5, column=3)

        btn_onedel = tk.Button(self, text='<--', command=lambda: self.delete_one(),
                               font=('Arial', 20), width=5, bg='blue', fg='white')
        btn_onedel.grid(row=5, column=2)


app = Calculator()
app.mainloop()
