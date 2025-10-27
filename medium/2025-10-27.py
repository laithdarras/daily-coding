"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""

# UNDERSTAND
# I need to find the minimum number of perfect squares that will sum up to n
# This is a good problem involving math and dynamic programming
# Can do so recursively or iteratively, i will see which one i will use
# edge cases include if n is 0, then return 0. if n is negative, return -1 bc we cant have negative squares

# MATCH
# I will solve this problem using dynamic programming with arithmetic operations

# PLAN
# 0. Base case 
# 1. Initialize a dp list of size n+1 and set all values to n (worst case scenario)
# 2. Set the first index of the list to 0 bc 0 can be represented by 0 squares
# 3. Loop through each number 
# 4. Perform a nested loop to check for all perfect squares that are less than or equal to the current number
# 5. Update the dp list with the minimum number of squares needed to represent n
# 6. Return value

# IMPLEMENT

def minSquares(n):
    # Base case

    if n == 0:
        return 0
    elif n < 0:
        return -1
    
    # DP
    dp = [n] * (n+1) # N is the worst case senario and n+1 is the size of the list and we multiply by n to fill the list with n

    dp[0] = 0

    # Loops
    for i in range(1, n+1): # from second element to last
        for j in range(1, i+1): # from 1 to current number
            square = j * j
            # Check if square is <= curr
            if square <= i:
                dp[i] = min(dp[i], dp[i - square] + 1)  # Update list with min squares needed
            else:
                break # no need to check further if square exceeds the current number

    return dp[n] # Return the last element which contains the answer

print(minSquares(13))
print(minSquares(27))

# My solution runs in O(N*SQRT(N)) time complexity. The outer loops runs N times and the inner loops runs up to SQRT(N) times because it stops when the square exceeds the current number
# Space complexity would be O(N) bc of the dp list
# DP problems are fun and interesting because I can break a larger problem into smaller subproblems like this one
# The larger problem would be to find the min squares for n, and I broke it down into finding the min squares for all numbers leading up to n
# Iterative > Recursive for this problem because it avoid putting too many calls on the stack 