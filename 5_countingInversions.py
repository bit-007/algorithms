def sort_and_count(L):
    # Base case: a list of 0 or 1 elements is already sorted, with no inversions
    if len(L) <= 1:
        return L, 0
    # Split the list into two halves
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]
    
    # Recursively sort and count inversions in the left and right halves
    sorted_left, inversions_left = sort_and_count(left)
    sorted_right, inversions_right = sort_and_count(right)
    
    # Merge the two sorted halves and count split inversions
    inversions_split, sorted_list = merge_and_count(sorted_left, sorted_right)
    
    # Total inversions is the sum of left, right, and split inversions
    total_inversions = inversions_left + inversions_right + inversions_split
    return sorted_list, total_inversions

def merge_and_count(A, B):
    merged = []
    i = j = inversions = 0
    
    # Merge two sorted lists A and B
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
            # Count inversions: all remaining elements in A are greater than B[j]
            inversions += len(A) - i
    
    # Append remaining elements (if any)
    merged.extend(A[i:])
    merged.extend(B[j:])
    return inversions, merged

# Function to count inversions in one user's ranking compared to another user's ranking
def count_inversions(base_user, comparison_user):
    # Map songs in comparison_user to their positions in base_user
    mapped_comparison = [base_user.index(song) for song in comparison_user]
    # Count inversions in the mapped comparison
    _, inversions = sort_and_count(mapped_comparison)
    return inversions

# Input rankings for 3 users
users = []
for i in range(3):
    while True:
        try:
            print(f"Enter the ranking for user {i + 1} (8 space-separated integers):")
            user_input = input().strip().split()
            if len(user_input) != 8:
                raise ValueError("Please enter exactly 8 integers.")
            users.append(list(map(int, user_input)))
            break
        except ValueError as e:
            print(e)

# Count inversions between User 1 and User 2
inv_user1_user2 = count_inversions(users[0], users[1])
# Count inversions between User 1 and User 3
inv_user1_user3 = count_inversions(users[0], users[2])
# Count inversions between User 2 and User 3
inv_user2_user3 = count_inversions(users[1], users[2])

# User 1's comparison results
print(f"User 2 has {inv_user1_user2} inversions when compared to User 1.")
print(f"User 3 has {inv_user1_user3} inversions when compared to User 1.")
if inv_user1_user3 < inv_user1_user2:
    print("User 1 has a similar taste to User 3")
elif inv_user1_user2 < inv_user1_user3:
    print("User 1 has a similar taste to User 2")
else:
    print("User 2 and User 3 have the same similarity to User 1")

print()

# User 2's comparison results
inv_user2_user1 = count_inversions(users[1], users[0])
print(f"User 1 has {inv_user2_user1} inversions when compared to User 2.")
print(f"User 3 has {inv_user2_user3} inversions when compared to User 2.")
if inv_user2_user1 < inv_user2_user3:
    print("User 2 has a similar taste to User 1")
elif inv_user2_user3 < inv_user2_user1:
    print("User 2 has a similar taste to User 3")
else:
    print("User 1 and User 3 have the same similarity to User 2")

print()

# User 3's comparison results
inv_user3_user1 = count_inversions(users[2], users[0])
print(f"User 1 has {inv_user3_user1} inversions when compared to User 3.")
print(f"User 2 has {inv_user2_user3} inversions when compared to User 3.")
if inv_user3_user1 < inv_user2_user3:
    print("User 3 has a similar taste to User 1")
elif inv_user2_user3 < inv_user3_user1:
    print("User 3 has a similar taste to User 2")
else:
    print("User 1 and User 2 have the same similarity to User 3")
