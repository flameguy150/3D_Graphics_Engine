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

root.minsize(600, 400)
root.maxsize(1536, 864)


canvas = tk.Canvas(root, width=600, height=400, bg='navy')

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

# print(root.winfo_screenwidth)
# print(root.winfo_screenheight)

# originxx = canvas.create_text(1/2 * int(canvas['width']) + 5, 1/2 * int(canvas['height']) + 5, text="O")

#gridpoints
ticks = []
tecks = []
for x in range (int(-middle_w), int(middle_w) + 1, 50):
    ticks.append(canvas.create_line(middle_w + x, int(canvas['height'])/2, middle_w + x + 2, int(canvas['height'])/2, width=10, fill="white")) 
    tecks.append(canvas.create_text(middle_w + x, int(canvas['height'])/2 + 10, text=str(x)))
for y in range (int(-middle_h), int(middle_h) + 1, 50):
    ticks.append(canvas.create_line(int(canvas['width'])/2, middle_h + y, int(canvas['width'])/2, middle_h + y + 2, width=10, fill="white")) 
    tecks.append(canvas.create_text(int(canvas['width'])/2 + 10, middle_h + y, text=str(y), fill="white"))


def can_resize(event):
    # new_w = root.winfo_screenwidth()
    # new_h = root.winfo_screenheight()
    # can_width = new_w
    # can_height = new_h
    global crosshair
    global axis_x
    global axis_y
    global ticks
    global tecks
    print(root.winfo_width(), root.winfo_height())
    canvas.config(width=root.winfo_width(), height=root.winfo_height())
    canvas.delete(crosshair)
    crosshair = canvas.create_oval(int(canvas['width'])/2 - radius, 
                                    int(canvas['height'])/2 - radius, 
                                    int(canvas['width'])/2 + radius, 
                                    int(canvas['height'])/2 + radius, 
                                    fill="red", outline="blue", width="1")
    
    canvas.delete(axis_x, axis_y)
    axis_x = canvas.create_line(main_x1, int(canvas['height'])/2, 
                                canvas['width'], 
                                int(canvas['height'])/2,
                                fill="black")
    axis_y = canvas.create_line(int(canvas['width'])/2,
                                main_y1,
                                int(canvas['width'])/2,
                                canvas['height'],
                                fill="black")
    # canvas.delete(originxx)
    # originxx = canvas.create_text(int(canvas['width']/2) + 5, int(canvas['height']/2) + 5, text="O")

    #delete all gridpoints and text
    for tick in ticks:
        canvas.delete(tick)
    for teck in tecks:       
        canvas.delete(teck)

    ticks = []
    tecks = []

    #for tick in ticks:
        #canvas.delete(...)

    # for x in range (int(-middle_w), int(middle_w) + 1, 50):
    #     #ticks.append(canvas.create_....)
    #     gridpoint_x = canvas.create_line(middle_w + x, int(canvas['height'])/2, middle_w + x + 2, int(canvas['height'])/2, width=10, fill="white")  
    #     gridtext_x = canvas.create_text(middle_w + x, int(canvas['height'])/2 + 10, text=str(x), fill="white")
    # for y in range (int(-middle_h), int(middle_h) + 1, 50):
    #     gridpoint_y = canvas.create_line(int(canvas['width'])/2, middle_h + y, int(canvas['width'])/2, middle_h + y + 2, width=10, fill="white") 
    #     gridtext_y = canvas.create_text(int(canvas['width'])/2 + 10, middle_h + y, text=str(y), fill="white")

    #set max and min grid increment
    #max = 5
    #min = 50

    #600X400
    #100% = 50
    #min = 5

    #600 = 50
    # 50
    # 45
    # 40
    # 35
    # 30
    # 25
    # 20
    # 15
    # 10
    # 5
    #1536 = 5

    #get percentage/ratio to determine increments based on window size
    #round number to nice number divisble by 5
    
    #x-axis min=600 max=winfo.screen_width()
    # increments = x + 5
    
    # x = canvas['width']/

    # max = 1536
    # min = 600

    # diff = 936
    # percentjohn = (int(canvas['width'])-600) / 936
    # percentjohn * 45


    # DEBUG HERE
    # DEBUG HERE

    percentjohn = (int(canvas['width'])-600) / 936
    percentjlee = percentjohn * 45
    increments = int(percentjlee + 5)
    
    # DEBUG HERE
    # DEBUG HERE
    
    


    for x in range (int(-middle_w), int(middle_w) + 1, increments):
        ticks.append(canvas.create_line(middle_w + x, int(canvas['height'])/2, middle_w + x + 2, int(canvas['height'])/2, width=10, fill="white")) 
        tecks.append(canvas.create_text(middle_w + x, int(canvas['height'])/2 + 10, text=str(x), fill="white"))
    for y in range (int(-middle_h), int(middle_h) + 1, increments):
        ticks.append(canvas.create_line(int(canvas['width'])/2, middle_h + y, int(canvas['width'])/2, middle_h + y + 2, width=10, fill="white")) 
        tecks.append(canvas.create_text(int(canvas['width'])/2 + 10, middle_h + y, text=str(y), fill="white"))
root.bind("<Configure>", can_resize)


#create_line multiple times with for loop
#just need to change x1 and x2 to shift
#good width for lines is 10, distance for x1 and x2 should be about 2

# gridpoint = canvas.create_line(0, int(canvas['height'])/2, 2, int(canvas['height'])/2, width=10, fill="green")
# gridpoint = canvas.create_line(10, int(canvas['height'])/2, 12, int(canvas['height'])/2, width=10, fill="green")
# gridpoint = canvas.create_line(20, int(canvas['height'])/2, 22, int(canvas['height'])/2, width=10, fill="green")

  

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
# print(middle_h)
# print(middle_w)
# print(can_width)
# print(can_height)

#parameters of create_ovals (x1,y1) = top left point of box of circle, (x2, y2) = bottom right point of box of circle
# crosshair.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) does not work
# print(canvas.coords(crosshair))





root.mainloop()

# for x in range(10):
#     time.sleep(0.2)
#     crosshair.move(crosshair, 10, 0)


#Make the shape move
#