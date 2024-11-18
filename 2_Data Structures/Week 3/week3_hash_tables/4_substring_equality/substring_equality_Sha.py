import random

class SubstringEquality:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = random.randint(1, 10**9)

        self.h1 = self._precompute_hashes(self.m1)
        self.h2 = self._precompute_hashes(self.m2)

        self.pow1 = self._precompute_powers(self.m1)
        self.pow2 = self._precompute_powers(self.m2)

    def _precompute_hashes(self, m):
        h = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            h[i] = (self.x * h[i - 1] + ord(self.s[i-1])) % m
        return h
    
    def _precompute_powers(self, m):
        pow_m = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            pow_m[i] = (pow_m[i-1] * self.x) % m
        return pow_m
    
    def are_equal(self, a, b, l):
        h1_a = (self.h1[a+l] - self.pow1[l] * self.h1[a]) % self.m1
        h1_b = (self.h1[b+l] - self.pow1[l] * self.h1[b]) % self.m1

        if h1_a < 0:
            h1_a += self.m1
        
        if h1_b < 0:
            h1_b += self.m1

        if h1_a != h1_b:
            return False
        
        h2_a = (self.h2[a+l] - self.pow2[l] * self.h2[a]) % self.m2
        h2_b = (self.h2[b+l] - self.pow2[l] * self.h2[b]) % self.m2

        if h2_a < 0:
            h2_a += self.m2
        
        if h2_b < 0:
            h2_b += self.m2

        return h2_a == h2_b
    

def main():
    s = input().strip()
    checker = SubstringEquality(s)

    q = int(input().strip())
    results = []

    for _ in range(q):
        a, b, l = map(int, input().strip().split())

        results.append("Yes" if checker.are_equal(a, b, l) else "No")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()