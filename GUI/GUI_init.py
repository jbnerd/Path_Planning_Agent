##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

from turtle import *
from random import *

# Initialising the text window
def init_text_window(init_t):
	width = float(window_width())
	height = float(window_height())
	# Drawing the 1:2 partition
	init_t.penup()
	init_t.setpos((width/3)-(width/2), (-1 * height)/2)
	init_t.pendown()
	init_t.left(90)
	init_t.pensize(3)
	init_t.fd(height)
	init_t.penup()

	init_t.setpos(-1 * width/2, height/2 - 50)
	cood_list = []
	for i in range(1, 12):
		init_t.pendown()
		init_t.write("R" + str(i) + " :", move = True, font = ("Arial", 15, "normal"))
		temp = init_t.pos()
		cood_list.append(temp)
		init_t.penup()
		init_t.setpos(-1 * width/2, temp[1] - 65)

	return cood_list

# initialise the windows for graphs
def init_graph_window(init_t):

	width = float(window_width())
	height = float(window_height())
	# Drawing the graph partitions
	init_t.penup()
	init_t.setpos((width/3)-(width/2), 0)
	init_t.right(90)
	init_t.pendown()
	init_t.fd(2*width/3)
	init_t.penup()
	init_t.setpos((width/2)-(width/3), -1 * (height/2))
	init_t.left(90)
	init_t.pendown()
	init_t.fd(height)
	init_t.penup()

# Draw the grid
def draw_grid(init_t, coordinates, cell_width, cell_height):
	height = float(window_height())
	width = float(window_width())
	
	init_t.pensize(1.5)
	init_t.penup()
	init_t.setpos(coordinates[0], coordinates[1])
	init_t.right(90)

	for i in range(11):
		init_t.pendown()
		init_t.fd((width/3) - 1)
		init_t.penup()
		init_t.setpos(coordinates[0], coordinates[1] - i*cell_height)

	init_t.right(90)
	init_t.penup()
	init_t.setpos(coordinates[0], coordinates[1])
	
	for i in range(11):
		init_t.pendown()
		init_t.fd((height/2) - 1)
		init_t.penup()
		init_t.setpos(coordinates[0] + i*cell_width, coordinates[1])

	init_t.penup()
	init_t.right(180)

def initialise_board():
	# Invoking the screen and setting the window size.
	screen = Screen()
	screen.title("\t"*9 + "Vacuum Cleaner Intelligent Agent")
	
	# Setting the turtle speed to the slowest and drawing the GUI.
	init_t = Turtle()
	init_t.ht()
	#init_t.ht()
	init_t.speed(0)
	text_end_cood_list = init_text_window(init_t)
	#print(text_end_cood_list)
	init_graph_window(init_t)

	init_t.setpos(0,0)
	#init_t.write("LOL",font=("Arial", 20, "normal"))
	#init_t.write("WEW",font=("Arial", 20, "normal"))
	#init_t.write("     ",font=("Arial", 20, "normal"))

	# Finding the co-ordinates of the upper-left corner of the grid
	height = float(window_height())
	width = float(window_width())

	cell_width = ((width/3)-1)/10
	cell_height = ((height/2)-1)/10

	coordinates_1 = [(width/3) - (width/2) + 1, (height/2) - 1]
	coordinates_2 = [(width/2) - (width/3) + 1, (height/2) - 1]

	# Drawing the grid
	draw_grid(init_t, coordinates_1, cell_width, cell_height)
	draw_grid(init_t, coordinates_2, cell_width, cell_height)

	return screen, init_t, coordinates_1, coordinates_2, width, height, text_end_cood_list