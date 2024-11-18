def edit_distance(A, B):
    n = len(A)
    m = len(B)
    
    # Initialize the DP table
    distance = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(n + 1):
        distance[i][0] = i
    for j in range(m + 1):
        distance[0][j] = j
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = distance[i][j - 1] + 1
            deletion = distance[i - 1][j] + 1
            if A[i - 1] == B[j - 1]:
                match = distance[i - 1][j - 1]
                distance[i][j] = min(insertion, deletion, match)
            else:
                mismatch = distance[i - 1][j - 1] + 1
                distance[i][j] = min(insertion, deletion, mismatch)
    
    return distance[n][m]

if __name__ == '__main__':
    A = input()
    B = input()
    print(edit_distance(A, B))


    