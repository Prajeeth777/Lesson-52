from tkinter import *

window=Tk()

window.title("My first tkinkter window")
window.geometry("400x300")

label1=Label(text="Hello World",fg="green",bg="yellow")
entry=Entry()
button=Button(text="Click Me",fg="blue")
text=Text(bg="lightgreen")

frame=Frame(master=window,relief=RAISED,borderwidth=5)
label2=Label(master=frame,text="in frame")

label1.pack()
entry.pack()
button.pack()
label2.pack()
frame.pack()
text.pack()

window.mainloop()
