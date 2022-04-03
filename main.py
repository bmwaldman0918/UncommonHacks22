from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sys
import os
from photo_sorting import PhotoLib
from color import Color

coldict = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "white": (0, 0, 0),
           "black": (255, 255, 255)}
rgb = Color()
grey = False
directory = ""
fileList = list()
validDir = False


def quitted():
    sys.exit()


def open_image():
    global rgb
    global grey
    global directory
    global validDir
    global canvas
    directory = e1.get()
    try:
        rgb.red = coldict[colChoose.get()][0]
        rgb.green = coldict[colChoose.get()][1]
        rgb.blue = coldict[colChoose.get()][2]
    except KeyError:
        grey = True
    if not os.path.isdir(directory):
        messagebox.showwarning("Warning", "Please input a valid directory")
    else:
        validDir = True
        image_display = Toplevel()
        canvas = Canvas(image_display, width=700, height=700)
        canvas.pack()
        image_display.title("Image Viewer")
        display("image.jpg")
        display("0001.jpg")

    print(dir)
    print(rgb)


def display(name):
    global img
    canvas.delete("all")
    imgf = Image.open(os.path.join(directory, name))
    imgf.thumbnail((600, 600))
    img = ImageTk.PhotoImage(imgf)
    canvas.create_image(0, 0, anchor=NW, image=img)


root = Tk()
root.title("Search for a file")
root.geometry("800x500")
colChoose = StringVar(root)
tex1 = Label(root, text="Directory")
tex1.grid(row=0, column=0)
tex2 = Label(root, text="Color")
tex2.grid(row=1, column=0)
e1 = Entry(root)
col = OptionMenu(root, colChoose, "red", "green", "blue", "grey", "black", "white")
e1.grid(row=0, column=1)
col.grid(row=1, column=1)
button1 = Button(root, text="sort", bd=2, command=open_image)
button1.grid(row=2, column=0)
root.protocol("WM_DELETE_WINDOW", quitted)
print(colChoose)
root.mainloop()
