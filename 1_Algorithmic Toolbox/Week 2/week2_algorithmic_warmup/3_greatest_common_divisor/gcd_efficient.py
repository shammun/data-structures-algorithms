def gcd_naive1(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_naive2(a, b):
    best = 1
    for d in range(2, a + b):
        if a % d == 0 and b % d == 0:
            best = d
    return best

# Lemma
# Let a and b be positive integers. Then gcd(a, b) = gcd(b, a mod b).
def gcd_euclid(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a%b)


def gcd_stress():
    """
    Stress tests the fibonacci_number_efficient function.

    Args:
    """
    from random import randint
    import time

    a = randint(21, 100)
    b = randint(121, 200) 
    start1 = time.time()
    naive = gcd_naive2(a, b)
    end1 = time.time()
    time1 = end1 - start1

    start2 = time.time()
    efficient = gcd_euclid(a, b)
    end2 = time.time()
    time2 = end2 - start2

    print(f'GCD of {a} and {b}\n With naive method, the GCD is -- {naive} and time taken is {time1}\n With Euclid method, the value is {efficient} and time taken is {time2}')
    if naive == efficient:
        print('OK')
    else:
        print(f'Wrong answer: {naive}, {efficient}')


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_euclid(a, b))
