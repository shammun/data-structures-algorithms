def primitive_calculator(n):
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(1, n):
        if i + 1 <= n:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        if i * 2 <= n:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= n:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    
    # Find the sequence by backtracking
    sequence = []
    current = n
    while current > 0:
        sequence.append(current)
        if current % 3 == 0 and dp[current] == dp[current // 3] + 1:
            current //= 3
        elif current % 2 == 0 and dp[current] == dp[current // 2] + 1:
            current //= 2
        else:
            current -= 1
    sequence.reverse()
    return dp[n], sequence

if __name__ == '__main__':
    n = int(input())
    num_operations, sequence = primitive_calculator(n)
    print(num_operations)
    print(" ".join(map(str, sequence)))
