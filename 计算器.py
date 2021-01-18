'''
Author: 战恩泽
Date: 2021-01-17 01:10:26
Description: 计算器
'''
import os
import pickle
from tkinter import *

def chge_0208():
    choices[0] = '0208'
def chge_0802():
    choices[0] = '0802'
def chge_0810():
    choices[0] = '0810'
def chge_1008():
    choices[0] = '1008'
def chge_1016():
    choices[0] = '1016'
def chge_1610():
    choices[0] = '1610'

def chge_num():
    x = v1.get()
    if choices[0] == '0208'
        num = oct(int(x, 2))
    if choices[0] == '0802'
        num = bin(int(x, 8))
    if choices[0] == '0810'
        num = int(x, 8)
    if choices[0] == '1008'
        num = oct(int(x, 10))
    if choices[0] == '1016'
        num = hex(int(x, 10))
    if choices[0] == '1610'
        num = int(x, 16)
    l2.set(num)

root = Tk()
root.title("Calculator")

rows = 0
l1 = Label(root,text = "进制转换").grid(row = rows,sticky = W)

rows += 1
var = IntVar()
choices = ['0208']
R1 = Radiobutton(root,text = "二转八",variable = var,value = 1,command = chge_0208()).grid(row = rows,column = 0)
R2 = Radiobutton(root,text = "八转二",variable = var,value = 2,command = chge_0802()).grid(row = rows,column = 1)

rows += 1
R3 = Radiobutton(root,text = "八转十",variable = var,value = 3,command = chge_0810()).grid(row = rows,column = 0)
R4 = Radiobutton(root,text = "十转八",variable = var,value = 4,command = chge_1008()).grid(row = rows,column = 1)

rows += 1
R5 = Radiobutton(root,text = "十转十六",variable = var,value = 5,command = chge_1016()).grid(row = rows,column = 0)
R6 = Radiobutton(root,text = "十六转十",variable = var,value = 6,command = chge_1610()).grid(row = rows,column = 1)

rows += 1
v1 = StringVar()
e1 = Entry(root,textvariable = v1).grid(row = rows,column = 0,columnspan = 3,padx = 20,pady = 10)

rows += 1
l2 = Label(root,text = "0").grid(row = rows,sticky = W,column = 1)

rows += 1
Button(root,text = "计算",command = (lambda: chge_num())).grid(row = rows,column = 0,sticky = W,padx = 20,pady = 10)
Button(root,text = "清除",command = (lambda: del_text())).grid(row = rows,column = 1,sticky = W,padx = 20,pady = 10)

root.mainloop()