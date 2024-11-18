def knapsack_with_repetitions(W, weights, values):
    # Initialize the value array with zeros
    value = [0] * (W + 1)

    for w in range(1, W + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                val = value[w - weights[i]] + values[i]
                if val > value[w]:
                    value[w] = val
    
    return value, value[W]

if __name__ == '__main__':
    # Example usage
    W = int(input())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))
    list, values = knapsack_with_repetitions(W, weights, values)
    print(list)
    print(values)
