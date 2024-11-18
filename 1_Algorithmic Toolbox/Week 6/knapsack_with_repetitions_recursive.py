def knapsack_with_repetitions_recursive(W, weights, values, memo):
    if W in memo:
        return memo[W]
    
    if W == 0:
        return 0
    
    max_value = 0
    for i in range(len(weights)):
        if weights[i] <= W:
            val = knapsack_with_repetitions_recursive(W - weights[i], weights, values, memo) + values[i]
            if val > max_value:
                max_value = val
            
    memo[W] = max_value
    return max_value

if __name__ == '__main__':
    W = int(input())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))

    memo = {}
    max_value = knapsack_with_repetitions_recursive(W, weights, values, memo)
    print(memo)
    print(max_value)