import tkinter as tk
import time
import numpy as np

from Utilities import my_range, Canvas_2D, Point

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

#cube
p1 = Point(1, 1, 1)
p2 = Point(1, 1, -1)
p3 = Point(1, -1, 1)
p4 = Point(1, -1, -1)
p5 = Point(-1, 1, 1)
p6 = Point(-1, 1, -1)
p7 = Point(-1, -1, 1)
p8 = Point(-1, -1, -1)







canvas = Canvas_2D(root, 600, 400, 'DodgerBlue4')
canvas.draw_axes()
canvas.draw_ticks()


#choose size 1-10
# canvas.create_cube()
canvas.create_octahedron(4)





canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)




root.mainloop()

# for x in range(10):
#     time.sleep(0.2)
#     crosshair.move(crosshair, 10, 0)


#Make the shape move
#