import tkinter as tk
import time
import numpy as np # py -m pip install (wtv package)
from pygame import mixer
import random



from Utilities import my_range, Canvas_2D, Point
from colors import colors, beautiful_colors

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
# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("piano_soundtrack_-_isolation.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.75) 
  
# Start playing the song 
mixer.music.play(-1, 0.0) 


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




bg = random.choice(colors)

canvas = Canvas_2D(root, 600, 400, bg)
# canvas.draw_axes()
# canvas.draw_ticks()

# button = tk.Button(root, text="Good color!", activebackground="black", anchor="n", command = canvas.append_color())

# #choose size 1-10
canvas.create_cube(-2, -2, 6)
canvas.create_octahedron(3, 3, 8)
canvas.create_triprism(0,0,7)
canvas.create_triprism(1,0,7)
canvas.create_cube(0, 0, 3)



# for i in range(9): #fun

#     canvas.create_triprism(i, i, random.uniform(1,9))
#     canvas.create_triprism(-i, -i, random.uniform(1,9))

# canvas.create_star(0,0,1)

#create object class for the auto rotate, put all these objects into it ig

"""

Infinite Terrain Generation

"""

# canvas.terrain_grid()

canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

canvas.auto_rotate(x=0, y=0, speed = .2, left=1) #type x to rotate x axis, type y to rotate y axis
#also speed argument

# canvas.update()



root.mainloop()
