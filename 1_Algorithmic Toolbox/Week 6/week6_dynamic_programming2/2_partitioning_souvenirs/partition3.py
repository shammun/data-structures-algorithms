from sys import stdin
import itertools


def partition3(values):
    for x in itertools.product(range(3), repeat=len(values)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if x[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
