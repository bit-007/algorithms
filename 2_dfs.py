def DFS(arr, visited, start, vertices):
    # Mark the starting vertex as visited
    visited[start] = 1
    # Print the starting vertex
    print(start)
    
    # Explore all adjacent vertices of the current vertex
    for j in range(vertices):
        # If there is an edge between the current vertex and vertex j
        if arr[start][j] == 1:
            # If vertex j has not been visited
            if visited[j] == 0:
                # Recursively call DFS for vertex j
                DFS(arr, visited, j, vertices)

# Input the number of vertices
n = int(input("Enter number of vertices: "))

# Initialize visited list to keep track of visited vertices
visited = [0 for i in range(n)]

# Input the number of edges
e = int(input("Enter the number of edges: "))

# Initialize adjacency matrix
arr = [[0 for i in range(n)] for j in range(n)]

# Input edges and fill the adjacency matrix
for i in range(e):
    print("Enter edge (u, v): ")
    vi = int(input())
    vj = int(input())
    arr[vi][vj] = 1
    arr[vj][vi] = 1  # Since the graph is undirected

# Print the adjacency matrix
print("Adjacency matrix: ", arr)

# Input the starting vertex for DFS
strt = int(input("Enter starting vertex: "))

# Perform DFS traversal starting from the given vertex
print("DFS: ")
DFS(arr, visited, strt, n)
