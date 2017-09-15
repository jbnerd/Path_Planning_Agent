##########################
# Abhishek V Joshi
# 2015A7PS0116P
##########################

import copy

# Definitions used in Iterative Deepening Search
class State(object):
	"""docstring for State"""
	
	def __init__(self, agent_coordinate, dirt_list):
		self.agent_coordinate = agent_coordinate
		self.dirt_list = dirt_list
			
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
	
	def __init__(self, state, parent, action, path_cost, matrix_size, depth):
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
		self.depth = depth

	def __str__(self):
		return str(self.parent) + str(self.action) + str(self.path_cost) + str(self.depth)

	def __repr__(self):
		return str(self.parent) + str(self.action) + str(self.path_cost) + str(self.depth)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__
	
	# successors function
	def children(self, matrix_size):
		child_nodes = []

		if self.state.dirt_list is not None and self.state.agent_coordinate in self.state.dirt_list:
			"""if len(self.state.dirt_list) == 1:
				new_dirt_list = []
			else:"""
			# new_dirt_list = self.state.dirt_list.remove(self.state.agent_coordinate)
			indx = self.state.dirt_list.index(self.state.agent_coordinate)
			new_dirt_list = self.state.dirt_list[:indx] + self.state.dirt_list[indx+1:]
			new_agent_coordinate = copy.deepcopy(self.state.agent_coordinate)
			new_state = State(new_agent_coordinate, new_dirt_list)
			new_path_cost = self.path_cost + 1
			new_action = "suck"
			new_node = Node(new_state, self, new_action, new_path_cost, matrix_size, self.depth + 1)
			child_nodes.append(new_node)
		else:
			actions = ["up", "right", "down", "left"]
			for action in actions:
				if action == "up" and self.state.agent_coordinate[0] != 0:
					temp = self.state.dirt_list
					child_nodes.append(Node(State([self.state.agent_coordinate[0] - 1, self.state.agent_coordinate[1]], temp), self, action, self.path_cost + 2, matrix_size, self.depth + 1))
				elif action == "left" and self.state.agent_coordinate[1] != 0:
					temp = self.state.dirt_list
					child_nodes.append(Node(State([self.state.agent_coordinate[0], self.state.agent_coordinate[1] - 1], temp), self, action, self.path_cost + 2, matrix_size, self.depth + 1))
				elif action == "down" and self.state.agent_coordinate[0] != matrix_size - 1:
					temp = self.state.dirt_list
					child_nodes.append(Node(State([self.state.agent_coordinate[0] + 1, self.state.agent_coordinate[1]], temp), self, action, self.path_cost + 2, matrix_size, self.depth + 1))
				elif action == "right" and self.state.agent_coordinate[1] != matrix_size - 1:
					temp = self.state.dirt_list
					child_nodes.append(Node(State([self.state.agent_coordinate[0], self.state.agent_coordinate[1] + 1], temp), self, action, self.path_cost + 2, matrix_size, self.depth + 1))
		return child_nodes