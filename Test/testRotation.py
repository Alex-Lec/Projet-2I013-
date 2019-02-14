from tkinter import *
import math

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



#points1=[[550,225],[550,175],[450,175],[450,225]]

points2 = rotate(points,90,)
draw_square(points1, "blue")
draw_square(points2, "red")
print(points2)


mainloop()
