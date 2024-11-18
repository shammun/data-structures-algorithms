import random
import sys
import time

def fibonacci_number_naive(n):
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)

# Efficient implementation of the Fibonacci number algorithm.
def fibonacci_number_efficient(n):
    if n <= 1:
        return n
    F = [0] * (n + 1)
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

def stress_test(num_tests):
    """
    Performs stress testing on the fibonacci_number_efficient functions.
    Args:
        num_tests (int): Number of tests to run.
        max_n (int): Maximum number of elements in the test array.
    """
    for i in range(num_tests):
        print(f"Running stress test {i + 1} of {num_tests}")
        n = random.randint(2, 9)

        start_time = time.time()
        naive_result = fibonacci_number_naive(n)
        naive_time = time.time() - start_time

        start_time = time.time()
        fast_result = fibonacci_number_efficient(n)
        fast_time = time.time() - start_time

        if naive_result != fast_result:
            print("Wrong answer")
            return
        print("OK")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "stress_test":
        if len(sys.argv) == 3:
            num_tests = int(sys.argv[2])
            stress_test(num_tests)
        elif len(sys.argv) == 2:
            stress_test(10)
    else:
        try:
            num_tests = int(input())
            print(fibonacci_number_efficient(num_tests))
        except ValueError:
            print("Invalid input. Wrong input format")
        except AssertionError as e:
            print(f"Input error: {e}")


