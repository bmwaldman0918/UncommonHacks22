from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sys
import os
from photo_sorting import PhotoLib
from color import Color

coldict = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0 ,255), "white": (0, 0, 0),
           "black": (255, 255, 255)}

rgb = Color()
grey = False
dir = ""
fileList = list()
photos = list()
validDir = False
def quitted():
    sys.exit()

def allImageFiles(path : str):
    for file in os.listdir(path):
        f = os.path.join(path, file)
        if not os.path.isfile(f):
            continue
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', 'ppm')):
            try:
                image = Image.open(f)
                image.verify()
                fileList.append(f);
            except Exception:
                continue
    print (fileList)

def file_to_Photo():


def files_to_PhotoLib():
    for file in fileList:



def openImage():
    global rgb
    global grey
    global dir
    global validDir
    global canvas
    global button2
    dir = e1.get()
    try:
        rgb.red = coldict[colChoose.get()][0]
        rgb.green = coldict[colChoose.get()][1]
        rgb.blue = coldict[colChoose.get()][2]
    except KeyError:
        grey = True;
    if not os.path.isdir(dir):
        messagebox.showwarning("Warning","Please input a valid directory")
    else:
        validDir = True
        imageDisplay = Toplevel()
        canvas = Canvas(imageDisplay, width=700, height=700)
        canvas.pack()
        button3["state"] = NORMAL
        imageDisplay.title("Image Viewer")
        display("image.jpg")
        display("0001.jpg")
        allImageFiles(dir)
    print(dir)
    print(rgb)

def display(name : str):
    global img
    canvas.delete("all")
    imgf = Image.open(os.path.join(dir, name))
    imgf.thumbnail((600, 600))
    img = ImageTk.PhotoImage(imgf)
    canvas.create_image(0, 0, anchor=NW, image=img)

def buttonWithdraw(bt: Button):
    bt.withdraw()

def ableSelectButton(*attr):
    global button1
    if button1["state"] == DISABLED:
        button1["state"] = NORMAL

def goNext():
    global canvas
    canvas.delete("all")


def goPrev():
    pass

root = Tk()
root.title("Search for a file")
root.geometry("800x500")
colChoose = StringVar(root)
tex1 = Label(root, text="Directory").grid(row=0,column=0)
tex2 = Label(root, text="Color").grid(row=1,column=0)
e1 = Entry(root)
col = OptionMenu(root, colChoose, "red", "green", "blue", "grey", "black", "white", command=ableSelectButton)
e1.grid(row=0,column=1)
col.grid(row=1,column=1)
button1 = Button(root, text="sort", bd=2, command=openImage, state=DISABLED)
button1.grid(row=2, column=0)
button2 = Button(root, text= "prev", bd=2, command=goPrev, state=DISABLED)
button3 = Button(root, text= "next", bd=2, command=goNext, state=DISABLED)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
root.protocol("WM_DELETE_WINDOW", quitted)
print (colChoose)

root.mainloop()