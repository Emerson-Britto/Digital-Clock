from tkinter import *
from tkinter.ttk import *
from time import strftime

app = Tk()
app.title("Clock")

def updateTime():
	timeStr = strftime("%H:%M:%S %p")
	label.config(text=timeStr)
	label.after(1000, updateTime)

label = Label(app, font=("ds-digital", 80), background="black", foreground="purple")
label.pack(anchor="center")
updateTime()
mainloop()