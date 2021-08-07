from tkinter import *
#######################################
root = Tk()
root.title("Calculator")

current = " "
state = -1


def putin(n):
    curr = len(e.get())
    e.insert(curr, str(n))


def add():
    global current
    current = e.get()
    if (len(current) == 0):
        return
    e.delete(0, 10000)
    global state
    state = 0


def subtract():
    global current
    current = e.get()
    if (len(current) == 0):
        return
    e.delete(0, 10000)
    global state
    state = 1


def multiply():
    global current
    current = e.get()
    if (len(current) == 0):
        return
    e.delete(0, 10000)
    global state
    state = 2


def divide():
    global current
    current = e.get()
    if (len(current) == 0):
        return
    e.delete(0, 10000)
    global state
    state = 3


def equals():
    now = e.get()
    e.delete(0, 10000)
    if (state == -1):
        e.delete(0, 10000)
        e.insert(0, "Error, click on \"Clear\"")
    elif (state == 0 and len(current) > 0 and len(now) > 0):
        e.insert(0, int(current)+int(now))
    elif (state == 1 and len(current) > 0 and len(now) > 0):
        e.insert(0, int(current)-int(now))
    elif (state == 2 and len(current) > 0 and len(now) > 0):
        e.insert(0, int(current)*int(now))
    elif (state == 3 and len(current) > 0 and len(now) > 0):
        e.insert(0, int(current)/int(now))
    else:
        e.insert(0, "Error, click on \"Clear\"")


def clear():
    e.delete(0, 10000)
    global current
    current = " "
    global state
    state = -1


e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

number9 = Button(root, text="9", padx=40, pady=20, command=lambda: putin(9))  #
number8 = Button(root, text="8", padx=40, pady=20, command=lambda: putin(8))  #
number7 = Button(root, text="7", padx=40, pady=20, command=lambda: putin(7))  #
number6 = Button(root, text="6", padx=40, pady=20, command=lambda: putin(6))  #
number5 = Button(root, text="5", padx=40, pady=20, command=lambda: putin(5))  #
number4 = Button(root, text="4", padx=40, pady=20, command=lambda: putin(4))  #
number3 = Button(root, text="3", padx=40, pady=20, command=lambda: putin(3))  #
number2 = Button(root, text="2", padx=40, pady=20, command=lambda: putin(2))  #
number1 = Button(root, text="1", padx=40, pady=20, command=lambda: putin(1))  #
number0 = Button(root, text="0", padx=40, pady=20, command=lambda: putin(0))  #
equals = Button(root, text="=", padx=86, pady=20, command=equals)  #
add = Button(root, text="+", padx=40, pady=51, command=add)  #
subtract = Button(root, text="-", padx=40, pady=20, command=subtract)  #
divide = Button(root, text="÷", padx=40, pady=20, command=divide)  #
multiply = Button(root, text="x", padx=40, pady=20, command=multiply)  #
clear = Button(root, text="Clear", padx=40, pady=20, command=clear)

number9.grid(row=1, column=2)
number8.grid(row=1, column=1)
number7.grid(row=1, column=0)
number6.grid(row=2, column=2)
number5.grid(row=2, column=1)
number4.grid(row=2, column=0)
number3.grid(row=3, column=2)
number2.grid(row=3, column=1)
number1.grid(row=3, column=0)
number0.grid(row=4, column=0)
equals.grid(row=4, column=1, columnspan=2)
add.grid(row=3, column=4, rowspan=2)
subtract.grid(row=2, column=4)
multiply.grid(row=1, column=4)
divide.grid(row=0, column=4)
clear.grid(row=5, column=0, columnspan=3)

root.mainloop()
