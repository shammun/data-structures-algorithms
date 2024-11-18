import sys
from collections import defaultdict

P = 31
M = 10**9 + 7

def compute_hashes(s, length):
    h = [0] * (len(s) - length + 1)
    s = [ord(c) - ord('a') + 1 for c in s]
    p_pow = pow(P, length, M)

    for i in range(len(s) - length, -1, -1):
        if i == len(s) - length:
            for j in range(length):
                h[i] = (h[i] * P + s[i + j]) % M
        else:
            h[i] = (h[i+1] * P - s[i+length]*p_pow + s[i]) % M
    
    return h

def check_equal_substrings(s, t, length):
    hs = compute_hashes(s, length)
    ht = compute_hashes(t, length)

    common = defaultdict(list)

    for i, h in enumerate(hs):
        common[h].append(i)
    
    for i, h in enumerate(ht):
        if h in common:
            for j in common[h]:
                if s[j:j+length] == t[i:i+length]:
                    return j, i
                
    return -1, -1

def solve(s, t):
    lo, hi = 0, min(len(s), len(t))
    pos_s, pos_t = 0, 0

    while lo <= hi:
        mid = (lo + hi) // 2
        i, j = check_equal_substrings(s, t, mid)
        if i >= 0:
            lo = mid + 1
            pos_s, pos_t = i, j
        else:
            low = mid - 1
    
    return pos_s, pos_t

if __name__ == "__main__":
    print("Enter your test cases, one per line.")
    print("Type 'END' on a new line when you're finished entering test cases.")
    
    # Read input lines until 'END' is encountered
    input_lines = []
    while True:
        line = input().strip()
        if line == 'END':
            break
        input_lines.append(line)
    
    # Process each pair of strings
    results = []
    for line in input_lines:
        s, t = line.split()
        results.append(solve(s, t))
    
    # Print all results
    for i, j, l in results:
        print(i, j, l)