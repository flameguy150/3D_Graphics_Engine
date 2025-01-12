import tkinter as tk
import time
import numpy as np # py -m pip install (wtv package)
from pygame import mixer
import random



from Utilities import my_range, Canvas_2D, Point, beautiful_colors
from colors import colors

"""
Define a function called plot(x,y) that takes a pair of coordinates x, y and 
plot it on the canvas.

If you plot(0,0), there should be a small circle in the origin.
If you plot (1, 1), it should be on the corresponding space on a grid.

"""

root = tk.Tk()
root.geometry('600x400')


root.title('3D Engine')

#transparency

# makes overall window transparent
# root.attributes("-alpha", 0.5) 

#removes titlebar and close buttons
# root.overrideredirect(True) 

# brings window to top of the window stack
# root.lift() 

#ensures window stays on top all of other windows
# root.wm_attributes("-topmost", True) 

#disabes user interaction w window
# root.wm_attributes("-disabled", True) 

#any part of the window w the specific color becomes transparent
root.wm_attributes("-transparentcolor", "snow") 




root.minsize(600, 400)
root.maxsize(1536, 864)
# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("piano_soundtrack_-_isolation.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.7) 
  
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
bg2 = random.choice(beautiful_colors)

canvas = Canvas_2D(root, 600, 400, 'white')
canvas.draw_axes()
canvas.draw_ticks()





# #choose size 1-10
canvas.create_cube(0, 0, 3)
# canvas.create_octahedron(3, 3, 8)
# canvas.create_triprism(0,0,7)
# canvas.create_triprism(1,0,7)
# canvas.create_cube(0, 0, 3)

canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

# for i in range(9): #fun

#     canvas.create_triprism(i, i, random.uniform(1,9))
#     canvas.create_triprism(-i, -i, random.uniform(1,9))

# canvas.create_star(0,0,1)

#create object class for the auto rotate, put all these objects into it ig

"""

experimentation time!

"""
# color_button = tk.Button(root, text="Good color!", command=lambda: canvas.append_color(canvas.color))
# color_button.pack(side='top')
# switch_color_button = tk.Button(root, text="Different bg color!", command=lambda: canvas.switch_bg_color())
# switch_color_button.pack(side='top')




# canvas.auto_rotate(x=0, y=0, speed = .2, left=1) #type x to rotate x axis, type y to rotate y axis
#also speed argument
#command=lambda : btn1click()
# start_rotate_bt = tk.Button(root, text="Start rotation", activebackground="white", command=lambda: canvas.auto_rotate(x=0, y=0, left=1))
# start_rotate_bt.pack(side="left")
# stop_rotate_bt = tk.Button(root, text="Stop rotation", activebackground="white", command=lambda: canvas.stop_rotate())
# stop_rotate_bt.pack(side="right")
# initial_state_bt = tk.Button(root, text="Reset", activebackground="white", command=lambda: canvas.initial_state())
# initial_state_bt.pack(side="bottom")

# incspeed_bt = tk.Button(root, text="+ speed", command=lambda: canvas.increase_rotate_speed())
# incspeed_bt.pack(side="left")
# decspeed_bt = tk.Button(root, text="- speed", command=lambda: canvas.decrease_rotate_speed())
# decspeed_bt.pack(side="left")

# hide_cplane_bt = tk.Button(root, text="hide coordinate plane", command=lambda: canvas.hide_cordplane())
# hide_cplane_bt.pack(side="top")


# color_button = canvas.create_button(root, "Good color!", canvas.append_color(canvas.color), 'top', False)

hide_btns = canvas.create_button(root, "☰", lambda: canvas.hide_buttons(), 'top', 'nw', False)

glitch_bt = canvas.create_button(root, "glitch", lambda: canvas.glitch_effect(), 'top', 'nw', False)


switch_color_button = canvas.create_button(root, "Different bg color!", lambda: canvas.switch_bg_color(), 'top', 'nw', False)


start_rotate_bt = canvas.create_button(root, "Start rotation", lambda: canvas.auto_rotate(x=1, y=1, right=1), 'top', 'nw', False)

stop_rotate_bt = canvas.create_button(root, "Stop rotation", lambda: canvas.stop_rotate(),'top', 'nw', False)

initial_state_bt = canvas.create_button( root, "Reset", lambda: canvas.initial_state(), 'top', 'nw', False)


#user slider widget for speed
incspeed_bt = canvas.create_button(root, "+ speed", lambda: canvas.increase_rotate_speed(), 'top', 'nw', True)

decspeed_bt = canvas.create_button(root, "- speed", lambda: canvas.decrease_rotate_speed(), 'top', 'nw', True)


hide_cplane_bt = canvas.create_button(root, "hide coordinate plane", lambda: canvas.hide_cordplane(), 'top', 'nw', False)









# canvas.update()



root.mainloop()
