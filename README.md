# Path Planning Agent

## Problem Statement

- The environment consists of a 10x10 tiled floor, of which some of the tiles have dirt on them.
- There is an intelligent vacuum cleaner which has the job to find the dirty tiles and clean them. It starts its job from a fixed starting position and finishes it on a fixed ending position,
- The vacuum cleaner has two sensors: one to percieve its own position and the other to percieve the dirt on a tile.
- The actuators are its wheels and dirt-sucking mechanism which gives it the following actions:
	- MR (Move Right)
	- ML (Move Left)
	- MU (Move Up)
	- MD (Move Down)
	- S (Suck the dirt)
	- N (do Nothing)
- The cost of any kind of movement is two units and the cost of dirt sucking is 1 unit.
- The Vacuum Cleaner has to find a path that minimizes the cleaning cost.

## Thinking Approach

- The Problem is posed like a State Search Problem.
- Performance Measure of the Intelligent Agent is its Path Cost.
- The Problem is solved using two kinds of Search Methods:
	- Uninformed Search (Assuming the environment is Globally Observable):
		- Breadth First Search
		- Iterative Deepening Depth First Search
	- Informed Search (Assuming only the immediate neighbor tiles are visible to the agent):
		- Greedy Best First Search using Heuristics

### States

- To generate a State Space for the search, the states are represented as a Python object, which keeps the account of the current agent coordinate and the list of dirty tiles.

### Tree Nodes

- The State space is generated as a Tree.
- The nodes of the tree keep the track of `action`, `state`, `path_cost` and `parent`.
- `Action` : The Action that generates the node.
- `State` : The current state of the node.
- `Path_cost` : The path cost uptill the generation of this node.
- `Parent` : Parent node of the current node.

## Implementation

- The Problem is implemented using `Python2.7.13` using the Standard Internal Libraries.
- Some Linux Machines may not come with `Python-tk` pre-installed. This implementation uses `Turtle` Graphics, which internally uses `Python-tk`.

## Modules

- Dirt Generator:
	- This module generates dirt on random tiles depending upon the percentage parameter that is passed to it.
	- The dirt generator returns the initial state of the room.
- Uninformed Search:
	- Implementations of Breadth First Search and Iterative Deepening Depth First Search.
- Informed Search:
	- Implementation of Greedy Best First Search using two different heuristics.
- GUI module:
	- Intializes the GUI for graphic implementation of the proposed algorithms.

## Rationale for choosing the proposed Algorithms

- Uninformed Search
	- Depth First Search is not chosen because it is not complete.
	- Breadth First Search is implemented becuase it is complete and optimal; also to check the tight memory bounds it faces, due to large size of the Auxilliary Queue (frontier) it uses.
	- Iterative Deepening Search is also complete and optimal. It uses much less memory owing to a Auxilliary Stack Frontier, but it takes untractible time to compute the solution even for reasonably small inputs.

- Informed Search
	- Since the environment is parially observable, hence a Greedy Best First Search approach is used with two different heuristic functions.

## Analysis

### R's

- For IDS:
	- R1 = Numbmer of nodes generated till the problem is solved using Iterative Deepening Search on a 4x4 matrix with 60% dirt on it.
	- R2 = Amount of memory allocated to one node of Tree for IDS.
	- R3 = Maximum size of the Auxiliary Stack used for IDS.
	- R4 = Total cost to clean the room.
	- R5 = Total time taken to compute the path.
- For H1 (Heuristic 1) and H2 (Heuristic 2):
	- R6 = Total number of nodes generated till the problem is solved.
	- R7 = Amount of memory allocated to one node of the Tree.
	- R8 = Costs of paths computed by both the Heuristics.
	- R9 = Total time to compute the paths.
- Comparative Analysis
	- R10 = Total memory used in both types of Searches.
	- R11 = Average path cost after running both the algorithms for 10 times each.

## Graphical Depictions

- Upper Left = Initially depicts the path of the IDS algorithm on a 4x4 board.
- Upper Right = Depicts the paths of Informed Searches, heuristic 1 in Blue and heuristic 2 in Green.
- Lower Left = Depicts the variation of running time of Greedy Best Search with respect to board size varied from 3x3 to 14x14.
- Lower Right = Depicts the variation of running time of Greedy Best Search with respect to percentage of Dirty Tiles on the board increasing from 10% to 100% in the steps of 5%.

## Heuristics

- Both the Heuristics are **Transition** Heuristics and not State Heuristics.

### Heuristic 1 - Immediate Heuristic

- This heuristic assigns scores to each state transition:
	- If the agent is on a dirty tile, assign it a score 10 and suck the dirt.
	- If the agent moves to a dirty tile which is the immediate neighbor, assign it a score of 5. If the immediate neighbour tiles of the new tile which also lie in the percept of the parent tile, then add a score of 3 corresponding to each such tile and a score of 2 if dirt is also present on diagonal neighbors.
	- Do the same cost additions except for the one that adds 5 if the transition occurs to a clean tile.

### Heuristic 2 - Sequential Heuristic

- This heuristic works the same as before, with the difference that it adds the new scores to the heuristic scores of its parent node.

## Running the program

- Type in `python2 run.py` from the required directory into the Linux terminal to fire up the GUI and see the implementation of the algorithms.

