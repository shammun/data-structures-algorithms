def knapsack(W, weights, values, n):
    # Initialize the DP table with 0
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # If not including the current item
            dp[i][w] = dp[i-1][w]
            
            # If including the current item
            if weights[i-1] <= w:
                val = dp[i-1][w - weights[i-1]] + values[i-1]
                if dp[i][w] < val:
                    dp[i][w] = val

        # Print the current state of the dp table
            print(f"After considering item {i} with weight {weights[i-1]} and value {values[i-1]} for weight position {w}:")
            for row in dp:
                print(row)
            print()

    return dp[n][w]

if __name__ == "__main__":
    # Ask for user input
    W = int(input())
    n = int(input())

    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    
    max_value = knapsack(W, weights, values, n)
    print("Maximum value in knapsack:", max_value)
