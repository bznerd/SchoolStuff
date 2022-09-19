"""
Ben Campbell 9/16/22
1.1.6 Spider
Draws a spider using arcs
"""
import turtle
import math

#Create turtle
spider = turtle.Turtle()
spider.hideturtle()

#Add multiple list types together and return as a tuple
def add(*coords):
    total = [0 for x in range(len(coords[0]))]
    for pair in coords:
       total = [total[x] + pair[x] for x in range(len(total))] 
    return tuple(total)

#Convert degrees to radians
def to_rad(degrees):
    return degrees * math.pi/180

#Draw circle routine
def draw_circle(location, size, color):
    spider.penup()
    spider.pensize(1)
    spider.pencolor(color)
    spider.fillcolor(color)
    spider.seth(0)
    spider.goto(add((0,-size), location))
    spider.pendown()
    spider.begin_fill()
    spider.circle(size)
    spider.end_fill()

#Draw leg routine
def draw_leg(angle, location, radius, extent, thickness=4, color='black'):
    spider.penup()
    spider.pensize(thickness)
    spider.pencolor(color)
    spider.seth(angle)
    spider.goto(location)
    spider.pendown()
    spider.circle(radius, extent)

#Polar coords to cartesian
def to_cartesian(angle, radius):
    return (radius * math.cos(to_rad(angle)), radius * math.sin(to_rad(angle)))

#Parameters
body_coords = (0,0) 
head_offset = (0,-80)
body_size, head_size = 80, 45
eye_size = 8  
pupil_size = 2
eye_spacing = 25 
eye_offset = (-5, -20)
leg_range = 60
leg_len = 100
leg_radius = 100

#Draw body and head circles
draw_circle(body_coords, body_size, 'black')
draw_circle(add(body_coords, head_offset), head_size, 'black')

#List of angles for polar coords of legs (mirrored to each side)
legs = [(-1/2 * leg_range) + (x * leg_range/3) for x in range(4)] 
legs += [180 + leg for leg in legs]

#For each leg call draw function with coordinates from polar (angle + body radius), and switch curve direction past 90 degrees
for leg in legs:
    draw_leg(leg, to_cartesian(leg, body_size), -leg_radius if leg < 90 else leg_radius, leg_len)

#Draw circles for eyes
draw_circle(add(body_coords, head_offset, eye_offset, (-1/2 * eye_spacing, 0)), eye_size, 'purple')
draw_circle(add(body_coords, head_offset, eye_offset, (+1/2 * eye_spacing, 0)), eye_size, 'purple')
draw_circle(add(body_coords, head_offset, eye_offset, (-1/2 * eye_spacing - 3, -3)), pupil_size, 'black')
draw_circle(add(body_coords, head_offset, eye_offset, (+1/2 * eye_spacing - 3, -3)), pupil_size, 'black')

#Wait for keyboard input to close
input()
