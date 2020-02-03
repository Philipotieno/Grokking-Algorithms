graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# the cost table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# The parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_node = float("inf")
    lowest_cost_node = None
    
    # Go through each node
    for node in costs:
        cost = costs[node]
        # If its the lowest cost so far an has not been processed
        if cost < lowest_node and node not in processed:
            # Set it as the lowest -cost node
            lowest_cost = cost
            lowest_cost_node =node
        return lowest_cost_node
    
# find the lowest cost node that you havent processed yet
node = find_lowest_cost_node(costs)
# If you have processed all the nodes this while loop is done
while node is not None:
    cost = costs[node]
    #  go through all  the neighbors of this node
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = neighbors[n]
        # If its cheaper to get to this neighbor by going through this node
        if costs[n] > new_cost:
            # Update the cost for this node
            costs[n] > new_cost
            # this node becomes the new the new parent for this neighbor
            parents[n] = node
    # Mark the node as processed
    processed.append(node)
    # find the next node to process and loop
    node = find_lowest_cost_node(costs)
    
print("Costs from the start to each node:")
print(cost)