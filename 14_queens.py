def backtrack(r, n):
    # If we have placed queens in all rows, add the current board configuration to the result
    if r == n:
        res.append([" ".join(row) for row in board])
        return
    
    # Try placing a queen in each column of the current row
    for c in range(n):
        # Skip columns, secondary diagonals, and primary diagonals that are already occupied
        if c in col or (r + c) in secDiag or (r - c) in priDiag:
            continue
        
        # Place the queen on the board
        col.add(c)
        secDiag.add(r + c)
        priDiag.add(r - c)
        board[r][c] = 'Q'

        # Move to the next row
        backtrack(r + 1, n)

        # Remove the queen from the board and backtrack
        col.remove(c)
        secDiag.remove(r + c)
        priDiag.remove(r - c)
        board[r][c] = '_'

# Size of the board (n x n)
n = 4

# Sets to track the columns and diagonals that are already occupied
col = set()
priDiag = set()  # (r - c) for primary diagonals
secDiag = set()  # (r + c) for secondary diagonals

# List to store the solutions
res = []

# Initialize the board with empty spaces ('_')
board = [['_'] * n for i in range(n)]

# Start the backtracking algorithm from the first row
backtrack(0, n)

# Print the number of solutions found
print("Number of ways:", len(res))

# Print all the possible arrangements of the board
print("\nPossible arrangements:")
for r in res:
    print(r)
