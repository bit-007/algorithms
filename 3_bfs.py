def BFS(arr, visited, i, n):
    queue = []  # Initialize an empty queue
    visited[i] = 1  # Mark the starting vertex as visited
    print(i)  # Print the starting vertex
    queue.append(i)  # Add the starting vertex to the queue

    # Process the queue until it is empty
    while len(queue) != 0:
        vertex = queue.pop(0)  # Dequeue a vertex from the front of the queue
        
        # Traverse all adjacent vertices of the dequeued vertex
        for j in range(n):
            if arr[vertex][j] == 1:  # If there is an edge between vertex and j
                if visited[j] == 0:  # If vertex j has not been visited
                    visited[j] = 1  # Mark vertex j as visited
                    print(j)  # Print vertex j
                    queue.append(j)  # Enqueue vertex j

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
print("Adjacency matrix: \n", arr)

# Input the starting vertex for BFS
strt = int(input("Enter starting vertex: "))

# Perform BFS traversal starting from the given vertex
print("BFS: ")
BFS(arr, visited, strt, n)
