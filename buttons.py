#单选按钮和复选按钮
from tkinter import *
root = Tk()
root.title("Top Window")
#RATIOBUTTON 单选按钮
# foo = IntVar()
# for text, value in [('red',1), ('green', 2), ('black', 3),('blue', 4), ('yellow',5)]:
#     r = Radiobutton(root, text = text, value = value, variable = foo)
#     r.pack(anchor = W)
# foo.set(2)

#CHECKBUTTON 复选按钮
l = [('red',1, NORMAL), ('green', 2,NORMAL), ('black', 3,NORMAL),('blue', 4,DISABLED), ('yellow',5,DISABLED)]
for text,value,status in l:
    foo = IntVar()
    c = Checkbutton(root, text=text, variable = foo, state = status)
    c.pack(anchor = W)

root.mainloop()
