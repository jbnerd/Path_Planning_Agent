##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

import copy

class State(object):
	"""docstring for State"""
	
	def __init__(self, agent_coordinate, dirt_list):
		self.agent_coordinate = agent_coordinate
		self.dirt_list = dirt_list
		#self.heuristic_cost = heuristic_cost
			
	def __str__(self):
		return "Agent_coordinate: " + str(self.agent_coordinate) + ", Dirt List: " + str(self.dirt_list)

	def __eq__(self, other):
		return (self.agent_coordinate == other.agent_coordinate and self.dirt_list == other.dirt_list)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash((tuple(self.agent_coordinate), tuple([tuple(x) for x in self.dirt_list])))

class Node(object):
	"""docstring for Node"""
	
	def __init__(self, state, parent, action, path_cost, matrix_size, heuristic_cost):
		"""
			state: the state in the state space to which the node corresponds.
			parent: the node in the search tree that generated this node.
			action: the action that was applied to the parent to generate the node.
			path_cost: the cost, traditionally denoted by g(n), of the path from the intital state to the node, as indicated by the parent pointers.
		"""
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost
		self.matrix_size = matrix_size
		self.heuristic_cost = heuristic_cost

	def __str__(self):
		return str(self.parent) + str(self.action) + str(self.path_cost)

	def __repr__(self):
		return str(self.parent) + str(self.action) + str(self.path_cost)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def get_agent_coordinate(self):
		return self.state.agent_coordinate

	def find_max(self, child_nodes):
		maxi = child_nodes[0].heuristic_cost
		itr = 0

		for i, child in enumerate(child_nodes):
			if maxi < child.heuristic_cost:
				maxi = child.heuristic_cost
				itr = i
		return child_nodes[i]

	def children(self, matrix_size):
		
		child_nodes = []
		actions = ["suck", "up", "right", "down", "left"]

		for action in actions:

			new_heuristic_cost = 0
			if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
				new_heuristic_cost -= 3
			if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
				new_heuristic_cost -= 3
			if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
				new_heuristic_cost -= 3
			if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
				new_heuristic_cost -= 3
 
 			if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
				new_heuristic_cost -= 1
			if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
				new_heuristic_cost -= 1
			if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
				new_heuristic_cost -= 1
			if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
				new_heuristic_cost -= 1			


			if action == "suck" and self.state.agent_coordinate in self.state.dirt_list:			
				indx = self.state.dirt_list.index(self.state.agent_coordinate)
				new_dirt_list = self.state.dirt_list[:indx] + self.state.dirt_list[indx+1:]
				
				new_agent_coordinate = copy.deepcopy(self.get_agent_coordinate())
				new_state = State(new_agent_coordinate, new_dirt_list)
				
				new_path_cost = self.path_cost + 1
				new_action = "suck"				
				new_heuristic_cost -= 10
				new_node = Node(new_state, self, new_action, new_path_cost, matrix_size, self.heuristic_cost + new_heuristic_cost)
				child_nodes.append(new_node)
			else:
				if action == "up" and self.state.agent_coordinate[0] != 0:
					temp = self.state.dirt_list
					if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
						new_heuristic_cost -= 5
					if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
						new_heuristic_cost += -2
					if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
						new_heuristic_cost += -2								
					child_nodes.append(Node(State([self.state.agent_coordinate[0] - 1, self.state.agent_coordinate[1]], temp), self, action, self.path_cost + 2, matrix_size, self.heuristic_cost + new_heuristic_cost))
				elif action == "left" and self.state.agent_coordinate[1] != 0:
					temp = self.state.dirt_list
					if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
						new_heuristic_cost -= 5
					if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
						new_heuristic_cost += -2
					if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
						new_heuristic_cost += -2								
					child_nodes.append(Node(State([self.state.agent_coordinate[0], self.state.agent_coordinate[1] - 1], temp), self, action, self.path_cost + 2, matrix_size, self.heuristic_cost + new_heuristic_cost))
				elif action == "down" and self.state.agent_coordinate[0] != matrix_size - 1:
					temp = self.state.dirt_list
					if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
						new_heuristic_cost -= 5
					if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
						new_heuristic_cost += -2
					if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] - 1] in self.state.dirt_list:
						new_heuristic_cost += -2								
					child_nodes.append(Node(State([self.state.agent_coordinate[0] + 1, self.state.agent_coordinate[1]], temp), self, action, self.path_cost + 2, matrix_size, self.heuristic_cost + new_heuristic_cost))
				elif action == "right" and self.state.agent_coordinate[1] != matrix_size - 1:
					temp = self.state.dirt_list
					if [self.get_agent_coordinate()[0], self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
						new_heuristic_cost -= 5
					if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1] + 1] in self.state.dirt_list:
						new_heuristic_cost += -5
					if [self.get_agent_coordinate()[0] + 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
						new_heuristic_cost += -2
					if [self.get_agent_coordinate()[0] - 1, self.get_agent_coordinate()[1]] in self.state.dirt_list:
						new_heuristic_cost += -2

					child_nodes.append(Node(State([self.state.agent_coordinate[0], self.state.agent_coordinate[1] + 1], temp), self, action, self.path_cost + 2, matrix_size, self.heuristic_cost + new_heuristic_cost))
			
		# child = self.find_max(child_nodes)

		return child_nodes

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

def gbs2(root_state, goal_state, matrix_size):

	if(root_state == goal_state):
		return [], 0

	root_node = Node(root_state, None, None, 0, matrix_size, 0)
	frontier = []
	explored = {}
	frontier.append(root_node)
	explored[root_node] = 0

	k, z = 0, 0
	while len(frontier) > 0:
		k += 1
		if k == 100000:
			k = 0
			z += 1
			print(z)
		
		# frontier.sort(key = lambda x: x.heuristic_cost)
		node = frontier.pop()
		children = node.children(matrix_size)
		children.sort(key = lambda x: x.heuristic_cost, reverse = True)
		for child in children:
			if child.state not in explored:
				if child.state == goal_state:
					return solution(child, goal_state)
				else:
					frontier.append(child)
					explored[child.state] = child.path_cost
			else:
				if explored[child.state] >= child.path_cost:
					explored[child.state] = child.path_cost
					frontier.append(child)
	return None

if __name__ == "__main__":

	goal_dirt_list = []
	root_dirt_list = [[0,0], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
	goal_state = State([2, 2], goal_dirt_list)
	root_state = State([0, 0], root_dirt_list)
	action_list, path_cost = gbs(root_state, goal_state, 3)
	print(action_list, path_cost)