import time
import copy

# Get the initial node state from the .txt file
def get_initial_node(file):
    with open(file) as f:
        array = [[int(x) for x in line.split()] for line in f]
    return array

# Convert the row-wise matrix to column wise for storing in the node files
def column_format(node_state):
    arr = []
    for i in range(3):
        for j in range(3):
            arr.append(node_state[j][i])
    return arr

def backtrack(node_idx, parent_nodes, node_list):
    final_list = [node_idx]
    node = node_idx

    while node != 0:
        node = parent_nodes[node]
        final_list.append(node)
    traversed_path = traversal_path(copy.deepcopy(final_list), node_list)
    save_data(node_list, traversed_path, parent_nodes)
    return final_list

def traversal_path(final_list, node_list):
    traversal = []
    length = len(final_list)
    for i in range(length):
        idx = final_list[-1]
        traversal.append(node_list[idx])
        final_list.pop()
    return traversal

def save_data(node_list, node_path, parent_nodes):
    # all nodes
    path_file = open('data/Nodes.txt', 'w')
    for node in node_list:
        col_node = column_format(node)
        for i in col_node:
            path_file.writelines("%s " % i)
        path_file.writelines("\n")

    # final traversal
    path_file = open('data/nodePath.txt', 'w')
    for node in node_path:
        col_node = column_format(node)
        for i in col_node:
            path_file.writelines("%s " % i)
        path_file.writelines("\n")
    
    # index of nodes and parents of final traversal
    path_file = open('data/NodeInfo.txt', 'w')
    path_file.writelines("Node_index      Parent_Node_index       Cost\n")
    for node in range (1, len(node_list)):
            path_file.writelines("\t%s\t\t"%node)
            path_file.writelines("%s\t\t0\n"%parent_nodes[node])
# get the position of the element 0 in the node
def get_blank(data):
    length = len(data)
    idx = (length-1, length-1)
    for i in range(len(data)):
        for j in range(len(data)):
            if (data[i][j] == 0):
                idx = (i, j)
                break
    return idx

def move_down(data, idx_of_blank):
    i = idx_of_blank[0]
    j = idx_of_blank[1]
    data[i][j] = data[i+1][j]
    data[i+1][j] = 0
    return data

def move_up(data, idx_of_blank):
    i = idx_of_blank[0]
    j = idx_of_blank[1]
    data[i][j] = data[i-1][j]
    data[i-1][j] = 0
    return data

def move_right(data, idx_of_blank):
    i = idx_of_blank[0]
    j = idx_of_blank[1]
    data[i][j] = data[i][j+1]
    data[i][j+1] = 0
    return data

def move_left(data, idx_of_blank):
    i = idx_of_blank[0]
    j = idx_of_blank[1]
    data[i][j] = data[i][j-1]
    data[i][j-1] = 0
    return data

# Create a list of child nodes for a particular parent node
def get_children(data, visited):
    length = len(data)
    idx = get_blank(data)

    changed_data = list()
    # shift left 
    if (idx[1] > 0): 
        left_data = move_left(copy.deepcopy(data), idx)
        if left_data not in visited:
            changed_data.append(left_data)

    # shift right
    if (idx[1] < length-1):
        right_data = move_right(copy.deepcopy(data), idx)
        if right_data not in visited:
            changed_data.append(right_data)

    # move up
    if (idx[0] > 0): 
        up_data = move_up(copy.deepcopy(data), idx)
        if up_data not in visited:
            changed_data.append(up_data)

    # move down
    if (idx[0] < length-1): 
        down_data = move_down(copy.deepcopy(data), idx)
        if down_data not in visited:
            changed_data.append(down_data)

    return changed_data

def bfs_search(start):

    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]

    print("Start node:", start)
    print("Goal node", goal, "\n")

    visited = []
    node_idx = 0
    que = [start]
    node_list = []
    parent_nodes = {}
    node_list.append(start)

    if start == goal:
        backtrack(node_idx, parent_nodes, node_list)
        return True

    while (que):

        curr = que.pop(0)

        # Get index of the current node and consider it as the parent node
        parent_index = node_list.index(curr)

        if curr not in visited:
            visited.append(curr)
            children = get_children(curr, visited)

            for child in children:
                if child not in visited:

                    node_idx += 1
                    que.append(child)

                    node_list.append(child)
                    parent_nodes[node_idx] = parent_index

                    # Check if goal has been reached
                    if child == goal:
                        backtrack(node_idx, parent_nodes, node_list)
                        return True
    return False

input_file = 'data/start_node.txt'
start_node = get_initial_node(input_file)

##### Change the initial node manually here #####
# start_node = [[1, 5, 2],
#               [4, 0, 3],
#               [7, 8, 6]]

start_time = time.time()
if(bfs_search(start_node)):
    print("Path Found in",time.time() - start_time,"seconds!")
else:
    print("Path Not Found")
