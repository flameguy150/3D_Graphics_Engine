# In order to put anything on github, you want the following pattern
# git init once
# add ., commit, push


import tkinter as tk
import time

root = tk.Tk()
root.geometry('600x400')
root.title('Canvas Demo')

canvas = tk.Canvas(root, width=600, height=400, bg='black')

# trying to resize circle to center it when expanding window
# def resize_oval(circle2):
#     width = circle

# Don't use pack
#canvas.pack(anchor=tk.CENTER, expand=True)

# Use canvas.place if you wanna fill the whole window
# relx and rely changes the shape of the canvas window relative to the main window's INITIAL width and hight
# relwidth and relheight makes the canvas window follow the main window's relative width and height
canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

#creating a shape is create_shape(x coordinate, y coordinate,, fill=color) to make shape in window
# circle = canvas.create_oval(50, 50, 300, 300, fill="blue")

radius = 50
middle_w = 1/2 * int(canvas['width'])
middle_h = 1/2 * int(canvas['height'])

#seems right
print(middle_h)
print(middle_w)

#parameters of create_ovals (x1,y1) = top left point of box of circle, (x2, y2) = bottom right point of box of circle
crosshair = canvas.create_oval(middle_w - radius, middle_h - radius, middle_w + radius, middle_h + radius, fill="red", outline="blue", width="1")
# crosshair.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) does not work
print(canvas.coords(crosshair))

root.mainloop()

# for x in range(10):
#     time.sleep(0.2)
#     canvas.move(circle, 10, 10)


#Make the shape move
#