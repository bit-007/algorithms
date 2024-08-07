# Define a large value representing infinity for edge weights
INF = 999

# Function to perform Prim's algorithm on a graph represented by an adjacency matrix
def Prims(G, visited, V): 
    # Initialize the number of edges in the MST and the total cost of the MST
    edges, cost = 0, 0
    
    # Start from the first vertex
    visited[0] = True
    
    print("Edge: Weight")
    
    # Loop until we have V-1 edges in the MST
    while (edges < V - 1):
        # Initialize the minimum edge weight and the vertices it connects
        minimum, x, y = INF, 0, 0
        
        # Traverse all vertices to find the minimum weight edge
        for i in range(V):
            if visited[i]:  # If the vertex is in the MST
                for j in range(V):
                    # If the vertex j is not visited and there is an edge from i to j
                    if ((not visited[j]) and G[i][j]):
                        # Update the minimum edge if the current edge is smaller
                        if minimum > G[i][j]:
                            minimum, x, y = G[i][j], i, j
        
        # Print the selected edge and its weight
        print(f"{x} <---> {y}: {G[x][y]}")
        
        # Mark the vertex y as visited
        visited[y] = True
        
        # Add the weight of the selected edge to the total cost
        cost += G[x][y]
        
        # Increment the number of edges in the MST
        edges += 1
    
    # Print the total cost of the minimum spanning tree
    print("Cost of minimum spanning tree:", cost)

# Get the number of vertices from the user
n = int(input("\nEnter the number of vertices: "))
# Initialize a list to keep track of visited vertices
visited = [0 for i in range(n)]

# Initialize the adjacency matrix with INF (except for the diagonal elements which are 0)
arr = [[INF for i in range(n)] for j in range(n)]
for i in range(n):
    arr[i][i] = 0

# Get the number of edges from the user
e = int(input("Enter the number of edges: "))
# Read each edge and its weight from the user
for i in range(e):
    print("Enter edge (u, v): ")
    u = int(input())  # Start vertex of the edge
    v = int(input())  # End vertex of the edge
    weight = int(input("Enter its weight: "))  # Weight of the edge
    # Update the adjacency matrix with the weight of the edge
    arr[u][v], arr[v][u] = weight, weight

# Print the adjacency matrix
print("\nAdjacency matrix: ")
for i in range(n):
    print(arr[i])

# Perform Prim's algorithm and print the results
print("\nPrims: ")
Prims(arr, visited, n)
