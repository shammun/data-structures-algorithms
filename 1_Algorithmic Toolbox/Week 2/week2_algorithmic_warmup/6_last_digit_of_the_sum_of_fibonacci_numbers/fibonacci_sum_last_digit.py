def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

"""
def fibonacci_sum_efficient(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10
        _sum += current

    return _sum % 10
"""

def period(m):
    a, b, c = 0, 1, 1
    for i in range(m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1

def fib(n, m):
    rem = n % period(m)
    a, b = 0, 1
    res = rem
    for i in range(1, rem):
        res = (a + b) % m
        a, b = b, res
    return res % m

# Sum Of (Fib[0]+Fib[1]+.....+Fib[n]) = Fib[n+2]-Fib[2]
def fib_huge(n):
    n_plus_2 = fib(n + 2, 10)
    n_2 = fib(2, 10)

    if n_plus_2 >= n_2:
        return n_plus_2 - n_2
    else:
        return 10 + n_plus_2 - n_2


if __name__ == '__main__':
    n = int(input())
    print(fib_huge(n))
