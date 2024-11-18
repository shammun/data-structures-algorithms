def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

"""
def fibonacci_huge_efficient(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current
"""

def fibonacci_huge_pisano(n, m):
    if n <= 1:
        return n
    
    # Compute the Pisano period
    pisano_period = get_pisano_period(m)
    
    if pisano_period != 1:
        n = n % pisano_period
    
    previous = 0
    current = 1
    for _ in range(n-1):
        previous, current = current, (previous + current) % m
    
    return current

"""
The Pisano period for m=2 is 3 * 2^(k-2), where k is the smallest integer such 
that 2^k is greater than n
"""

def get_pisano_period(m):
    if m == 2:
        k = 2
        while 2 ** k <= n:
            k += 1
        return 3 * 2 ** (k - 2)
    
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1
    return 1



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_pisano(n, m))