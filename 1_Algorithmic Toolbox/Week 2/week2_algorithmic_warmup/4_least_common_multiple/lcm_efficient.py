
def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return 1

    assert False

# Let a and b be positive integers. Then gcd(a, b) = gcd(b, a mod b).
def gcd_euclid(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a%b)

def lcm(a, b):
    if a > b:
        return (a * b) // gcd_euclid(a, b)
    else:
        return (a * b) // gcd_euclid(b, a)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

