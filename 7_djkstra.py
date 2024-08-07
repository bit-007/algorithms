def Dijkstras(graph, src, V):
    # Initialize the shortest paths from the source to all vertices as infinity
    shortest_path = [float('inf')] * V
    shortest_path[src] = 0  # Distance from the source to itself is 0

    # Priority queue to track vertices and their current shortest distance from the source
    queue = [(0, src)]  # (distance, vertex)

    # Process vertices in the priority queue
    while queue:
        current_distance, u = queue.pop(0)

        # If the current path to u is longer than the shortest known path, skip it
        if current_distance > shortest_path[u]:
            continue

        # Explore neighbors of vertex u
        for neighbor, weight in graph[u]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update shortest_path and add to queue
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                queue.append((distance, neighbor))

    # Print the shortest paths from the source vertex to all vertices
    print("\nVertex\tDistance from source")
    for i in range(V):
        print(f"{i}\t\t{shortest_path[i]}")

# Input from the user
V = int(input("\nEnter number of vertices: "))
graph = [[] for _ in range(V)]

E = int(input("Enter the number of edges: "))
for _ in range(E):
    print("Enter edge (u, v): ")
    u = int(input())
    v = int(input())
    weight = int(input("Enter its weight: "))
    # Add edges to the graph as adjacency list representation
    graph[u].append((v, weight))
    graph[v].append((u, weight))  # For undirected graph, add the reverse edge as well

# Print the adjacency list representation of the graph
print("\nAdjacency list:")
for i in range(V):
    print(f"{i}: {graph[i]}")

# Input the source vertex
src = int(input("\nEnter source vertex: "))

# Run Dijkstra's algorithm and print the shortest paths
Dijkstras(graph, src, V)
