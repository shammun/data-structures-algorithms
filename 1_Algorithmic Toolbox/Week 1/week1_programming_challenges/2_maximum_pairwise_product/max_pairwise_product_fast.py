
def max_pairwise_product_naive(arr):
    """
    Calculates the maximum pairwise product of a list of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum pairwise product of the list.
    """
    product = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = max(product, arr[i] * arr[j])
    return product

def max_pairwise_product_fast(arr):
    """
    Calculates the maximum pairwise product of a list of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum pairwise product of the list.
    """
    arr.sort()
    return arr[-1] * arr[-2]

from random import randint
def max_product_stress(n, m):
    """
    Stress tests the max_pairwise_product_fast function.

    Args:
        n (int): The number of integers in the list.
        m (int): The maximum value of an integer in the list.
    """

    arr = [randint(0, m) for _ in range(n)]
    naive = max_pairwise_product_naive(arr)
    fast = max_pairwise_product_fast(arr)
    if naive == fast:
        print('OK')
    else:
        print(f'Wrong answer: {naive}, {fast}')


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    # n = randint(0, 200)
    # m = randint(8, 10)
    # max_product_stress(n, m)
    print(max_pairwise_product_fast(input_numbers))