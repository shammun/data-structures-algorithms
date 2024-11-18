

# too slow
def fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


"""
# Too slow
memo = {0: 0, 1: 1}
def fibonacci_last_digit(n):
    if n in memo:
        return memo[n] % 10
    else:
        memo[n] = fibonacci_last_digit(n - 1) + fibonacci_last_digit(n - 2)
        return memo[n]
"""

def fibonacci_last_digit_efficient(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit_efficient(n))



# efficient implementation of the Fibonacci number algorithm.
# def fibonacci_number_efficient(n):
