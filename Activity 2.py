from tkinter import *

window=Tk()
window.title("Tkinter Grid")

for i in range(3):
    for j in range(3):
          frame=Frame(master=window,
                      relief=GROOVE,
                      borderwidth=4)
          frame.grid(row=i,column=j,padx=5,pady=5)
          label=Label(master=frame,text=f"Row{i}/Column{j}")
          label.pack()

window.mainloop()
