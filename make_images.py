from PIL import Image
import os
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw() 

file_path = filedialog.askopenfilename()

im = Image.open(file_path)
name, ext = os.path.splitext(file_path)

imgre=im.resize((400, 400))

filename = name + "_resized.png"
imgre.save(filename)

parent_dir = "./Images/"
fd = os.path.join(parent_dir, name)
os.mkdir(fd)

w,h = imgre.size
d = 100
k = 1
for i in range(4):
    for j in range(4):
        box = (j * d, i * d, (j + 1) * d, (i + 1) * d)
        title = imgre.crop(box)
        savetitle = os.path.join(fd, f'img{k}.png')
        title.save(savetitle)
        k+=1