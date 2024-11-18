import random
import sys
import time

def max_pairwise_product(arr):
    """
    Calculates the maximum pairwise product of a list of integers.
    Args:
        arr (list): A list of integers.
    Returns:
        int: The maximum pairwise product of the list.
    """

    n = len(arr)
    assert n >= 2, "Array shold have at least 2 elements"

    product = 0
    for i in range(n):
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

    n = len(arr)
    assert n >=2, "Array should have at least 2 elements"

    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])

    for i in range(2, n):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

    return max1 * max2

def generate_test(n, m):
    """
    Generate a random test case
    Args:
        n (int): The number of integers in the list.
        m (int): The maximum value of an integer in the list.

    Returns:
        list: A list of integers.
    """
    return [random.randint(0, m) for _ in range(n)]

def stress_test(num_tests, max_n, max_m):
    """
    Performs stress testing on the max_pairwise_product functions.
    Args:
        num_tests (int): Number of tests to run.
        max_n (int): Maximum number of elements in the test array.
        max_m (int): Maximum value of elements in the test array.
    """
    for i in range(num_tests):
        print(f"Running test {i+1} of {num_tests}")
        n = random.randint(2, max_n )
        m = random.randint(0, max_m)
        arr = generate_test(n, m)

        start_time = time.time()
        naive_result = max_pairwise_product(arr)
        naive_time = time.time() - start_time

        start_time = time.time()
        fast_result = max_pairwise_product_fast(arr)
        fast_time = time.time() - start_time

        # print(f"Array: {arr}")
        # print(f"Naive result: {naive_result}, Time: {naive_time}")
        # print(f"Fast result: {fast_result}, Time: {fast_time}")

        if naive_result != fast_result:
            print("Wrong answer")
            return
        print("OK")
        print()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "stress_test":
        if len(sys.argv) == 5:
            num_tests = int(sys.argv[2])
            max_n = int(sys.argv[3])
            max_m = int(sys.argv[4])
        else:
            num_tests = 100
            max_n = 1000
            max_m = 100000

        print(f"Running stress tests with {num_tests} tests, max_n = {max_n}, max_m = {max_m}")
        stress_test(num_tests, max_n, max_m)
    else:
        try:
            n = int(input())
            arr = list(map(int, input().split()))
            assert n == len(arr), f"Expected {n} numbers, got {len(arr)}"
            result = max_pairwise_product_fast(arr)
            print(result)
        except ValueError:
            print("Invalid input. Wrong input format")
        except AssertionError as e:
            print(f"Input error: {e}")        