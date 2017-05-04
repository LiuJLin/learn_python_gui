import tkinter, sys
from tkinter import *
# window
root = Tk()
# title
root.title("顶层窗口")

# frame框架
for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
    f = Frame(root, borderwidth = 2, relief = relief)
    # label , text
    Label(f, text = relief, width = 10).pack(side = LEFT)
    f.pack(side = LEFT, padx = 5, pady = 5)
# buttons
Button(root, text = "Disabled", state = DISABLED).pack(side = LEFT)
Button(root, text = "Cancel").pack(side = LEFT)
Button(root, text = "OK").pack(side = LEFT)
Button(root, text = "Quit", command = root.quit).pack(side = RIGHT)

#entry 输入框
f1 = Frame(root)
Label(f1, text = "Standard Entry: ").pack(side = LEFT, padx = 5, pady = 10)
e1 = StringVar()
Entry(f1, width = 50, textvariable = e1).pack(side = LEFT)
e1.set("输入框默认内容")
f1.pack()

f2 = Frame(root)
Label(f2, text = "Disabled Entry: ").pack(side = LEFT, padx = 5, pady = 10)
e2 = StringVar()
Entry(f2, width = 50, textvariable = e2, state = DISABLED).pack(side = LEFT)
e2.set("不可修改的内容")
f2.pack()

root.mainloop()
