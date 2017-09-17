##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

from random import *
from turtle import *

# fill the selected tile with given color
def fill_color(dirt_t, start_x, start_y, color, cell_width, cell_height, half = False, default = 0):
	dirt_t.penup()

	if not half:
		dirt_t.setpos(start_x, start_y)
	else:
		cell_height /= 2
		if default == 0:
			dirt_t.setpos(start_x, start_y)
		else:
			dirt_t.setpos(start_x, start_y - cell_height)
	# Assuming that the turtle is pointing vertically upwards when the function is called.
	dirt_t.fillcolor(color)
	dirt_t.begin_fill()
	dirt_t.pendown()
	dirt_t.right(90)
	dirt_t.fd(cell_width)
	dirt_t.right(90)
	dirt_t.fd(cell_height)
	dirt_t.right(90)
	dirt_t.fd(cell_width)
	dirt_t.right(90)
	dirt_t.fd(cell_height)
	dirt_t.right(90)
	dirt_t.end_fill()
	dirt_t.penup()
	dirt_t.left(90)

# Get the coordinates of a given tile
def get_coordinates(coordinates, dirt, cell_width, cell_height):
	temp = []
	temp.append(coordinates[0] + dirt[1]*cell_width)
	temp.append(coordinates[1] - dirt[0]*cell_height)
	return temp

# Draw the generated dirt
def dirt_generator(init_t, grid_coordinates, coordinates, cell_width, cell_height, dirt_list):
	#print(dirt_list)
	for dirt in dirt_list:
		dirt_coordinate = get_coordinates(coordinates, dirt, cell_width, cell_height)
		fill_color(init_t, dirt_coordinate[0], dirt_coordinate[1], "gray", cell_width, cell_height)

# Generate the dirt randomly
def generate_dirt(percentage, init_t, screen, coordinates, width, height, matrix_size, draw = True):
	cell_width = ((width/3)-1)/10
	cell_height = ((height/2)-1)/10
	# Initialising the grid coordinates of all the points
	grid_coordinates = []
	for i in range(matrix_size):
		for j in range(matrix_size):
			temp = [i, j]
			grid_coordinates.append(temp)

	percentage = (percentage * matrix_size * matrix_size)/(10*10)

	dirt_list = sample(grid_coordinates, percentage)
	if draw:
		dirt_generator(init_t, grid_coordinates, coordinates, cell_width, cell_height, dirt_list)
	
	return dirt_list
