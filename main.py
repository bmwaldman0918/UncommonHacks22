from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sys
import os
from photo_sorting import PhotoLib, Photo
from jpeg_to_array import jpeg_to_4vector
from color import Color

coldict = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "white": (0, 0, 0),
           "black": (255, 255, 255)}

rgb = Color()
grey = False
dir = ""
fileList = list()
validDir = False
rgb = Color()
grey = False
directory = ""
fileList = list()
validDir = False
sorted = list()
isSort = False
currIndex = 0


def quitted():
    sys.exit()


def allImageFiles(path: str):
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
    files_to_PhotoLib()


def file_to_Photo(f: str):
    numpy_arr = jpeg_to_4vector(f)
    ph = Photo(numpy_arr, f)
    return ph


def files_to_PhotoLib():
    global photos
    ls = list()
    for file in fileList:
        ls.append(file_to_Photo(file))
    photos = PhotoLib(ls)
    print(photos.photos)


def phList_to_fileList():
    global fileList
    fileList = list()
    for photo in sorted:
        fileList.append(photo.name)
    print(fileList)


def open_image():
    global rgb
    global grey
    global directory
    global validDir
    global canvas
    global button2
    global sorted
    global isSort
    dir = e1.get()
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
        button3["state"] = NORMAL
        image_display.title("Image Viewer")
        if not isSort:
            allImageFiles(dir)
            sorted = photos.sort(Photo.comp_by_col(c=rgb))
            phList_to_fileList()
            isSort = True
        display(fileList[0])

    print(dir)
    print(rgb)


def display(name):
    global img
    canvas.delete("all")
    imgf = Image.open(os.path.join(directory, name))
    imgf.thumbnail((600, 600))
    img = ImageTk.PhotoImage(imgf)
    canvas.create_image(0, 0, anchor=NW, image=img)


def buttonWithdraw(bt: Button):
    bt.withdraw()


def ableSelectButton(*attr):
    global button1
    global isSort
    if button1["state"] == DISABLED:
        button1["state"] = NORMAL
    if isSort:
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        isSort = False


def goNext():
    global canvas
    global currIndex
    canvas.delete("all")
    currIndex += 1
    display(fileList[currIndex])
    if currIndex > 0:
        button2["state"] = NORMAL
    if currIndex == len(fileList) - 1:
        button3["state"] = DISABLED
    print(fileList[currIndex])


def goPrev():
    global currIndex
    canvas.delete("all")
    currIndex -= 1
    display(fileList[currIndex])
    if currIndex == 0:
        button3["state"] = DISABLED


if __name__ == "__main__":
    root = Tk()
    root.title("Search for a file")
    root.geometry("800x500")
    colChoose = StringVar(root)
    tex1 = Label(root, text="Directory")
    tex1.grid(row=0, column=0)
    tex2 = Label(root, text="Color")
    tex2.grid(row=1, column=0)
    e1 = Entry(root)
    col = OptionMenu(root, colChoose, "red", "green", "blue", "grey", "black", "white", command=ableSelectButton)
    e1.grid(row=0, column=1)
    col.grid(row=1, column=1)
    col = OptionMenu(root, colChoose, "red", "green", "blue", "grey", "black", "white")
    e1.grid(row=0, column=1)
    col.grid(row=1, column=1)
    button1 = Button(root, text="sort", bd=2, command=open_image)
    button1.grid(row=2, column=0)
    button2 = Button(root, text="prev", bd=2, command=goPrev, state=DISABLED)
    button3 = Button(root, text="next", bd=2, command=goNext, state=DISABLED)
    button2.grid(row=2, column=1)
    button3.grid(row=2, column=2)
    root.protocol("WM_DELETE_WINDOW", quitted)
    print(colChoose)

    root.mainloop()
    print(colChoose)
    root.mainloop()
