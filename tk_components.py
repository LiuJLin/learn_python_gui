import tkinter
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
    
root.mainloop()
