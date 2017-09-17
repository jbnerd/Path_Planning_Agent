##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

from Definitions_IDS import *

def direct_reach(agent_coordinate, goal_coordinate):

	row_pos = agent_coordinate[0] - goal_coordinate[0]
	col_pos = agent_coordinate[1] - goal_coordinate[1]
	cost = 0

	action_list = []

	if row_pos > 0:
		for i in range(row_pos):
			action_list.append("up")
			cost += 2
	else:
		for i in range(abs(row_pos)):
			action_list.append("down")
			cost += 2

	if col_pos > 0:
		for i in range(col_pos):
			action_list.append("left")
			cost += 2
	else:
		for i in range(abs(col_pos)):
			action_list.append("right")
			cost += 2

	#print(action_list, row_pos, col_pos, agent_coordinate, goal_coordinate)
	return [action_list, cost]

def solution(node, goal_state):

	action_list = []
	cost = node.path_cost
	orig_agent_coordinate = node.state.agent_coordinate
	while (node.parent is not None):
		action_list.append(node.action)
		#cost += node.path_cost
		node = node.parent

	action_list = action_list[::-1]
	#print(orig_agent_coordinate)
	temp = direct_reach(orig_agent_coordinate, goal_state.agent_coordinate)
	new_action_list = action_list + temp[0]
	
	return action_list, cost + temp[1]

def dls(root_state, goal_state, matrix_size, depth, explored):

	if(root_state == goal_state):
		return [], 0
	count = 0
	max_stack_size = 1

	root_node = Node(root_state, None, None, 0, matrix_size, 1)
	count += 1

	frontier = []
	#explored = set()
	
	frontier.append(root_node)
	#explored.add(root_state)
	
	k, z = 0, 0
	while len(frontier) > 0:
		k += 1
		if k == 100000:
			k = 0
			z += 1
			print(z)

		node = frontier.pop()
		children = node.children(matrix_size)
		count += len(children)
		for child in children:
			if child.state not in explored:
				if child.state == goal_state:
					return (solution(child, goal_state), count, max_stack_size)
				elif child.depth <= depth:
					explored[child.state] = child.path_cost
					frontier.append(child)
					if len(frontier) >= max_stack_size:
						max_stack_size = len(frontier)
			else:
				if child.depth <= depth:
					if explored[child.state] >= child.path_cost:
						explored[child.state] = child.path_cost
						frontier.append(child)
						if len(frontier) >= max_stack_size:
							max_stack_size = len(frontier)

	return None


		# #if node.depth < depth:
		# children = node.children(matrix_size)
		# for child in children:
		# 	if child.state.dirt_list == []:
		# 		return solution(child, goal_state)
		# 	if child.state in explored:# and explored[child.state] > child.path_cost:
		# 			continue
		# 			# explored[child.state] = child.path_cost
		# 			# frontier.append(child)
		# 	else:
		# 		if child.depth <= depth:
		# 			explored.add(child.state)# = child.path_cost
		# 			frontier.append(child)
		# 		# if child.state == goal_state:
		# 		# 	return solution(child, goal_state)
		# 		# elif child.state in explored and explored[child.state] > child.path_cost:
		# 		# 	explored[child.state] = child.path_cost
		# 		# 	frontier.append(child)
		# 		# else:
		# 		# 	frontier.append(child)
		# 		# 	explored[child.state] = child.path_cost

	#return None

def ids(root_state, goal_state, matrix_size):

	depth = 1
	explored = {}
	explored[root_state] = 0
	while(True):
		print("depth: " + str(depth))
		found = dls(root_state, goal_state, matrix_size, depth, explored)
		if found is not None:
			return found
		else:
			depth += 1

if __name__ == "__main__":

	# goal_dirt_list = []
	# root_dirt_list = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
	# goal_state = State([3, 3], goal_dirt_list)
	# root_state = State([0, 0], root_dirt_list)
	# action_list, path_cost = ids(root_state, goal_state, 4)
	# print(action_list, path_cost)


	goal_dirt_list = []
	root_dirt_list = [[1,1],[2,2],[1,2],[4,2],[3,3]]#,[5,5],[3,9],[2,8],[1,6],[8,6],[9,3],[5,7],[6,3]]
	goal_state = State([9, 9], goal_dirt_list)
	root_state = State([0, 0], root_dirt_list)
	action_list, path_cost = ids(root_state, goal_state, 10)
	print(action_list, path_cost)