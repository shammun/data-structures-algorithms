def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

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

# Sum Of (Fib[0]^2+Fib[1]^2+.....+Fib[n]^2) = Fib[n]*Fib[n+1]
def fib_huge(n):
    n_plus_1 = fib(n + 1, 10)
    n = fib(n, 10)

    return (n * n_plus_1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fib_huge(n))
