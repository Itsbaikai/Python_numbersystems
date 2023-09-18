from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("进制转换")
root.geometry('600x450')

def one():
    b = bin(int(e2.get()))
    e3.set(b)

def two():
    c = oct(int(e2.get()))
    e3.set(c)

def three():
    d = hex(int(e2.get()))
    e3.set(d)

def two_ten():
    e = int(e4.get(), 2)
    e5.set(e)

def eight_ten():
    f = int(e6.get(), 8)
    e7.set(f)

def six_ten():
    g = int(e8.get(), 16)
    e9.set(g)

label = Label(root, text='进制转换', font=("Arial Bold", 30))
label.grid(row=0, column=1)
t2 = tk.Label(root, text='请输入你要转换的十进制:\t')
t2.grid(row=1, column=0)
t3 = tk.Label(root, text='结果\t:')
t3.grid(row=2, column=0)
t4 = tk.Label(root,text= "请输入想要转换为十进制的二进制:\t")
t4.grid(row=4,column=0)
t5 = tk.Label(root,text= "请输入想要转换为十进制的八进制:\t")
t5.grid(row=6,column=0)
t6 = tk.Label(root,text= "请输入想要转换为十进制的十六进制:\t")
t6.grid(row=8,column=0)


e2 = tk.Entry(root) #获取的信息数字
e2.grid(row=1, column=1)
e4 = tk.Entry(root)
e4.grid(row=4,column=1)

e3 = tk.StringVar()
tk.Label(root, width=20, height=1, bg='white', textvariable=e3).grid(row=2, column=1)
e5 = tk.StringVar()
tk.Label(root, width=20, height=1, bg='white', textvariable=e5).grid(row=5, column=1)

e6 = tk.Entry(root)
e6.grid(row=6,column=1)
e7 = tk.StringVar()
tk.Label(root, width=20, height=1, bg='white', textvariable=e7).grid(row=7, column=1)

e8 = tk.Entry(root)
e8.grid(row=8,column=1)
e9 = tk.StringVar()
tk.Label(root, width=20, height=1, bg='white', textvariable=e9).grid(row=9, column=1)

btn1 = Button(root,text="二进制",bg='#C0C0C0', command=one)
btn2 = Button(root,text="八进制",bg='#C0C0C0', command=two)
btn3 = Button(root,text="十六进制",bg='#C0C0C0', command=three)
btn4 = Button(root,text="十进制",bg='#C0C0C0', command=two_ten)
btn5 = Button(root,text="八进制",bg='#C0C0C0', command=eight_ten)
btn6 = Button(root,text="十六进制",bg='#C0C0C0', command=six_ten)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=3)
btn4.grid(row=5, column=0)
btn5.grid(row=7, column=0)
btn6.grid(row=9, column=0)

root.mainloop()