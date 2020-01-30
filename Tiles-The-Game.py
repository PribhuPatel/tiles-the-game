from random import shuffle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

zero_index = 0
zero_column = 1
zero_row = 1
numbers = []
def_numbers = []
def_numbers2=[]

def check_win():
    if numbers == def_numbers or numbers == def_numbers2:
        win_mes = messagebox.askyesno("You Won", "Do you want to play again?")
        return win_mes


def button_pressed(num, column, row):
    global zero_index, zero_column, zero_row
    print(num)
    if (abs(zero_column - column) == 1 and abs(zero_row - row) == 0) or (
            abs(zero_column - column) == 0 and abs(zero_row - row) == 1):
        numbers[num], numbers[zero_index] = 0, numbers[num]
        zero_index = num
        draw_buttons()
        win_mes = check_win()
        if win_mes:
            if win_mes:
                reset()
            else:
                exit(0)


def draw_buttons():
    global zero_row, zero_column
    column = 1
    row = 2
    for i in range(0, len(numbers)):
        if numbers[i] == 0:
            text = ""
        else:
            text = numbers[i]
        ttk.Button(root, text=text, command=lambda i=i, column=column, row=row: button_pressed(i, column, row),width=2,padding="50 50 50 50").grid(column=column,row=row,
                                               sticky=(N, W))
        if numbers[i] == 0:
            zero_column = column
            zero_row = row
        if column == 3:
            column = 1
            row += 1
        else:
            column += 1


def reset():
    global zero_index, numbers, def_numbers,def_numbers2
    zero_index = 0
    numbers = list(range(1, 9))
    def_numbers = list(range(0, 9))
    def_numbers2=list(range(1,9))
    def_numbers2.append(0)
    shuffle(numbers)
    numbers.insert(0, 0)
    draw_buttons()


root = Tk()
root.title("Tiles Game")
# for i in range(0,6):
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
button_frame = ttk.Frame(root)
button_frame.grid(row=1, column=2, sticky=W+E+N+S)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(row=2, column=0, rowspan=1, columnspan=6, sticky=W+E+N+S)

ttk.Button(button_frame, text="Reset", command=reset, padding="23 0 23 0").grid(column=5, row=1, sticky=(E))

reset()

root.mainloop()
