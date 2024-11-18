def lcs3(A, B, C):
    n = len(A)
    m = len(B)
    o = len(C)

    lcs = [[[0] * (o + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            for k in range(o + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
                else:
                    lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1])

    return lcs[n][m][o]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
