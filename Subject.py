import tkinter as tk
import numpy as np

def get():
    subjectFile = open("basics.txt", 'r')
    subject = subjectFile.readlines()
    subjectList = [x.split() for x in subject]
    subjectInfo = {}
    for i in subjectList: print(*i)

def Caller():
    f = open("basics.txt", 'r')
    arr = []
    for line in f:
        line = line.strip()
        list= line.split('	', 6)
        arr.extend([list])
        gwamok = np.array(arr)
    f.close()
    return gwamok

def Changer(Gwamok):
    f = open("basics.txt", 'w')
    for i in range(Gwamok.shape[0]):
        for j in range(Gwamok.shape[1]):
            f.write(Gwamok[i,j])
            f.write('\t') 
        f.write('\n')
    f.close()


def Shower():
    popup=tk.Tk()
    popup.title("YUN DAE HEE")
    popup.geometry("900x1000+100+1")
    popup.resizable(False, False)

    label = tk.Label(popup, height=1)
    show = tk.Label(text="class number", width=20, height=2)
    show.grid(row=0, column=0)
    show = tk.Label(text="class name", width=20, height=2)
    show.grid(row=0, column=1)
    show = tk.Label(text="class pilsu", width=20, height=2)
    show.grid(row=0, column=2)
    show = tk.Label(text="class credit", width=20, height=2)
    show.grid(row=0, column=3)
    show = tk.Label(text="class time", width=20, height=2)
    show.grid(row=0, column=4)
    show = tk.Label(text="class room", width=20, height=2)
    show.grid(row=0, column=5)
    for i in range(Caller.gwamok.shape[0]):
        for j in range(Caller.gwamok.shape[1]):
            show  = tk.Label(text=Caller.gwamok[i][j], width=20, height=2)
            show.grid(row=i+1, column=j)
        
    popup.mainloop()