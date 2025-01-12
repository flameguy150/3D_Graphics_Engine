#stores all functions and classes so... files are cleaner 

from tkinter import *
import tkinter as tk
import numpy as np
from copy import deepcopy
import math
import time
import random
import os
from pygame import mixer

# Access utilities.py
colors = os.path.join("tkinter_sound_colors", "colors.py")

song1 = os.path.join("tkinter_sound_colors", "piano_soundtrack_-_isolation.mp3")
song2 = os.path.join("tkinter_sound_colors", "lofi_replus.mp3")

music = [song1, song2]

# Starting the mixer 
mixer.init() 





beautiful_colors = ['snow', 'white', 'lavender', 'steel blue', 'ivory2', 'indian red', 'dark sea green', 'MediumOrchid1', 'SkyBlue4']

i = 20
rradians_x = 0
rradians_y = 0

"""
PYTHON FUNCS
"""
def my_range(start, end, increment):
    current_value = start
    values = []
    while current_value < end:
        values.append(current_value)
        current_value += increment
    
    return values

def infinite_range(start):
    current_value = start
    values=[]
    while True:
        values.append(current_value)
    return values


def my_deep_copy(array):
    deep_array = []
    for point in array:
        deep_array.append(point)
    return deep_array
    # return [x for x in array] #John Leung's deepcopy do not steal

"""
PYTHON FUNCS
"""


class Point():
    def __init__(self, x, y, z):
        self.canvas_point_id = None
        self.x_ = x
        self.y = y
        self.z = z
        self.vector = np.array([x, y, z]).transpose()

        self.originalpts = []
        self.currentpts = []

        # self.radians = 0

    
    def rotate(self, degree):
        radians = math.radians(degree)
        a = np.array([[math.cos(radians), -(math.sin(radians))], 
                     [math.sin(radians), math.cos(radians)]])
        self.vector = np.dot(a, self.vector)
        
        # print(self.currentpts)
        # print(radians)


    def rotate_x(self, degree):
        global rradians_x

        radians = math.radians(degree)
        a = np.array([[1, 0, 0], 
                      [0, math.cos(radians), -(math.sin(radians))], 
                      [0, math.sin(radians), math.cos(radians)]])
        self.vector = np.dot(a, self.vector)
        self.currentpts = self.vector.tolist()
        # print(self.currentpts)
        # print(radians)
        rradians_x += degree

    
    def rotate_y(self, degree):
        global rradians_y
        
        radians = math.radians(degree)
        a = np.array([[math.cos(radians), 0, math.sin(radians)], 
                      [0, 1, 0], 
                      [-(math.sin(radians)), 0, math.cos(radians)]])
        self.vector = np.dot(a, self.vector)
        self.currentpts = self.vector.tolist()
        rradians_y += degree
    

    def __repr__(self):
        vec = [int(x) for x in self.vector]
        return str(vec)

# class Buttons():
    # def __init__(self, root, text, command, location):
    #     tk.Button.__init__(self, master = root)
    #     self.root = root
    #     self.text = text
    #     self.command = command
    #     self.location = location
        
        
    
    # def create_button(self, root2, text2, command2, location2, bind = None):
    #     button_ = tk.Button(root2, text = text2, command=command2)
    #     button_.pack(side = location2)
    #     if bind != None:
    #         self.bind('<ButtonPress-1>', self.start)
    #         self.bind('<ButtonRelease-1>', self.stop)

    # def start(self, event=None):
    #     if self.command is not None:
    #         self.command()
    #         if self.timeout is not None:
    #             self.timer = self.after(self.timeout, self.start)

    # def stop(self, event=None):
    #     self.after_cancel(self.timer)
    




class Canvas_2D(Canvas):
    def __init__(self, root, width, height, bg):
        # Initializer for our own Canvas. We have to call the parent class before
        # adding any variables

        Canvas.__init__(self, master = root, width = width, height = height, bg = bg)        
        self.root = root
        self.middle_w = 1/2 * int(self['width'])
        self.middle_h = 1/2 * int(self['height'])
        self.ticks = []
        self.axis_x = 0
        self.axis_y = 0
        self.color = bg

        self.points_current = [] # array of Points (the object guys we made that have rotate in them)
        self.plotted_points_list = [] # array of canvas.points (the little circles)
        self.connected_lines = [] # array of canvas lines (type sht)
        self.lines_current = [] # array of points to connect

        self.buttons = [] #all buttons to hide and reshow
        self.button_packs = [] # to reshow all buttons with proper locations
        self.button_anchors = []

        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.root.bind("<Configure>", self.resize_event)
        self.root.bind("<Button-1>", self.mouse_click_print)
        self.root.bind("<B1-Motion>", self.drag)


        self.old_click_coords_x = 0
        self.old_click_coords_y = 0
        self.new_click_coords_x = 0
        self.new_click_coords_y = 0

        self.running = False
        self.rotspeed = .3

        self.ticks_drawn = False
        self.axis_drawn = False

        self.btns_hidden = False

        self.glitching = False

        self.current_song = song1
        self.muted = False



        self.switch_music()
        

        self.print_color()
        

    def mouse_click_print(self, event):
        # print(event.x, event.y)
        self.old_click_coords_x = event.x
        self.old_click_coords_y = event.y



    def my_create_rectangle(self, x1, y1, x2, y2, outline, bg, width):#dont really need this lol
        # pass #create rectangle
        self.create_rectangle(x1, y1, x2, y2, outline= outline, fill=bg, width = width)



    def calculate_middle(self):
        # Calculate the coordinates of the middle of the Canvas.
        # We end up using this to help us place our axes and tick marks,
        # as well as plot our points
        self.middle_w = 1/2 * int(self["width"])
        self.middle_h = 1/2 * int(self["height"])

    def draw_axes(self):
        # Draw the two axes
        self.axis_x = self.create_line(0, self.middle_h, self['width'], self.middle_h, fill="white")
        self.axis_y = self.create_line(self.middle_w, 0, self.middle_w, self['height'], fill="white")
        self.axis_drawn = True

    def draw_ticks(self):
        # Draw tick marks on the axes of the Canvas

        self.ticks = []
        x_ticks = 20
        increments_x = int(self['width'])/x_ticks
        y_ticks = 10
        increments_y = int(self['height'])/y_ticks

        x_coordinates = my_range(0, int(self['width']), increments_x)
        y_coordinates = my_range(0, int(self['height']), increments_y)
        
        for x in x_coordinates:
            self.ticks.append(self.create_line(x, int(self['height'])/2,  x + 1, int(self['height'])/2, width=10, fill="white")) 
        for y in y_coordinates:
            self.ticks.append(self.create_line(int(self['width'])/2, y, int(self['width'])/2, y + 1, width=10, fill="white")) 
        
        self.ticks_drawn = True


    



    def plot_points2(self, point):

        x = point.vector[0]
        y = point.vector[1]

        width = (int(self['width']) / 2) + x*(int(self['width'])/20)
        height = (int(self['height']) / 2) - y*(int(self['height'])/10)

        radius = 5
        plotted_point = self.create_oval(width + radius, height + radius, width - radius, height - radius, fill="black", width="1", outline="")
        point.originalpts = point.vector.tolist()
        self.plotted_points_list.append(plotted_point) #do this bc we need to delete the canvas ovals later on
        self.points_current.append(point)#do this so we can redraw every Point object with their respective vectors
        
        # print(point.originalpts)
        
    
    #connecting lines of shape objects
    #need to make it resized with window and rotate with shape/points
    def connect_lines(self, point1, point2):
        # middle_width = self.middle_w = 1/2 * int(self['width'])
        # middle_height = self.middle_h = 1/2 * int(self['width'])
        x1 = point1.vector[0]
        y1 = point1.vector[1]
        x2 = point2.vector[0]
        y2 = point2.vector[1]
       
        width1 = self.middle_w + x1*(int(self["width"])/20)
        height1 = self.middle_h - y1*(int(self["height"])/10)
        width2 = self.middle_w + x2*(int(self["width"])/20)
        height2 = self.middle_h - y2*(int(self["height"])/10)

        line = self.create_line(width1, height1, width2, height2, fill="black")
        self.connected_lines.append(line)
        self.lines_current.append((point1, point2)) #  array of points to connect

    






    def resize_event(self, event):
        # Call this every time we resize the window. 

        self.config(width=self.root.winfo_width(), height=self.root.winfo_height())
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        
        self.calculate_middle()

        self.delete_axis()
        self.delete_ticks()

        if self.axis_drawn == True: #we redraw
            self.draw_axes()
            self.draw_ticks()
        elif self.axis_drawn == False:
            self.axis_drawn = False
            self.ticks_drawn = False

        # We delete all the objects on the window
        
        self.delete_points()

        self.delete_lines()

        # Then we draw them back
        self.redraw_points()
        self.redraw_lines()


    def redraw_points(self):

        temp_points = my_deep_copy(self.points_current)
        self.points_current = []

        for i in range(len(temp_points)):     
            self.plot_points2(temp_points[i])


        self.points_current = temp_points

    def redraw_lines(self):
        temp_lines = my_deep_copy(self.lines_current)
        self.lines_current = []
        
        
        for i in range(len(temp_lines)):     
            self.connect_lines(temp_lines[i][0], temp_lines[i][1])
    


        self.lines_current = temp_lines



    def drag(self, event):

        # old_mouse_click_x = event.x
        # new_mouse_click_x = event.x
        
        self.new_click_coords_x = event.x
        self.new_click_coords_y = event.y

        # Calculate the difference between the old drag_x and now_x
        diffx = self.new_click_coords_x - self.old_click_coords_x
        diffy = self.new_click_coords_y - self.old_click_coords_y
        # print("diffx: " + str(diffx))
        # print("diffy: " + str(diffy))
        self.old_click_coords_x = event.x
        self.old_click_coords_y = event.y
        
        # call rotate on every point in points list by that many (negative) degrees

        #delete every point and lines
        self.delete_points()
        self.plotted_points_list = []
        

        self.delete_lines()
        self.connected_lines = []

        #rotate
        for point in self.points_current:
            point.rotate_y(-(diffx))
            point.rotate_x(-(diffy))


        #deepcopy so that the list doesnt expand forever
        temp_points = my_deep_copy(self.points_current)
        self.points_current = []

        temp_lines = my_deep_copy(self.lines_current)
        self.lines_current = []


        for point in temp_points:
            self.plot_points2(point)
        
        for p1,p2 in temp_lines: #connect_lines needs two Point objs in argument, lines_current should be holding a tuple with the two points objects
            self.connect_lines(p1, p2)



        """
        BUTTONS BUTTONS   BUTTONS   BUTTONS BUTTON BUTTONS BUTTONS

        """
    
    def hide_buttons(self):
        if self.btns_hidden: #buttons are hidden, we redraw bts
            for button in self.buttons: 
                if button.cget("text") != "☰":
                    for pack2 in self.button_packs:
                        for anchor in self.button_anchors:
                            button.pack(side = pack2, anchor = anchor)
            self.btns_hidden = False

        else: #if buttns are shown, we hide
            for button in self.buttons:
                if button.cget("text") != "☰":
                    button.pack_forget() #forgets the pack of btns, does not delete btn
            self.btns_hidden = True


    def hide_cordplane(self):
        if self.axis_drawn == True and self.ticks_drawn == True:
            self.delete_axis()
            self.axis_drawn = False
            self.delete_ticks()
            self.ticks_drawn = False
        else:
            self.draw_axes()
            self.draw_ticks()

    def create_button(self, root2, text2, command2, location2, anchor, bind):
        button_ = tk.Button(root2, text = text2, command=command2)
        button_.pack(side = location2, anchor=anchor)
        # if bind != None:
        #     button_.bind('<ButtonPress-1>',self.start_press)
        #     button_.bind('<ButtonRelease-1>',self.stop_press)
        self.update()
        if button_.cget("text") != "☰":
            self.button_packs.append(location2)
            self.button_anchors.append(anchor)
        self.buttons.append(button_)
    
    def start_press(self, event):
        self.button_running = True
        while self.button_running == True:
            self.after(self.interval, self.start_press)

    def stop_press(self, event):
        self.button_running = False


    def print_color(self):
        print(self.color)
        

    def random_color(self):
        global beautiful_colors
        size = len(beautiful_colors)
        if size == 0:
            beautiful_colors = ['lavender', 'steel blue', 'ivory2', 'indian red', 'dark sea green', 'MediumOrchid1', 'SkyBlue4']
        
        new_color = random.choice(beautiful_colors)
        beautiful_colors.remove(new_color)
        return new_color


    def append_color(self, color):
        global beautiful_colors
        if color not in beautiful_colors:
            beautiful_colors.append(self.color)
            print("appending " + self.color + "!")
        else:
            print("already in list!")
    

    def switch_bg_color(self):
        #self.config(width=self.root.winfo_width(), height=self.root.winfo_height())
        #random.uniform(colors)
        new_color = self.random_color()
        self.config(bg = new_color)
        self.color = new_color
        self.print_color()

    def pause_music(self):
        if self.muted == False:
            mixer.music.pause()
            self.muted = True
        else:
            mixer.music.unpause()
            self.muted = False

    def switch_music(self):
        # Loading the song 
        
        for song in music:
            if self.current_song == song:
                music.remove(song)#delete it temp so we dont play same song
                randomsong = random.choice(music)
                self.current_song = randomsong
                mixer.music.load(randomsong) 
                music.append(song)#add it back
        
        # Setting the volume 
        mixer.music.set_volume(0.7) 
        
        # Start playing the song 
        mixer.music.play(-1, 0.0) 


    def glitch_effect(self):
        if self.glitching == False:
            self.glitching = True
        else:
            self.glitching = False

    def auto_rotate(self, x =None, y =None, left = None, right = None): #maybe have it rotate after every time root updates?
        #we could bind this function to a key, like spacebar, so that if we continously press it down, it will continue to spin
        #and then we can have it so tkinter thinks its always pushed down?
        global i
        self.running = True


        while self.running:
            self.delete_points()
            self.plotted_points_list = []
            self.delete_lines()
            self.connected_lines = []

            if self.glitching == True: #if glitch btn is pressed 
                    self.update()
            
            if left == None:  #turn right
                if y == None: #rotate around y axis
                    for point in self.points_current:
                        point.rotate_y(-(self.rotspeed))#turn right

                elif x == None: #rotate around x axis
                    for point in self.points_current:
                        point.rotate_x(-(self.rotspeed))#turn right
                        print("hello")

                else: #rotate around both
                    for point in self.points_current:
                        point.rotate_y(-(self.rotspeed))
                        point.rotate_x(-(self.rotspeed)) #right
                        #self.update() #VERY COOL GLITCHY EFFECT
                        print(self.rotspeed)
            elif right == None:
                if y == None: #rotate around y axis
                    for point in self.points_current:
                        point.rotate_y(-(-self.rotspeed))#turn left

                elif x == None: #rotate around x axis
                    for point in self.points_current:
                        point.rotate_x(-(-self.rotspeed))#turn left

                else: #rotate around both
                    for point in self.points_current:
                        point.rotate_y(-(-self.rotspeed))
                        point.rotate_x(-(-self.rotspeed)) #left
            

                       
            
                

            temp_points = my_deep_copy(self.points_current)
            self.points_current = []

            temp_lines = my_deep_copy(self.lines_current)
            self.lines_current = []
            
            for point in temp_points:
                self.plot_points2(point)
            
            for p1,p2 in temp_lines: #connect_lines needs two Point objs in argument, lines_current should be holding a tuple with the two points objects
                self.connect_lines(p1, p2)
            # time.sleep(.01)
            self.update()
            # self.update_idletasks()
    def increase_rotate_speed(self):
        self.rotspeed += .05

    def decrease_rotate_speed(self):
        self.rotspeed -= .05

    def stop_rotate(self):
        self.running = False
        self.update()
        

    def initial_state(self):#need2complete
        global rradians_x
        global rradians_y
        #i would have to store the initial state of the points, 
        #then find the current state and find the diff = current-initial
        #FINALLY rotate the points by that much

        for point in self.points_current:
            diff_x = rradians_x
            diff_y = rradians_y
            point.rotate_x(-(diff_x))
            point.rotate_y(-(diff_y))
            print("ogogogo")
        
        rradians_x = 0
        rradians_y = 0


        self.update()



        """
        BUTTONS BUTTONS   BUTTONS   BUTTONS BUTTON BUTTONS BUTTONS
        
        """



    def delete_points(self):
        for point in self.plotted_points_list:
            self.delete(point) # deleting all canvas ovals
        self.plotted_points_list = []
        

    def delete_lines(self):
        for line in self.connected_lines:
            self.delete(line)
        self.connected_lines = []

    def delete_axis(self):
        self.delete(self.axis_x, self.axis_y)

    def delete_ticks(self):
        for tick in self.ticks:
            self.delete(tick) 




    #creating cube class
    def create_cube(self, x, y, size):
        p1 = Point( x+(1)*size, y+(1)*size, 1*size)
        p2 = Point( x+(1)*size, y+(1)*size, -1*size)
        p3 = Point( x+(1)*size, y+(-1)*size, 1*size)
        p4 = Point( x+(1)*size, y+(-1)*size, -1*size)
        p5 = Point( x+(-1)*size, y+( 1)*size, 1*size)
        p6 = Point( x+(-1)*size, y+( 1)*size, -1*size)
        p7 = Point( x+(-1)*size, y+( -1)*size, 1*size)
        p8 = Point( x+(-1)*size, y+( -1)*size, -1*size)

        cube_points = [p1, p2, p3, p4, p5, p6, p7, p8]
        for point in cube_points:
            point.originalpts.append(point)
            self.plot_points2(point)

        edges = [(p1, p2), (p2, p6), (p6, p5), (p5, p1), 
                 (p1, p3), (p2, p4), (p6, p8), (p5, p7),
                 (p3, p4), (p4, p8), (p8, p7), (p7, p3)
                 ]
        for p1, p2 in edges:
            self.connect_lines(p1, p2)
        
    
    def create_octahedron(self, x, y, size): # should also have an argument to ctrl size
        p1 = Point(x+(0)*size, y + (1)*size, 0*size)
        p2 = Point(x+(1)*size, y + (0)*size, 0*size)
        p3 = Point(x+(0)*size, y + (0)*size, -1*size)
        p4 = Point(x+(-1)*size,y + (0) *size, 0*size)
        p5 = Point(x+(0)*size, y + (0)*size, 1*size)
        p6 = Point(x+(0)*size, y + (-1) *size, 0*size)

        octahedron_pts = [p1, p2, p3, p4, p5, p6]
        for pt in octahedron_pts:
            pt.originalpts.append(pt)
            self.plot_points2(pt)
        
        edges = [(p1, p2), (p1, p3), (p1, p4), (p1, p5), 
                 (p6, p2), (p6, p3), (p6, p4), (p6, p5),
                 (p2, p3), (p3, p4), (p5, p4), (p5, p2)
        ]
        
        for p1, p2 in edges:
            self.connect_lines(p1, p2)
    
    def create_triprism(self, x, y, size):
        p1 = Point(x+(0)*size, y + (1)*size, (-1)*size)
        p2 = Point(x+(-1)*size, y + (0)*size, (-1)*size)
        p3 = Point(x+(1)*size, y + (0)*size, (-1)*size)
        p4 = Point(x+(0)*size, y + (1)*size, (1)*size)
        p5 = Point(x+(-1)*size, y + (0)*size, (1)*size)
        p6 = Point(x+(1)*size, y + (0)*size, (1)*size)

        triprism_pts = [p1, p2, p3, p4, p5, p6]
        for pt in triprism_pts:
            pt.originalpts.append(pt)
            self.plot_points2(pt)
        
        edges = [(p1, p2), (p2, p3), (p3, p1), 
                 (p1, p4), (p2, p5), (p3, p6),
                 (p4, p5), (p5, p6), (p6, p4)
        ]
        for p1, p2 in edges:
            self.connect_lines(p1, p2)

    
    def create_star(self, x, y, size):
        p1 = Point(x+(0)*size, y + (2)*size, (0)*size)
        p2 = Point(x+(-.75)*size, y + (.75)*size, (0)*size)
        p3 = Point(x+(-2)*size, y + (0)*size, (0)*size)
        p4 = Point(x+(-1)*size, y + (-.5)*size, (0)*size)
        p5 = Point(x+(-1.2)*size, y + (-2)*size, (0)*size)
        p6 = Point(x+(0)*size, y + (-1)*size, (0)*size)
        p7 = Point(x+(1.2)*size, y + (-2)*size, (0)*size)
        p8 = Point(x+(1)*size, y + (-.5)*size, (0)*size)
        p9 = Point(x+(2)*size, y + (0)*size, (0)*size)
        p10 = Point(x+(.75)*size, y + (.75)*size, (0)*size)


        # p11 = Point(x+(-.2)*size, y + (.5)*size, (0)*size)
        # p12 = Point(x+(.2)*size, y + (.5)*size, (0)*size)
        # p13 = Point(x+(-.6)*size, y + (0)*size, (0)*size)
        # p14 = Point(x+(-.3)*size, y + (-.3)*size, (0)*size)
        # p15 = Point(x+(0)*size, y + (-.4)*size, (0)*size)
        # p16 = Point(x+(.3)*size, y + (-.3)*size, (0)*size)
        # p17 = Point(x+(.6)*size, y + (0)*size, (0)*size)
        
        

        octahedron_pts = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10,
                        #    p11, p12, p13, p14, p15, p16, p17
                        ]
        for pt in octahedron_pts:
            pt.originalpts.append(pt)
            self.plot_points2(pt)
            
        
        edges = [(p1, p2), (p2, p3), (p3, p4), 
                 (p4, p5), (p5, p6), (p6, p7),
                 (p7, p8), (p8, p9), (p9, p10),
                 (p10, p1)
        ]
        for p1, p2 in edges:
            self.connect_lines(p1, p2)


                


if (__name__ == "__main__"):


    x = Point(1,0,0)
    x.rotate_x(90)