##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################
from GUI.GUI_init import *
from GUI.Dirt_Generator import *
from GUI.Path import *
from Uninformed_Search.BFS import *
from Uninformed_Search.IDS import *
from Informed_Search.Heuristic_1 import *
from Informed_Search.Heuristic_2 import *
from Uninformed_Search.Definitions_IDS import *
import sys
from time import time
import turtle

def main():

	# Initialising the GUI screen, and fetching some helper parameters through the initialise_board() function.
	screen, init_t, coordinates_1, coordinates_2, width, height, text_end_cood_list = initialise_board()
	
	# Generating the dirt onto the board and fetching the dirt list for two boards. Creating desired root states and goal states.
	dirt_list_1 = generate_dirt(60, init_t, screen, coordinates_1, width, height, 4)
	dirt_list_2 = generate_dirt(40, init_t, screen, coordinates_2, width, height, 10)
	goal_state = State([0,0], [])
	root_state1 = State([0,0], dirt_list_1)
	root_state2 = State([0,0], dirt_list_2)

	# Iterative Deepening Search
	t0 = time()
	temp = ids(root_state1, goal_state, 4)
	t1 = round(time() - t0, 4)
	#print(t1)
	action_list1 = temp[0][0]
	path_cost1 = temp[0][1]
	count1 = temp[1]
	max_stack_size = temp[2]
	trace_path(action_list1, coordinates_1, width, height)
	
	# Greedy Best First Search - Heuristic 1
	t0 = time()
	temp = gbs1(root_state2, goal_state, 10)
	t1 = round(time() - t0, 4)
	action_list2 = temp[0][0]
	path_cost2 = temp[0][1]
	count2 = temp[1]
	trace_path(action_list2, coordinates_2, width, height, True, 0)
	
	# Greedy Best First Search - Heuristic 1
	t2 = time()
	action_list3, path_cost3 = gbs2(root_state2, goal_state, 10)
	t3 = round(time() - t2, 4)
	#print(action_list3, path_cost3)
	trace_path(action_list3, coordinates_2, width, height, True, 1)
	
	# Printing out Ri's
	# R1
	init_t.penup()
	init_t.setpos(text_end_cood_list[0][0], text_end_cood_list[0][1])
	init_t.pendown()
	init_t.write(str(count1), font = ("Arial", 15, "normal"))

	# R2
	temp = Node(State([0, 0], [[1,2], [2,1]]), None, None, 10, 1, 1)
	sizeof_node = sys.getsizeof(temp)
	#print(sizeof_node)
	init_t.penup()
	init_t.setpos(text_end_cood_list[1][0], text_end_cood_list[1][1])
	init_t.pendown()
	init_t.write(str(sizeof_node) + "bytes", font = ("Arial", 15, "normal"))

	# R3
	init_t.penup()
	init_t.setpos(text_end_cood_list[2][0], text_end_cood_list[2][1])
	init_t.pendown()
	#print(max_stack_size)
	init_t.write(str(max_stack_size), font = ("Arial", 15, "normal"))

	# R4
	init_t.penup()
	init_t.setpos(text_end_cood_list[3][0], text_end_cood_list[3][1])
	init_t.pendown()
	init_t.write(str(count2) + "units", font = ("Arial", 15, "normal"))

	# R5
	init_t.penup()
	init_t.setpos(text_end_cood_list[4][0], text_end_cood_list[4][1])
	init_t.pendown()
	init_t.write(str(t1) + "seconds", font = ("Arial", 15, "normal"))

	# R6
	init_t.penup()
	init_t.setpos(text_end_cood_list[5][0], text_end_cood_list[5][1])
	init_t.pendown()
	init_t.write(str(path_cost1), font = ("Arial", 15, "normal"))

	# R7
	init_t.penup()
	init_t.setpos(text_end_cood_list[6][0], text_end_cood_list[6][1])
	init_t.pendown()
	init_t.write(str(sizeof_node) + "bytes", font = ("Arial", 15, "normal"))

	# R8
	init_t.penup()
	init_t.setpos(text_end_cood_list[7][0], text_end_cood_list[7][1])
	init_t.pendown()
	init_t.write(str(path_cost2) + ", " + str(path_cost3) , font = ("Arial", 15, "normal"))

	# R9
	init_t.penup()
	init_t.setpos(text_end_cood_list[8][0], text_end_cood_list[8][1])
	init_t.pendown()
	init_t.write(str(t1 + t3) + ", " + str(path_cost3) , font = ("Arial", 15, "normal"))

	# R10
	init_t.penup()
	init_t.setpos(text_end_cood_list[9][0], text_end_cood_list[9][1])
	init_t.pendown()
	init_t.write(str(count1*sizeof_node) + ", " + str(count2*sizeof_node), font = ("Arial", 15, "normal"))

	# R11
	sum_cost = 0
	for i in range(10):
		dirt_list_1 = generate_dirt(100, init_t, screen, coordinates_1, width, height, 3, draw = False)
		goal_state = State([0,0], [])
		root_state1 = State([0,0], dirt_list_1)
		temp = ids(root_state1, goal_state, 3)
		sum_cost += temp[0][1]
	avg_cost1 = float(sum_cost)/10

	sum_cost = 0
	for i in range(10):
		dirt_list_2 = generate_dirt(100, init_t, screen, coordinates_2, width, height, 3, draw = False)
		goal_state = State([0,0], [])
		root_state2 = State([0,0], dirt_list_2)
		temp = gbs1(root_state2, goal_state, 3)
		sum_cost += temp[0][1]
	avg_cost2 = float(sum_cost)/10
		

	init_t.penup()
	init_t.setpos(text_end_cood_list[10][0], text_end_cood_list[10][1])
	init_t.pendown()
	init_t.write(str(avg_cost1) + ", " + str(avg_cost2) , font = ("Arial", 15, "normal"))

#################################################################################################
	# G3
	time_h1 = []
	time_h2 = []

	# Computing times.
	for mat_size in range(3, 15):
		dirt_list = generate_dirt(30, init_t, screen, coordinates_1, width, height, mat_size, False)
		goal_state = State([0,0], [])
		root_state = State([0,0], dirt_list)
		
		t0 = time()
		temp = gbs1(root_state, goal_state, mat_size)
		t1 = round(time() - t0, 4)
		time_h1.append(t1)

		t2 = time()
		temp = gbs2(root_state, goal_state, mat_size)
		t3 = round(time() - t2, 4)
		time_h2.append(t3)

		print("Check: ", mat_size, t1, t3)

	print(time_h1)
	print(time_h2)

	#time_h1 = [0.0003, 0.0006, 0.0026, 0.0018, 0.0024, 0.0041, 0.0262, 0.0074, 0.0154, 0.0217, 12.4673, 14.8326]
	#time_h2 = [0.0005, 0.0027, 0.0021, 0.0042, 0.0067, 0.0103, 0.0456, 0.1834, 0.0276, 0.5515, 0.3051, 27.4083]

	# Scaling according to the window size
	max1 = max(time_h1)
	max2 = max(time_h2)
	min1 = min(time_h1)
	min2 = min(time_h2)

	new_time_h1 = []
	new_time_h2 = []
	for i in time_h1:
		new_time_h1.append((i - min1)/(max1 - min1) * (height - 100)/2)
	print(new_time_h1)
	for i in time_h2:
		new_time_h2.append((i - min2)/(max2 - min2) * (height - 100)/2)
	print(new_time_h2)

	# Drawing the graph
	graph_t = Turtle()
	graph_t.pensize(2)
	graph_t.penup()
	graph_t.setpos((width/3)-(width/2) + 30, (-1 * (height- 50))/2)
	graph_t.pendown()
	graph_t.setheading(0)
	graph_t.fd(width/3 - 60)
	graph_t.setheading(90)
	graph_t.penup()
	graph_t.setpos((width/3)-(width/2)+30, (-1 * (height- 50))/2)
	graph_t.pendown()
	graph_t.fd((height - 100)/2)
	graph_t.penup()
	graph_t.setpos((width/3)-(width/2)+30, (-1 * (height- 50))/2)
	graph_t.pendown()

	k = 1
	graph_t.pensize(1.5)
	graph_t.pencolor("blue")
	for i in new_time_h1:
		graph_t.setpos((width/3) - (width/2) + 30 + ((width-60)/3)*k/14, (-1*(height-100)/2) + i)
		k += 1

	k = 1
	graph_t.pencolor("green")
	graph_t.penup()
	graph_t.setpos((width/3)-(width/2)+30, (-1 * (height- 50))/2)
	graph_t.pendown()
	for i in new_time_h2:
		graph_t.setpos((width/3) - (width/2) + 30 + ((width-60)/3)*k/14, (-1*(height-100)/2) + i)
		k += 1

####################################################################################
	# G4
	time_list = []
	for i in range(10, 105, 5):
		dirt_list = generate_dirt(i, init_t, screen, coordinates_1, width, height, 10)# draw = False)
		goal_state = State([0,0], [])
		root_state = State([0,0], dirt_list)
		t0 = time()
		temp = gbs1(root_state, goal_state, 10)
		action_list = temp[0][0]
		trace_path(action_list, coordinates_1, width, height)
		t1 = round(time() - t0, 4)
		time_list.append(t1)
	print(time_list)
	# time_list = [5.7793, 7.3004, 6.4329, 9.9558, 9.8568, 11.7416, 11.5955, 11.546, 12.97, 17.069, 19.3391, 16.8374, 18.008, 18.554, 20.7309, 23.6414, 25.369, 27.7575, 24.0187]
	max_time = max(time_list)
	min_time = min(time_list)
	new_time_list = []
	for time_instance in time_list:
	 	new_time_list.append((time_instance - min_time)/(max_time - min_time) * (height - 100)/2)
	print(new_time_list)

	graph_t.pencolor("black")
	graph_t.pensize(2)
	graph_t.penup()
	graph_t.setpos(-1*((width/3)-(width/2)) + 30, (-1 * (height- 50))/2)
	graph_t.pendown()
	graph_t.setheading(0)
	graph_t.fd(width/3 - 60)
	graph_t.setheading(90)
	graph_t.penup()
	graph_t.setpos(-1*((width/3)-(width/2))+30, (-1 * (height- 50))/2)
	graph_t.pendown()
	graph_t.fd((height - 100)/2)
	graph_t.penup()
	graph_t.setpos(-1*((width/3)-(width/2))+30, (-1 * (height- 50))/2)
	graph_t.pendown()

	k = 10
	graph_t.pensize(1.5)
	graph_t.pencolor("blue")
	for i in new_time_list:
		graph_t.setpos(-1*((width/3)-(width/2))+30 + ((width-90)/3)*k/110, (-1 * (height - 100)/2) + i)
		k += 5
########################################################################################

	screen.exitonclick()

if __name__ == "__main__":
	main()
