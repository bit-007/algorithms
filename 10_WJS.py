def compute_p(lst):
    p = [0] * len(lst)
    for i in range(len(lst)):
        for j in range(i - 1, -1, -1):
            if lst[j][1] <= lst[i][0]:  # if job j finishes before job i starts
                p[i] = j + 1
                break
    return p

def m_compute_opt(j, lst, p, M):
    if M[j] is not None:
        return M[j]
    if j == 0:
        M[j] = 0
    else:
        M[j] = max(lst[j-1][2] + m_compute_opt(p[j-1], lst, p, M), m_compute_opt(j-1, lst, p, M))
    return M[j]

if __name__ == "__main__":
    # Input handling
    n = int(input("Enter number of jobs: "))
    lst = []
    print("Enter start time, finish time, and profit of each job separated by space")
    for i in range(n):
        tup = tuple(map(int, input(f"Job {i+1}: ").split()))
        lst.append(tup)
    
    # Sort jobs by finish times
    lst.sort(key=lambda x: x[1])
    
    # Compute the predecessor array
    p = compute_p(lst)
    
    # Initialize the memoization array
    M = [None] * (n + 1)
    
    # Compute the maximum profit
    max_profit = m_compute_opt(n, lst, p, M)
    print("\nMax profit:", max_profit)
