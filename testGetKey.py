import tkinter
key = 0
def keyDown(e):
    global key
    key = e.keycode
    print("KEY:" + str(key))

root = tkinter.Tk()
root.bind("<KeyPress>",keyDown)
root.mainloop()
