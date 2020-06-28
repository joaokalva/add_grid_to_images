from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog
import os

print("Add Grid to Images - 28/06/2020")

root = tk.Tk()
root.withdraw()

gridDivisions = input("Grid divisions (default = 8): \n > ")
if gridDivisions == '':
	gridDivisions = 8

lineColor = input("Line Color (black/blue/red/green...): \n > ")
if lineColor == '':
	lineColor = 'black'

imagepath = filedialog.askopenfilename(title = "Select Source Image")
im = Image.open(imagepath)
filename = str(os.path.splitext(os.path.basename(imagepath))[0])

width = im.size[0]
height = im.size[1]
gridX = width/int(gridDivisions)
gridY = height/int(gridDivisions)

draw = ImageDraw.Draw(im) 

i = 1
while i < int(gridDivisions):
	draw.line([(gridX*i,0),(gridX*i,height)], fill=lineColor, width=4)
	draw.line([(0,gridY*i),(width,gridY*i)], fill=lineColor, width=4)
	i += 1 

savepath = filedialog.askdirectory(title = "Select Output Directory")

newfilename = filename + '_w_Grid'
im.save(savepath + "/" + newfilename + ".jpg", "JPEG")
print(newfilename + "_w_Grid.jpg Sucessfully saved!")

opendir = input("Open directory? (y/n) \n > ")
if opendir == 'y':
	path = savepath
	path = os.path.realpath(path)
	os.startfile(path)