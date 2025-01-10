#stores all functions and classes so... files are cleaner 

from tkinter import *
import tkinter as tk
import numpy as np
from copy import deepcopy
import math
import time
i = 20

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

    
    def rotate(self, degree):
        radians = math.radians(degree)
        a = np.array([[math.cos(radians), -(math.sin(radians))], 
                     [math.sin(radians), math.cos(radians)]])
        self.vector = np.dot(a, self.vector)

    def rotate_x(self, degree):
        radians = math.radians(degree)
        a = np.array([[1, 0, 0], 
                      [0, math.cos(radians), -(math.sin(radians))], 
                      [0, math.sin(radians), math.cos(radians)]])
        self.vector = np.dot(a, self.vector)
    
    def rotate_y(self, degree):
        radians = math.radians(degree)
        a = np.array([[math.cos(radians), 0, math.sin(radians)], 
                      [0, 1, 0], 
                      [-(math.sin(radians)), 0, math.cos(radians)]])
        self.vector = np.dot(a, self.vector)
    

    def __repr__(self):
        vec = [int(x) for x in self.vector]
        return str(vec)





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

        self.points_current = [] # array of Points (the object guys we made that have rotate in them)
        self.plotted_points_list = [] # array of canvas.points (the little circles)
        self.xcoords = []
        self.ycoords = []
        self.connected_lines = [] # array of canvas lines (type sht)
        self.lines_current = [] # array of points to connect

        self.main_x2 = self.root.winfo_width()
        self.main_y2 = self.root.winfo_height()
        self.root.bind("<Configure>", self.resize_event)
        self.root.bind("<Button-1>", self.mouse_click_print)
        self.root.bind("<B1-Motion>", self.drag)


        self.old_click_coords_x = 0
        self.old_click_coords_y = 0
        self.new_click_coords_x = 0
        self.new_click_coords_y = 0

        self.running = False



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


    



    def plot_points2(self, point):

        x = point.vector[0]
        y = point.vector[1]

        width = (int(self['width']) / 2) + x*(int(self['width'])/20)
        height = (int(self['height']) / 2) - y*(int(self['height'])/10)

        radius = 5
        plotted_point = self.create_oval(width + radius, height + radius, width - radius, height - radius, fill="black", width="1", outline="")
        self.plotted_points_list.append(plotted_point) #do this bc we need to delete the canvas ovals later on
        self.points_current.append(point)#do this so we can redraw every Point object with their respective vectors
        self.xcoords.append(x)
        self.ycoords.append(y)
    
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
        self.calculate_middle()

        # We delete all the objects on the window
        self.delete(self.axis_x, self.axis_y)
        for tick in self.ticks:
            self.delete(tick) 
        self.delete_points()

        self.delete_lines()

        # Then we draw them back
        self.draw_axes()
        self.draw_ticks()
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
        print("diffx: " + str(diffx))
        print("diffy: " + str(diffy))
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



    def reset(self):
        pass#to reset object to initial state before draggin



    def auto_rotate(self): #maybe have it rotate after every time root updates?
        #we could bind this function to a key, like spacebar, so that if we continously press it down, it will continue to spin
        #and then we can have it so tkinter thinks its always pushed down?
        global i
        self.running = True
        while self.running:
            self.delete_points()
            self.plotted_points_list = []
            self.delete_lines()
            self.connected_lines = []


            for point in self.points_current:
                point.rotate_y(-(.1))
                # point.rotate_x(-(1))


            temp_points = my_deep_copy(self.points_current)
            self.points_current = []

            temp_lines = my_deep_copy(self.lines_current)
            self.lines_current = []

            for point in temp_points:
                self.plot_points2(point)
            
            for p1,p2 in temp_lines: #connect_lines needs two Point objs in argument, lines_current should be holding a tuple with the two points objects
                self.connect_lines(p1, p2)
            self.update()

        self.running = False


    def delete_points(self):
        for point in self.plotted_points_list:
            self.delete(point) # deleting all canvas ovals
        self.plotted_points_list = []
        

    def delete_lines(self):
        for line in self.connected_lines:
            self.delete(line)
        self.connected_lines = []




    def mouse_click_print(self, event):
        # print(event.x, event.y)
        self.old_click_coords_x = event.x
        self.old_click_coords_y = event.y





    #creating cube class
    def create_cube(self, x, y, size):
        p1 = Point( x+(1)*size, y+(1)*size, 1*size)
        p2 = Point( x+(1)*size, y+(1)*size, -1*size)
        p3 = Point( x+(1)*size, y+(-1)*size, 1*size)
        p4 = Point( x+(1)*size, y+(-1)*size, -1*size)
        p5 = Point( x+(-1)*size,y+( 1)*size, 1*size)
        p6 = Point( x+(-1)*size,y+( 1)*size, -1*size)
        p7 = Point( x+(-1)*size,y+( -1)*size, 1*size)
        p8 = Point( x+(-1)*size,y+( -1)*size, -1*size)

        cube_points = [p1, p2, p3, p4, p5, p6, p7, p8]
        for point in cube_points:
            self.plot_points2(point)

        edges = [(p1, p2), (p2, p6), (p6, p5), (p5, p1), 
                 (p1, p3), (p2, p4), (p6, p8), (p5, p7),
                 (p3, p4), (p4, p8), (p8, p7), (p7, p3)
                 ]
        for p1, p2 in edges:
            self.connect_lines(p1, p2)
        
    
    def create_octahedron(self,x, y, size): # should also have an argument to ctrl size
        p1 = Point(x+(0)*size, y + (1)*size, 0*size)
        p2 = Point(x+(1)*size, y + (0)*size, 0*size)
        p3 = Point(x+(0)*size, y + (0)*size, -1*size)
        p4 = Point(x+(-1)*size,y + (0) *size, 0*size)
        p5 = Point(x+(0)*size, y + (0)*size, 1*size)
        p6 = Point(x+(0)*size, y + (-1) *size, 0*size)

        octahedron_pts = [p1, p2, p3, p4, p5, p6]
        for pt in octahedron_pts:
            self.plot_points2(pt)
        
        edges = [(p1, p2), (p1, p3), (p1, p4), (p1, p5), 
                 (p6, p2), (p6, p3), (p6, p4), (p6, p5),
                 (p2, p3), (p3, p4), (p5, p4), (p5, p2)
        ]
        
        for p1, p2 in edges:
            self.connect_lines(p1, p2)

if (__name__ == "__main__"):


    x = Point(1,0,0)
    x.rotate_x(90)