def BellmanFord(graph, src, V):
    # Initialize distances from the source to all vertices as infinity
    dist = [float('inf')] * V
    # Distance to the source itself is always 0
    dist[src] = 0

    # Relax all edges |V| - 1 times
    for i in range(V - 1):
        # For each edge, update the distance if a shorter path is found
        for edge in graph:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]

    # Check for negative-weight cycles
    for edge in graph:
        if dist[edge[1]] > dist[edge[0]] + edge[2]:
            print("Negative cycle detected")
            return
    
    # Print the result
    print("\nVertex\tDistance from source")
    for i in range(V):
        print(i, "\t", dist[i])

# Input the number of vertices and edges
V = int(input("\nEnter number of Vertices: "))
E = int(input("\nEnter number of directed edges: "))

# Create a graph as a list of edges
graph = []
print("\nEnter adjacency list edges [u, v, weight] separated by space:")
for i in range(E):
    graph.append(list(map(int, input(f"Edge {i + 1}: ").split())))

# Input the source vertex
src = int(input("\nEnter source vertex: "))

# Print the input graph
print("\nGraph:", graph)

# Run the Bellman-Ford algorithm
BellmanFord(graph, src, V)
