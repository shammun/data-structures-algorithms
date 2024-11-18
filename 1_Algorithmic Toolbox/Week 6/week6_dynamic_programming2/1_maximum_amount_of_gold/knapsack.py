from sys import stdin

import numpy as np


def maximum_gold(capacity, weights):
    # write your code here

    matrix = np.zeros(shape=(len(weights), capacity + 1), dtype=int)

    for j in range(0, len(weights)):
        for i in range(1, capacity + 1):
            if weights[j] > i:
                matrix[j, i] = matrix[j - 1, i]
            else:
                matrix[j, i] = max(weights[j] + matrix[j - 1, i - weights[j]], matrix[j - 1, i])
    return matrix[len(weights) - 1, capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
