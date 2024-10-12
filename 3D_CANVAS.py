# In order to put anything on github, you want the following pattern
# git init once
# add ., commit, push


import tkinter as tk
import time
import numpy as np

from Utilities import my_range, plot, Canvas_2D

"""
Define a function called plot(x,y) that takes a pair of coordinates x, y and 
plot it on the canvas.

If you plot(0,0), there should be a small circle in the origin.
If you plot (1, 1), it should be on the corresponding space on a grid.

"""

root = tk.Tk()
root.geometry('600x400')
root.title('3D Engine')


root.minsize(600, 400)
root.maxsize(1536, 864)


# root.attributes("-toolwindow", True)

#need to resize canvas so it fits with window size
#get new coordinates of window by winfo_screenwidth() and winfo_screenheight()

points = []

canvas = Canvas_2D(root, 600, 400, 'DodgerBlue4')
canvas.draw_axes()
canvas.draw_ticks()
canvas.plot_points(0, 0)
canvas.plot_points(-1, -1)
canvas.plot_points(1, 1)



# plot(canvas, 0, 0) 

#gridpoints
# ticks = []
# # tecks = []
# for x in range (int(-middle_w), int(middle_w) + 1, 50):
#     ticks.append(canvas.create_line(middle_w + x, int(canvas['height'])/2, middle_w + x + 1, int(canvas['height'])/2, width=10, fill="white")) 
#     # tecks.append(canvas.create_text(middle_w + x, int(canvas['height'])/2 + 10, text=str(x)))
# for y in range (int(-middle_h), int(middle_h) + 1, 50):
#     ticks.append(canvas.create_line(int(canvas['width'])/2, middle_h + y, int(canvas['width'])/2, middle_h + y + 1, width=10, fill="white")) 
#     # tecks.append(canvas.create_text(int(canvas['width'])/2 + 10, middle_h + y, text=str(y), fill="white"))



# points = []


# def can_resize(event):
#     global crosshair
#     global axis_x
#     global axis_y
#     global ticks
#     global points
    
#     canvas.config(width=root.winfo_width(), height=root.winfo_height())
#     canvas.delete(crosshair)
#     crosshair = canvas.create_oval(int(canvas['width'])/2 - radius, 
#                                     int(canvas['height'])/2 - radius, 
#                                     int(canvas['width'])/2 + radius, 
#                                     int(canvas['height'])/2 + radius, 
#                                     fill="DodgerBlue4", outline="red", width="1")
    
#     canvas.delete(axis_x, axis_y)
#     axis_x = canvas.create_line(main_x1, int(canvas['height'])/2, 
#                                 canvas['width'], 
#                                 int(canvas['height'])/2,
#                                 fill="black")
#                                 #, arrow=tk.LAST)
#     axis_y = canvas.create_line(int(canvas['width'])/2,
#                                 main_y1,
#                                 int(canvas['width'])/2,
#                                 canvas['height'],
#                                 fill="black")
#                                 #, arrow=tk.LAST)
#     # canvas.delete(originxx)
#     # originxx = canvas.create_text(int(canvas['width']/2) + 5, int(canvas['height']/2) + 5, text="O")

#     #delete all gridpoints and text
#     for tick in ticks:
#         canvas.delete(tick)
#     # for teck in tecks:       
#     #     canvas.delete(teck)

    
#     for point in points:
#         canvas.delete(point)

#     x_ticks = 20
#     increments_x = int(canvas['width'])/x_ticks

#     y_ticks = 10
#     increments_y = int(canvas['height'])/y_ticks


    

#     x_coordinates = my_range(0, int(canvas['width']), increments_x)
#     y_coordinates = my_range(0, int(canvas['height']), increments_y)

#     for x in x_coordinates:
#         ticks.append(canvas.create_line(x, int(canvas['height'])/2,  x + 1, int(canvas['height'])/2, width=10, fill="white")) 
#     for y in y_coordinates:
#         ticks.append(canvas.create_line(int(canvas['width'])/2, y, int(canvas['width'])/2, y + 1, width=10, fill="white")) 

#     points = []
    
#     point1 = plot(points, canvas, 0, 0) 
#     point2 = plot(points, canvas, 1, 1) 
#     point3 = plot(points, canvas, 6, 0)
#     point4 = plot(points, canvas, 0, 4)
#     point5 = plot(points, canvas, 8, -4)
#     point6 = plot(points, canvas, -4, -2)

# root.bind("<Configure>", can_resize)


#create_line multiple times with for loop
#just need to change x1 and x2 to shift
#good width for lines is 10, distance for x1 and x2 should be about 2

# gridpoint = canvas.create_line(0, int(canvas['height'])/2, 2, int(canvas['height'])/2, width=10, fill="green")
# gridpoint = canvas.create_line(10, int(canvas['height'])/2, 12, int(canvas['height'])/2, width=10, fill="green")
# gridpoint = canvas.create_line(20, int(canvas['height'])/2, 22, int(canvas['height'])/2, width=10, fill="green")

  

# def mouse_print(event):
#     print(event.x, event.y)

# root.bind("<Button-1>", mouse_print)



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



#parameters of create_ovals (x1,y1) = top left point of box of circle, (x2, y2) = bottom right point of box of circle
# crosshair.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) does not work
# print(canvas.coords(crosshair))





root.mainloop()

# for x in range(10):
#     time.sleep(0.2)
#     crosshair.move(crosshair, 10, 0)


#Make the shape move
#