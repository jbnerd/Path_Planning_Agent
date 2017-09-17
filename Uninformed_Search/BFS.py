##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

from Queue import Queue
from collections import deque
import copy
from Definitions_BFS import *


# Reach the goal tile directly once all the tiles are clean.
def direct_reach(agent_coordinate, goal_coordinate):

	row_pos = agent_coordinate[0] - goal_coordinate[0]
	col_pos = agent_coordinate[1] - goal_coordinate[1]

	action_list = []

	if row_pos > 0:
		for i in range(row_pos):
			action_list.append("up")
	else:
		for i in range(abs(row_pos)):
			action_list.append("down")

	if col_pos > 0:
		for i in range(col_pos):
			action_list.append("left")
	else:
		for i in range(abs(col_pos)):
			action_list.append("right")

	#print(action_list, row_pos, col_pos, agent_coordinate, goal_coordinate)
	return action_list

# Generate the action sequence
def solution(node, goal_state):

	action_list = []
	cost = node.path_cost
	orig_agent_coordinate = node.state.agent_coordinate
	while (node.parent is not None):
		action_list.append(node.action)
		# cost += node.path_cost
		node = node.parent

	action_list = action_list[::-1]
	#print(orig_agent_coordinate)
	new_action_list = action_list + direct_reach(orig_agent_coordinate, goal_state.agent_coordinate)
	
	return new_action_list, cost

# BreadthFirst Search
def BFS(root_state, goal_state, matrix_size):

	root_node = Node(root_state, None, None, 0, matrix_size)
	if(root_state == goal_state):
		return [], 0

	frontier = deque()
	explored = set()
	frontier_check = set()

	frontier.append(root_node)
	frontier_check.add(root_node.state)
	
	while(True):
		if len(frontier) == 0:
			return [], 0 #-1 signifies failure

		node = frontier.popleft()
		frontier_check.discard(node.state)

		if node.state not in explored or child.state not in frontier_check:
			if node.state.dirt_list == []:
				return solution(node, goal_state)
		explored.add(node.state)

		children = node.children(matrix_size)
		for child in children:
			frontier.append(child)
			frontier_check.add(child.state)

"""		children = node.children(matrix_size)
		for child in children:
			if child.state not in explored or child.state not in frontier_check:
				if child.state.dirt_list == []:
					# print(child.state.agent_coordinate, goal_state.agent_coordinate)
					return solution(child, goal_state)
				frontier.append(child)
				frontier_check.add(child.state)
"""

if __name__ == "__main__":
	goal_dirt_list = []
	root_dirt_list = [[1,1],[2,2],[1,2],[4,2],[3,3],[5,5],[3,9],[2,8],[1,6],[8,6],[9,3],[5,7],[6,3]]
	goal_state = State([9, 9], goal_dirt_list)
	root_state = State([0, 0], root_dirt_list)
	action_list, path_cost = BFS(root_state, goal_state, 10)
	print(action_list, path_cost)

	#direct_path([2, 2], 4)
