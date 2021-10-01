import tkinter, sys
from tkinter import scrolledtext

root = tkinter.Tk()

def save():
    cur_inp = textFrame.get("1.0", tkinter.END)
    fl = open("output.txt", "w")
    print("antes ", fl)
    fl.write(cur_inp)
    print(fl.read)

textFrame = scrolledtext.ScrolledText(root, width=100, bd=10, relief="raised")
textFrame.pack()
saveb = tkinter.Button(root, text="Save", command= save)
saveb.pack()




root.mainloop()