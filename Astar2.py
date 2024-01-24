import heapq

def a_star_search(graph, start, goal, heuristic1):
    open_list = [(0,start)]
    closed_list = set()
    # score to reach that point
    actual_dist_of_node = {location:float('inf') for location in graph}
    actual_dist_of_node[start] = 0
    print(actual_dist_of_node)
    # heapq.heappush(open_list)
    while open_list:
        print(heapq)
        current_node = heapq.heappop(open_list)
        print(current_node)
        if(current_node[1]==goal):
            return current_node[0]
        if(current_node[1] in closed_list):
            print("Already Visited")
            continue
        closed_list.add(current_node[1])
        for neighbor,distance_to_neighbour_node in graph[current_node[1]].items():
            distance_till_node = actual_dist_of_node[current_node[1]] + distance_to_neighbour_node
            new_dist = distance_till_node+heuristic1[neighbor]
            if(new_dist<actual_dist_of_node[neighbor]):
                print(new_dist,actual_dist_of_node[neighbor])
                actual_dist_of_node[neighbor]=new_dist
                f_distance = new_dist + heuristic1[neighbor]
                print(f_distance,new_dist,actual_dist_of_node[neighbor])
                heapq.heappush(open_list,(f_distance,neighbor))
                        #     print(new_dist)
        # print(heapq)
        # print("hi")
    return float('inf')

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


