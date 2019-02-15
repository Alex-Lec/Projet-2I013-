from tkinter import *
import math
"""position : x 1  =  550   y 1  =  225
position : x 2  =  550   y 2  =  175
position : x 3  =  450   y 3  =  175
position : x 4  =  450   y 4  =  225
position : x 1  =  475.0   y 1  =  250.0
position : x 2  =  525.0   y 2  =  250.0
position : x 3  =  525.0   y 3  =  150.0
position : x 4  =  475.0   y 4  =  150.0"""
WIDTH = 1000
HEIGHT = 600
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
CANVAS_CENTER = (CANVAS_MID_X,CANVAS_MID_Y)
SIDE = WIDTH/4

root = Tk()
canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.pack()


points = [
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y + SIDE/2],
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y + SIDE/2],
]

def rotate(points, angle, center):
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points

def draw_square(points, color="red"):
    canvas.create_polygon(points, fill=color)



points1=[[550,225],[550,175],[450,175],[450,225]]

points2 = rotate(points1,90,(500,200))
draw_square(points1, "blue")
draw_square(points2, "red")
print(points2)


mainloop()
