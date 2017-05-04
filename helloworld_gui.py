#标题栏默认是tk，可以拖动改变窗口大小，窗口部件还可以组合

import tkinter
from tkinter import *
#创建一个Tk的根部件，一个普通的窗口，包括标题栏和最大化按钮等
root = Tk()
#标签部件，参数一是父部件，标签部件可以现实文本、图标、或图像，这里使用了文字
word = Label(root, text = "Hello, world!")
# pack方法，根据文本大小适应加入根窗口部件中
word.pack()
#根窗口的mainloop方法，使得Tkinter进入其时间循环
root.mainloop()
