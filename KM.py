from tkinter import *
import random, sys
window = Tk()
window.title("Key Maker - v1.0")
window.wm_iconbitmap("favicon.ico")
window.resizable(0,0)
img = PhotoImage(file = "logo.gif")
logLabel = Label(window,image = img)
ent1 = Text(window,relief = "flat", height=1,width=25, borderwidth=0)
getBtn = Button(window)
setBtn = Button(window)
logLabel.grid(row=1,column=1,rowspan=4)
ent1.grid(row=2,column=2,padx=10)
getBtn.grid(row=3,column=2,columnspan=3)
setBtn.grid(row=4,column=2,columnspan=3)
ent1.configure(state="disabled")
getBtn.configure(text="Generate",state=NORMAL)
setBtn.configure(text="Reset",state=DISABLED)
def gen():
     seq = "ABCDFGHJIKLMNOPQRSTUVWXYZ1234567890"
     key = ""
     ent1.configure(state="normal")
     for i in range(1):
            key = ('-'.join(''.join(random.choice(seq) for _ in range(4)) for _ in range(4)))
     ent1.insert(2.0, key)
     ent1.configure(state="disabled")
     getBtn.configure(state=DISABLED)
     setBtn.configure(state=NORMAL)
def res():
    ent1.configure(state="normal")
    ent1.delete(1.0,END)
    ent1.configure(state="disabled")
    getBtn.configure(state=NORMAL)
    setBtn.configure(state=DISABLED)
getBtn.configure(command=gen)
setBtn.configure(command=res)
window.mainloop()
