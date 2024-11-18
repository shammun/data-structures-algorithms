from sys import stdin

def optimal_loot(capacity, weights, values):
    value = 0
    
    for i in range(len(values)):
        if capacity == 0:
            return value
        max_value = [value/weight for value, weight in zip(values, weights)]
        max_index = max_value.index(max(max_value))
        amount = min(weights[max_index], capacity)
        value += amount * max_value[max_index]
        del weights[max_index]
        del values[max_index]
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2: (2*n + 2): 2]
    weights =data[3: (2*n + 2): 2]
    print("{:.6f}".format(optimal_loot(capacity, weights, values)))
