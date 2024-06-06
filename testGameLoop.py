import tkinter
timer = 0
def countUp():
    global timer
    timer += 1
    label["text"] = timer
    root.after(1000,countUp)

root = tkinter.Tk()
label = tkinter.Label(font=("Times New Roan",80))
label.pack()
root.after(1000,countUp)
root.mainloop()
