def fibonacci_number_naive(n):
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)

# Efficient implementation of the Fibonacci number algorithm.
def fibonacci_number_efficient(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current

# Dynamic programming implementation of the Fibonacci number algorithm.
def fibonacci_number_dynamic(n):
    if n <= 1:
        return n
    fibonacci_numbers = [0, 1]
    for _ in range(n - 1):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[-1]


# Generator implementation of the Fibonacci number algorithm.
def fibonacci_generator():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fibn_1 + fibn_2
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

# Memoization implementation of the Fibonacci number algorithm.
memo = {0: 0, 1: 1}
def fibonacci_number_memoization(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_number_memoization(n - 1) + fibonacci_number_memoization(n - 2)
        return memo[n]

# Stress tests the fibonacci_number_efficient function.
from random import randint
import time

def fibonacci_number_stress(m):
    """
    Stress tests the fibonacci_number_efficient function.

    Args:
        m (int): The highest number below which to generate Fibonacci number
    """
    
    n = randint(20, m) 
    start1 = time.time()
    fast = fibonacci_number_efficient(n)
    end1 = time.time()
    time1 = end1 - start1
    
    start2 = time.time()
    slow = fibonacci_number_naive(n)
    end2 = time.time()
    time2 = end2 - start2
    
    print(f'Generating Fibonacci number for {n}\n With fast method, the value is -- {fast} and time taken is {time1}\n With naive method, the value is {slow} and time taken is {time2}')
    if fast == slow:
        print('OK')
    else:
        print(f'Wrong answer: {fast}, {slow}')

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_efficient(input_n))