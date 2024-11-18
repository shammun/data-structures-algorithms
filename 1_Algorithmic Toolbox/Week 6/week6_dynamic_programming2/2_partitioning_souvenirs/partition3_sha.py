def partition3(nums):
    total_sum = sum(nums)

    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3
    n = len(nums)

    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n+1):
        for j in range(target + 1):
            for k in range(target + 1):
                current = nums[i-1]
                dp[i][j][k] = dp[i-1][j][k]
                if j >= current:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j-current][k]
                if k >= current:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j][k-current]

    return 1 if dp[n][target][target] else 0

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    print(partition3(values))