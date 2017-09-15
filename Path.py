##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

from turtle import *
from Dirt_Generator import *

def trace_path(action_list, coordinates, width, height, half = False, default = 2):

	cell_width = ((width/3)-1)/10
	cell_height = ((height/2)-1)/10

	path_t = Turtle()
	fill_t = Turtle()
	path_t_coordinate = [0, 0]

	path_t.pensize(3)
	path_t.speed(0)
	path_t.penup()
	path_t.setpos((coordinates[0] + cell_width/2, coordinates[1] - cell_height/2))
	if default == 0:
		path_t.pencolor("blue")
		color = "blue"
	elif default == 1:
		path_t.pencolor("green")
		color = "green"
	else:
		path_t.pencolor("red")
		color = "orange"
	path_t.pendown()
	
	fill_t.penup()
	fill_t.left(90)
	fill_t.pendown()
	fill_t.ht()
	fill_t.speed(0)

	for action in action_list:
		if action == "up":
			path_t.left(90)
			path_t.fd(cell_height)
			path_t.right(90)
			path_t_coordinate[0] -= 1
		elif action == "right":
			path_t.fd(cell_width)
			path_t_coordinate[1] += 1
		elif action == "down":
			path_t.right(90)
			path_t.fd(cell_height)
			path_t.left(90)
			path_t_coordinate[0] += 1
		elif action == "left":
			path_t.right(180)
			path_t.fd(cell_width)
			path_t.right(180)
			path_t_coordinate[1] -= 1
		elif action == "suck":
			fill_color(fill_t, coordinates[0] + cell_width*path_t_coordinate[1], coordinates[1] - cell_height*path_t_coordinate[0], color, cell_width, cell_height, half, default)
			
