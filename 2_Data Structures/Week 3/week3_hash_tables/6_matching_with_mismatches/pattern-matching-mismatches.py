import random

class PatternMatchingWithMismatches:
    def __init__(self):
        self.P = random.randint(26, 100)
        self.M = 1000000007

    def compute_hashes(self, s, length):
        h = [0] * (len(s) - length + 1)
        s = [ord(c) - ord('a') + 1 for c in s]
        p_pow = pow(self.P, length, self.M)

        for i in range(len(s) - length, -1, -1):
            if i == len(s) - length:
                for j in range(length):
                    h[i] = (h[i] * self.P + s[i + j]) % self.M
            else:
                h[i] = (h[i+1] * self.P - s[i+length]*p_pow + s[i]) % self.M
        
        return h

    def are_equal(self, h1, h2, i, j):
        return h1[i] == h2[j]

    def find_mismatch(self, h1, h2, l, r):
        while l < r:
            m = (l + r) // 2
            if self.are_equal(h1, h2, l, 0):
                l = m + 1
            else:
                r = m
        return l

    def find_occurrences(self, k, text, pattern):
        n, m = len(text), len(pattern)
        text_hash = self.compute_hashes(text, m)
        pattern_hash = self.compute_hashes(pattern, m)
        occurrences = []

        for i in range(n - m + 1):
            mismatches = 0
            pos = 0
            while pos < m and mismatches <= k:
                if not self.are_equal(text_hash, pattern_hash, i, 0):
                    mismatches += 1
                    if mismatches > k:
                        break
                    pos = self.find_mismatch(text_hash, pattern_hash, pos, m)
                else:
                    pos += 1
            if mismatches <= k:
                occurrences.append(i + 1)  # +1 because positions are 1-indexed

        return occurrences

    def process_input(self):
        k, text, pattern = input().split()
        k = int(k)
        occurrences = self.find_occurrences(k, text, pattern)
        print(len(occurrences), *occurrences)

# Main execution
if __name__ == "__main__":
    solver = PatternMatchingWithMismatches()
    solver.process_input()
