from itertools import permutations

def max_product_naive(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutations[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)
    return max_product

def max_product_efficient(first_sequence, second_sequence):
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    return sum(first_sequence[i] * second_sequence[i] for i in range(len(first_sequence)))

if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks)
    print(max_product_efficient(prices, clicks))