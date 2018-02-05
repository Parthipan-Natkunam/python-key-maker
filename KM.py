from tkinter import *
import random, sys
window = Tk()
window.title("Key Maker - v1.0")
window.wm_iconbitmap("favicon.ico")
window.resizable(0,0)
img = PhotoImage(file = "logo.gif")
logoLabel = Label(window,image = img)
txtBox = Text(window,relief = "flat", height=1,width=25, borderwidth=0)
getBtn = Button(window)
setBtn = Button(window)
logoLabel.grid(row=1,column=1,rowspan=4)
txtBox.grid(row=2,column=2,padx=10)
getBtn.grid(row=3,column=2,columnspan=3)
setBtn.grid(row=4,column=2,columnspan=3)
txtBox.configure(state="disabled")
getBtn.configure(text="Generate",state=NORMAL)
setBtn.configure(text="Reset",state=DISABLED)
def generateKey():
     sequenceStr = "ABCDFGHJIKLMNOPQRSTUVWXYZ1234567890"
     key = ""
     txtBox.configure(state="normal")
     for i in range(1):
            key = ('-'.join(''.join(random.choice(sequenceStr) for _ in range(4)) for _ in range(4)))
     txtBox.insert(2.0, key)
     txtBox.configure(state="disabled")
     getBtn.configure(state=DISABLED)
     setBtn.configure(state=NORMAL)
def resetTxtBox():
    txtBox.configure(state="normal")
    txtBox.delete(1.0,END)
    txtBox.configure(state="disabled")
    getBtn.configure(state=NORMAL)
    setBtn.configure(state=DISABLED)
getBtn.configure(command=generateKey)
setBtn.configure(command=resetTxtBox)
window.mainloop()
