from tkinter import *
root = Tk()
root.title("Top window")
l = Listbox(root, height=6, width =15)
scroll = Scrollbar(root, command = l.yview)
l.configure(yscrollcommand = scroll.set)
l.pack(side = LEFT)
scroll.pack(side=RIGHT, fill = Y)
for item in range(20):
    l.insert(END, item)

f = Frame(root, borderwidth = 2, relief = GROOVE)
# label , text
Label(f, text = "FRUITS", width = 10).pack()
f.pack(side = LEFT, padx = 10, pady = 5)
l = Listbox(f, width =15)
l.pack()
for item in ["apple", "orange", "peach", "banana", "melon"]:
    l.insert(END, item)
root.mainloop()
