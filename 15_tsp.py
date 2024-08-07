def tsp(graph, v, currPos, n, count, cost, path, answer):
    # If all vertices are visited and there is a path back to the starting vertex
    if count == n and graph[currPos][0]:
        # Add the cost of returning to the start and the path to the answer list
        answer.append((cost + graph[currPos][0], path + [0]))
        return

    # Explore all possible vertices for the next step
    for i in range(n):
        # If the vertex is not visited and there is an edge from the current vertex to this vertex
        if not v[i] and graph[currPos][i]:
            # Mark the vertex as visited
            v[i] = True
            # Recursively call tsp for the next vertex
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i], path + [i], answer)
            # Backtrack: Unmark the vertex as visited
            v[i] = False

if __name__ == '__main__':
    # Read the number of vertices and edges
    n = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    # Initialize the adjacency matrix with zeroes
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    print("Enter the edges:")
    # Read the edges and their weights
    for _ in range(edges):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w  # Assuming the graph is undirected
    
    # Initialize visited list and answer list
    visited = [False] * n
    visited[0] = True  # Start from the first vertex
    answer = []

    # Start TSP from the first vertex
    tsp(graph, visited, 0, n, 1, 0, [0], answer)

    # Find the minimum cost path from all possible paths
    if answer:
        min_cost, min_path = min(answer, key=lambda x: x[0])
        print("Minimum cost of the Hamiltonian Cycle:", min_cost)
        print("Path taken:", " -> ".join(map(str, min_path)))
    else:
        print("No Hamiltonian Cycle found")
