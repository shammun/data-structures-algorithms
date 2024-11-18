def edit_distance_with_backtrack(A, B):
    n = len(A)
    m = len(B)

    # Initialize the DP table
    D = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[''] * (m + 1) for _ in range(n + 1)]

    # Initialize base cases
    for i in range(n + 1):
        D[i][0] = i
        backtrack[i][0] = "up"
    for j in range(m + 1):
        D[0][j] = j
        backtrack[0][j] = "left"

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            if A[i-1] == B[j-1]:
                match = D[i-1][j-1]
                D[i][j] = min(insertion, deletion, match)
                if D[i][j] == match:
                    backtrack[i][j] = "diagonal"
                elif D[i][j] == deletion:
                    backtrack[i][j] = "up"
                else:
                    backtrack[i][j] = "left"
            else:
                mismatch = D[i-1][j-1] + 1
                D[i][j] = min(insertion, deletion, mismatch)
                if D[i][j] == mismatch:
                    backtrack[i][j] = "diagonal"
                elif D[i][j] == deletion:
                    backtrack[i][j] = "up"
                else:
                    backtrack[i][j] = "left"

    return backtrack

def outputAlignment(A, B, i, j, backtrack):
    if i == 0 and j == 0:
        return "", ""
    if i > 0 and backtrack[i][j] == "up":
        aligned_A, aligned_B = outputAlignment(A, B, i-1, j, backtrack)
        aligned_A += A[i-1]
        aligned_B += "-"
    elif j > 0 and backtrack[i][j] == "left":
        aligned_A, aligned_B = outputAlignment(A, B, i, j-1, backtrack)
        aligned_A += "-"
        aligned_B += B[j-1]
    else:
        aligned_A, aligned_B = outputAlignment(A, B, i-1, j-1, backtrack)
        aligned_A += A[i-1]
        aligned_B += B[j-1]
    return aligned_A, aligned_B

if __name__ == '__main__':
    A = input("Enter first string: ")
    B = input("Enter second string: ")
    backtrack = edit_distance_with_backtrack(A, B)
    aligned_A, aligned_B = outputAlignment(A, B, len(A), len(B), backtrack)
    
    for a, b in zip(aligned_A, aligned_B):
        print(f"{a} {b}")
