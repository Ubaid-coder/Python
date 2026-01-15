import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

def getTime():
    string = time.strftime("%H: %M, %S %p \n %D")
    label.config(text=string)
    label.after(1000,getTime)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

getTime()

root.mainloop()