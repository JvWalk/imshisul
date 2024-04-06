import tkinter as tk
import GwamokCaller


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
for i in range(GwamokCaller.gwamok.shape[0]):
    for j in range(GwamokCaller.gwamok.shape[1]):
        show  = tk.Label(text=GwamokCaller.gwamok[i][j], width=20, height=2)
        show.grid(row=i+1, column=j)
        

