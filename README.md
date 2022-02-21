# 8-Puzzle
Solves the puzzle to:

    | 1 2 3 |
    | 4 5 6 | 
    | 7 8 0 |

## 1. Dependecies: Libraries used
 1. [time](https://docs.python.org/3/library/time.html) : Library used to check the time taken for solving the puzzle
 2. [copy](https://docs.python.org/3/library/copy.html) : Library used to implement changes in parent node to generate child nodes

## 2. Run the code 
i. Define the start node state in the data/start_node.txt. Edit the node in a row-wise fashion
Example:Edit the start_node.txt file as:

    1 5 2
    4 0 3
    7 8 6

ii. Solve the puzzle

    python3 puzzle_solver.py
iii. Visualize the path taken to solve the puzzle by,

    python3 plot_path.py
## 3. Files
1. data/start_node.txt: Contains the initial node state which is ros-wise
2. puzzle_solver.py: Python file to solve the puzzle
3. plot_path.py: Python file to visualize the tree traversal to reach the goal state
4. data/NodeInfo.txt: Logs the child node states of each parent node
5. data/nodePath.txt: Logs the node states for the traversal
6. data/Nodes.txt: Logs all the nodes that we created for solving the puzzle
## 4. Example: 
The goal state can be changed directly in the bfs_search() function puzzle_solver.py file. 

Start node state

    | 1 | 5 | 2 |
    | 4 | 0 | 3 | 
    | 7 | 8 | 6 |
Step 1

    | 1 | 0 | 2 |
    | 4 | 5 | 3 | 
    | 7 | 8 | 6 |
Step 2

    | 1 | 2 | 0 |
    | 4 | 5 | 3 | 
    | 7 | 8 | 6 |
Step 3

    | 1 | 2 | 3 |
    | 4 | 5 | 0 | 
    | 7 | 8 | 6 |
Achieved Goal Node

    | 1 | 2 | 3 |
    | 4 | 5 | 6 | 
    | 7 | 8 | 0 |


