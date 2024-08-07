def subsetSum(n, W, weights):
    # Create a 2D table to store results of subproblems
    # M[i][w] will be True if a subset of the first i items has a sum w
    M = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Initialize the table: a sum of 0 is always possible with any number of items
    for i in range(n + 1):
        M[i][0] = 0
    
    # Fill the table M[][]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:
                # If the weight of the current item is more than the current sum w,
                # we can't include this item. So, take the value from the previous row.
                M[i][w] = M[i - 1][w]
            else:
                # Otherwise, check if the sum can be achieved by either:
                # 1. Excluding the current item (M[i-1][w])
                # 2. Including the current item (M[i-1][w - weights[i-1]])
                M[i][w] = M[i - 1][w] or M[i - 1][w - weights[i - 1]]
    
    # Backtracking to find the items included in the subset
    subset = []
    i, w = n, W
    while i > 0 and w > 0:
        # If the value in the current cell is not the same as the value in the cell above,
        # it means the current item is included in the subset
        if M[i][w] != M[i - 1][w]:
            subset.append(weights[i - 1])
            w -= weights[i - 1]
        i -= 1

    subset.reverse()  # To maintain the original order of weights
    return M[n][W], subset

# Input from the user
n = int(input("Enter the number of elements: "))
weights = [int(input(f"Enter weight {i + 1}: ")) for i in range(n)]
W = int(input("Enter the target sum: "))

# Check for subset sum and get the result
exists, subset = subsetSum(n, W, weights)

if exists:
    print(f"A subset with sum {exists} exists: {subset}")
else:
    print(f"No subset with sum {W} exists.")
