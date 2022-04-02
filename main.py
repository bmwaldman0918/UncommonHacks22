from tkinter import *

import sys
#from photo_sorting import Photo

def quitted():
    sys.exit()


root = Tk()
root.title("Search for a file")
tex1 = Label(root, text="Directory").grid(row=0,column=0)
tex2 = Label(root, text="Color").grid(row=1,column=0)
e1 = Entry(root)
e2 = Entry(root,show="*")
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
root.protocol("WM_DELETE_WINDOW", quitted)
root.mainloop()