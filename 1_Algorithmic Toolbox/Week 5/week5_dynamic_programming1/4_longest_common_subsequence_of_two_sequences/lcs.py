def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    
    # Initialize the DP table
    lcs = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs[n][m]

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    print(longest_common_subsequence(A, B))