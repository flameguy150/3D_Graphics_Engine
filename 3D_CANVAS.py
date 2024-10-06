# In order to put anything on github, you want the following pattern
# git init once
# add ., commit, push


import tkinter as tk
import time

root = tk.Tk()
root.geometry('600x400')
root.title('3D Engine')
# root.attributes("-toolwindow", True)

#need to resize canvas so it fits with window size
#get new coordinates of window by winfo_screenwidth() and winfo_screenheight()

canvas = tk.Canvas(root, width=600, height=400, bg='black')

radius = 50
middle_w = 1/2 * int(canvas['width'])
middle_h = 1/2 * int(canvas['height'])

main_x1 = 0
main_y1 = 0
main_x2 = root.winfo_width()
main_y2 = root.winfo_height()

can_width = canvas.winfo_width()
can_height = canvas.winfo_height()
crosshair = canvas.create_oval(middle_w - radius, middle_h - radius, middle_w + radius, middle_h + radius, fill="red", outline="blue", width="1")

axis_x = canvas.create_line(main_x1, middle_h, canvas['width'], middle_h, fill="white")
axis_y = canvas.create_line(middle_w, main_y1, middle_w, canvas['height'], fill="white")


def can_resize(event):
    # new_w = root.winfo_screenwidth()
    # new_h = root.winfo_screenheight()
    # can_width = new_w
    # can_height = new_h
    global crosshair
    global axis_x
    global axis_y
    print(root.winfo_width(), root.winfo_height())
    canvas.config(width=root.winfo_width(), height=root.winfo_height())
    canvas.delete(crosshair)
    crosshair = canvas.create_oval(int(canvas['width'])/2 - radius, 
                                    int(canvas['height'])/2 - radius, 
                                    int(canvas['width'])/2 + radius, 
                                    int(canvas['height'])/2 + radius, 
                                    fill="red", outline="blue", width="1")
    
    canvas.delete(axis_x, axis_y)
    axis_x = canvas.create_line(main_x1, int(canvas['height'])/2 , canvas['width'], int(canvas['height'])/2, fill="white")
    axis_y = canvas.create_line(int(canvas['width'])/2 , main_y1, int(canvas['width'])/2 , canvas['height'], fill="white")

root.bind("<Configure>", can_resize)


#create_line multiple times


def mouse_print(event):
    print(event.x, event.y)

root.bind("<Button-1>", mouse_print)





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


#seems right
print(middle_h)
print(middle_w)
print(can_width)
print(can_height)

#parameters of create_ovals (x1,y1) = top left point of box of circle, (x2, y2) = bottom right point of box of circle
# crosshair.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) does not work
# print(canvas.coords(crosshair))





root.mainloop()

# for x in range(10):
#     time.sleep(0.2)
#     crosshair.move(crosshair, 10, 0)


#Make the shape move
#