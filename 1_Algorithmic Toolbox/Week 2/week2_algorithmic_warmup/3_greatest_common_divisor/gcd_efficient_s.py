import random
import sys
import time

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd

def gcd_efficient(a, b):
    if b == 0:
        return a
    else:
        return gcd_efficient(b, a%b)
    
def stress_test(num_tests, max_a, max_b):
    """
    Performs stress testing on the gcd_efficient function.
    Args:
        num_tests (int): Number of tests to run.
        max_a (int): Maximum number to be considered for a
        max_b (int): Maximum number to be considered for b
    """
    for i in range(num_tests):
        print(f"Running test {i+1} of {num_tests}")
        b = random.randint(1, max_b)
        a = random.randint(b + 1, max_a)
        while(b > a):
            a = random.randint(2, max_a)
            b = random.randint(1, max_b)

        start_time = time.time()
        naive_result = gcd_naive(a, b)
        naive_time = time.time() - start_time

        start_time = time.time()
        fast_result = gcd_efficient(a, b)
        fast_time = time.time() - start_time

        if naive_result != fast_result:
            print(f"Wrong answer for {a} and {b}")
            print(f"Naive result is: {naive_result}")
            print(f"Fast result is: {fast_result}")
            return
        print("OK")
        print()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "stress_test":
        if len(sys.argv) == 4:
            num_tests = 1
            max_a = int(sys.argv[2])
            max_b = int(sys.argv[3])
        else:
            num_tests = 10
            max_a = 3000
            max_b = 200

        print(f"Running stress tests with {num_tests} tests, max_a = {max_a}, max_b = {max_b}")
        stress_test(num_tests, max_a, max_b)
    else:
        try:
            a, b = map(int, input().split())
            result = gcd_efficient(a, b)
            print(result)
        except ValueError:
            print("Invalid input. Wrong input format")
        except AssertionError as e:
            print(f"Input error: {e}")  