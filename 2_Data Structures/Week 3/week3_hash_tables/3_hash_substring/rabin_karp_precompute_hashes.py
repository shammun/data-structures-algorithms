import random

def poly_hash(s, p, x):
    hash_value = 0
    for char in reversed(s):
        hash_value = (hash_value * x + ord(char)) % p
    return hash_value

def precompute_hashes(T, pattern_length, p, x):
    T_length = len(T)
    H = [0] * (T_length - pattern_length + 1)
    S = T[T_length - pattern_length:T_length]
    H[T_length - pattern_length] = poly_hash(S, p, x)
    
    y = 1
    for i in range(pattern_length):
        y = (y * x) % p
    
    for i in range(T_length - pattern_length - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + pattern_length])) % p
        if H[i] < 0:
            H[i] += p
    
    return H

def are_equal(s1, s2):
    return s1 == s2

def rabin_karp(T, P):
    p = 1000000007
    x = random.randint(1, p - 1)
    positions = []

    p_hash = poly_hash(P, p, x)
    H = precompute_hashes(T, len(P), p, x)

    for i in range(len(T) - len(P) + 1):
        if p_hash != H[i]:
            continue
        if are_equal(T[i:i + len(P)], P):
            positions.append(i)

    return positions

def main():
    T = input()
    P = input()
    result = rabin_karp(T, P)
    print(result)

if __name__ == "__main__":
    main()
