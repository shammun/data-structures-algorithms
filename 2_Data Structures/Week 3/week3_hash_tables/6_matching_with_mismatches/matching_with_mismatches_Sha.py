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
                h[i] = (h[i + 1] * self.P - s[i + length]*p_pow + s[i]) % self.M
        
        return h

    def are_equal(self, h1, h2, i, j):
        return h1[i] == h2[j]
    
    def count_mismatches(self, text, pattern, start):
        mismatches = 0
        for i in range(len(pattern)):
            if text[start + i] != pattern[i]:
                mismatches += 1
            if mismatches > self.k:
                break
        return mismatches
    
    def find_occurrences(self, k, text, pattern):
        self.k = k
        n, m = len(text), len(pattern)
        text_hash = self.compute_hashes(text, m)
        pattern_hash = self.compute_hashes(pattern, m)
        occurrences = []

        for i in range(n - m + 1):
            if self.are_equal(text_hash, pattern_hash, i, 0):
                occurrences.append(i)
            else:
                mismatches = self.count_mismatches(text, pattern, i)
                if mismatches <= k:
                    occurrences.append(i)

        return occurrences
    
    def process_multiple_inputs(self):
        results = []
        print("Input")
        for _ in range(5):
            k, text, pattern = input().split()
            k = int(k)
            occurrences = self.find_occurrences(k, text, pattern)
            results.append([len(occurrences)] + occurrences)
        return results
    
    def format_output(self, results):
        print("\nOutput: ")
        for result in results:
            print(*result)

if __name__ == "__main__":
    solver = PatternMatchingWithMismatches()
    results = solver.process_multiple_inputs()
    solver.format_output(results)