import tkinter
# ウインドウオブジェクト
root = tkinter.Tk()
root.title("初めてのウインドウ")
root.geometry("800x600")

# キャンパスの作成
canvas = tkinter.Canvas(root,width=800,height=600,bg="skyblue")
canvas.pack()

# 画像の表示
img = tkinter.PhotoImage(file="images\Ball.png")
canvas.create_image(200,300,image=img)

# ウインドウを表示
root.mainloop()