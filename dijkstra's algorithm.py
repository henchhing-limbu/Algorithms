graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# print(graph) 
# {'start': {'a': 6, 'b': 2}}
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # The finish node doesn't have any neighbors

# representing infinity in python
infinity = float("inf")

# making cost table
# representing infinity in python
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# list to keep track of all the processed nodes
processed = []

# algorithm
node = find_lowest_cost_node(costs)
# loops until all the nodes have been processed
while node is not None:
    cost  = costs[node]
    neighbors = graph[node]
    # go through all the neighbors of this node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # if it's cheaper to get to this neighbor by going thruough this node
        if costs[n] > new_cost:
            # update the cost for this node
            costs[n] = new_cost
            # this node becomes the new parent for this neighbor
            parents[n] = node
    # mark this node as processed
    processed.append(node)
    # find the next node to process, and loop
    node = find_lowest_cost_node(costs)

#
def find_lowest_cost_node(costs):
    lowest_cost = float("int")
    lowest_cost_node = None
    # go through each node
    for node in costs:
        cost = costs[node]
        # if it's the lowest cost so far and hasn't been processed yet
        if cost < lowest_cost and node not in processed:
            # set it as the new lowest cost node
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node
        
    
