def knapsack(items, maxWeight):
    # Number of items
    n = len(items)

    # Create a 2D list to store the maximum value at each weight from 0 to maxWeight
    dp = [[0] * (maxWeight + 1) for i in range(n + 1)]

    # Build the dp table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(maxWeight + 1):
            # If the weight of the current item is less than or equal to the current capacity w
            if items[i - 1][1] <= w:
                # Include the item and compare the maximum value with or without the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][1]] + items[i - 1][2])
            else:
                # Exclude the current item
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find the items included in the knapsack
    w = maxWeight
    selected = []
    for i in range(n, 0, -1):
        # If the value in dp[i][w] is different from dp[i-1][w], the item i-1 is included
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= items[i - 1][1]

    # Reverse the list to maintain the original order of items
    selected.reverse()

    # Return the maximum value and the list of selected items
    return dp[n][maxWeight], selected

# List of items (item id, weight, value)
items = [(1, 5, 100), (2, 7, 300), (3, 8, 200), (4, 10, 100), (5, 5, 200), (6, 2, 100)]

# Maximum weight capacity of the knapsack
maxWeight = 20

# Compute the maximum value and the selected items
maxValue, selected = knapsack(items, maxWeight)

# Print the results
print("Maximum Value:", maxValue)
print("Selected Items:", selected)
