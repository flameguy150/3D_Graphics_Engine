#stores all functions and classes so... files are cleaner 

from tkinter import *
import tkinter as tk
import numpy as np
from copy import deepcopy
import math

def my_range(start, end, increment):
    current_value = start
    values = []
    while current_value < end:
        values.append(current_value)
        current_value += increment
    
    return values


def my_deep_copy(array):
    deep_array = []
    for point in array:
        deep_array.append(point)
    return deep_array
    # return [x for x in array] #John Leung's deepcopy do not steal


class Point():
    def __init__(self, x, y, z):
        self.canvas_point_id = None
        self.x_point = x
        self.y_point = y
        self.z_point = z
        #self.z_point = z
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
    
    # def rotate_z(self, degree):
    #     radians = math.radians(degree)
    #     a = np.array([[math.cos(radians), -(math.sin(radians)), 0], 
    #                   [math.sin(radians), math.cos(radians), 0], 
    #                   [-(math.sin(radians)), 0, math.cos(radians)]])
    #     self.vector = np.dot(a, self.vector)

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

        self.points_current = []
        self.plotted_points_list = []
        self.xcoords = []
        self.ycoords = []


        self.main_x2 = self.root.winfo_width()
        self.main_y2 = self.root.winfo_height()
        self.root.bind("<Configure>", self.resize_event)
        self.root.bind("<Button-1>", self.mouse_click_print)
        self.root.bind("<B1-Motion>", self.drag)


        self.old_click_coords_x = 0
        self.old_click_coords_y = 0
        self.new_click_coords_x = 0
        self.new_click_coords_y = 0

    def resize_event(self, event):
        # Call this every time we resize the window. 

        self.config(width=self.root.winfo_width(), height=self.root.winfo_height())
        self.calculate_middle()

        # We delete all the objects on the window
        self.delete(self.axis_x, self.axis_y)
        for tick in self.ticks:
            self.delete(tick) 
        for point in self.plotted_points_list:
            self.delete(point)

        # Then we draw them back
        self.draw_axes()
        self.draw_ticks()
        self.redraw_points()


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


    # def plot_points(self, x, y):
    #     # Plot a point (x, y) on the Canvas

    #     width = (int(self['width']) / 2) + x*(int(self['width'])/20)
    #     height = (int(self['height']) / 2) - y*(int(self['height'])/10)

    #     radius = 5
    #     point = self.create_oval(width + radius, height + radius, width - radius, height - radius, fill="black", width="1", outline="")
    #     self.points_current.append(point)
    #     self.xcoords.append(x)
    #     self.ycoords.append(y)

    def plot_points2(self, point):
        # Plot a point (x, y) on the Canvas

        # point.x, point.y, point.vector


        x = point.vector[0]
        y = point.vector[1]

        width = (int(self['width']) / 2) + x*(int(self['width'])/20)
        height = (int(self['height']) / 2) - y*(int(self['height'])/10)

        radius = 5
        plotted_point = self.create_oval(width + radius, height + radius, width - radius, height - radius, fill="black", width="1", outline="")
        self.plotted_points_list.append(plotted_point)
        self.points_current.append(point)
        self.xcoords.append(x)
        self.ycoords.append(y)

        

    def redraw_points(self):
        # After we resize the window, we're gonna use this to redraw all the points
        # self.points_current = []
        # temp_xcoords = my_deep_copy(self.xcoords)
        # temp_ycoords = my_deep_copy(self.ycoords)

        #self.points_list = []
        temp_points = my_deep_copy(self.points_current)
        self.points_current = []

        for i in range(len(temp_points)):     
            self.plot_points2(temp_points[i])

        # self.xcoords = temp_xcoords
        # self.ycoords = temp_ycoords

        self.points_current = temp_points

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

        for point in self.plotted_points_list:
            self.delete(point)
        self.plotted_points_list = []


        for point in self.points_current:
            point.rotate_y(-(diffx))
            point.rotate_x(-(diffy))

        temp_points = my_deep_copy(self.points_current)
        self.points_current = []

        for point in temp_points:
            self.plot_points2(point)

        # self.new_click_coords_x = 0
        # self.new_click_coords_y = 0
        # self.old_click_coords_x = 0
        # self.old_click_coords_y = 0
        #print(event.x, event.y)

    def mouse_click_print(self, event):
        # print(event.x, event.y)
        self.old_click_coords_x = event.x
        self.old_click_coords_y = event.y
if (__name__ == "__main__"):
    # root = tk.Tk()
    # root.geometry('600x400')
    # root.title('3D Engine')

    # root.minsize(600, 400)
    # root.maxsize(1536, 864)

    # canvas = Canvas_2D(root, 600, 400, 'White')

    # canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    # root.mainloop()

    x = Point(1,0,0)
    x.rotate_x(90)