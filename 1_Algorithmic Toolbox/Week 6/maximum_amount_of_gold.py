def maximum_amount_of_gold(W, weights):
    n = len(weights)
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            dp[i][w] = dp[i-1][w]

            if weights[i-1] <= w:
                val = dp[i-1][w-weights[i-1]] + weights[i-1]
                if dp[i][w] < val:
                    dp[i][w] = val

    return dp[n][W]

if __name__ == '__main__':
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))

    print(maximum_amount_of_gold(W, weights))