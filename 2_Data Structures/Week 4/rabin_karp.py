import random

def poly_hash(s, p, x):
    hash_value = 0
    for char in reversed(s):
        hash_value = (hash_value * x + ord(char)) % p
    return hash_value

def are_equal(s1, s2):
    return s1 == s2

def rabin_karp(T, P):
    p = 1000000007
    x = random.randint(1, p-1)
    positions = []

    p_hash = poly_hash(P, p, x)

    for i in range(len(T) - len(P) + 1):
        t_hash = poly_hash(T[i:i+len(P)], p, x)
        if p_hash != t_hash:
            continue
        if are_equal(T[i:i+len(P)], P):
            positions.append(i)

    return positions

def main():
    text = input()
    pattern = input()
    result = rabin_karp(text, pattern)
    print(f"Pattern found at positions: {result}")

if __name__ == "__main__":
    main()