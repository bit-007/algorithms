def find(parent, i):
    """
    :param parent: A list where parent[i] is the parent of i.
    :param i: The element to find the root of.
    :return: The root of the set containing i.
    """
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def Kruskals(graph, V):
    mst=[]
    # Sort the edges based on their weight
    graph = sorted(graph, key=lambda item: item[2])
    
    # Initialize parent and rank arrays
    parent = [i for i in range(V)]
    cost, edges, i = 0, 0, 0
    
    # Iterate through the sorted edges
    while edges < V - 1:
        # Get the next edge from the sorted list
        u, v, weight = graph[i]
        i += 1
        
        # Find the roots of the sets that u and v belong to
        x, y = find(parent, u), find(parent, v)
        
        # If the roots are different, the edge doesn't form a cycle
        if x != y:
            edges += 1
            # Add the edge to the MST
            mst.append([u, v, weight])
            # Union the two sets
            parent[y] = parent[x]
            # Add the weight of the edge to the cost
            cost += weight
    
    # Print the resulting Minimum Spanning Tree and its cost
    print("\nMinimum Spanning Tree: ", mst)
    print("\nMinimum Spanning Tree Cost: ", cost)

# Input number of vertices and edges
V = int(input("\nEnter no of vertices: "))
graph = []
E = int(input("\nEnter the no of edges: "))

# Input edges and their weights
print("Enter edges and their weight separated by space (u v weight)")
for i in range(E):
    u, v, weight = map(int, input(f"Edge {i+1}: ").split())
    graph.append([u, v, weight])

# Compute and print the Minimum Spanning Tree using Kruskal's algorithm
Kruskals(graph, V)
