import heapq
# Define the A* search function
def a_star_search(graph, start, goal, heuristic1):
    # Initialize the open list with the start node and a cost of 0
    open_list = [(0, start)]
    # Initialize the closed set (the set of nodes we've already visited)
    closed_set = set()
    # Initialize the g_score dictionary with infinity for all nodes
    g_score = {location: float('inf') for location in graph}
    # The cost to reach the start node is 0
    g_score[start] = 0

    # Main loop
    while open_list:
        # Pop the node with the lowest cost from the open list
        current_g,current_node = heapq.heappop(open_list)
        print(current_node)
        print(g_score)
        # If this node is the goal, we're done
        if current_node == goal:
            return g_score[goal]
        # If we've already visited this node, skip it
        if current_node in closed_set:
            continue
        # Mark this node as visited
        closed_set.add(current_node)

        # Explore the neighbors of the current node
        for neighbor, distance in graph[current_node].items():
            # Calculate the cost to reach this neighbor
            tentative_g = g_score[current_node] + distance
            # If this cost is less than the previously calculated cost, update it
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                # Calculate the f_score and add the neighbor to the open list
                f_score = tentative_g + heuristic1[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
        # print(current_node)
        # print(closed_set)
        # print(open_list)
        print(heapq)
    # If we get here, there's no path from start to goal
    return float('inf')

# Define the map
example_map = {
'S': {'A':1,'G':10},
'A': {'B':2, 'C':1, 'S':1},
'B': {'D':5, 'A':2},
'C': {'D':3, 'G':4, 'A':1},
'D': {'G':2, 'C':3, 'B':5},
'G': {'S':10, 'C':4, 'D':2},
}
# Define the heuristic function (straight-line distance to G)
heuristic1 = {
'S': 5,
'A': 3,
'B': 4,
'C': 2,
'D': 6,
'G': 0}

# Find the shortest path from 'S' to 'G'
shortest_distance = a_star_search(example_map, 'S', 'G', heuristic1)
if shortest_distance < float('inf'):
    print(f"The shortest distance from S to G is {shortest_distance}.")
else:
    print("No path found from S to G.")


