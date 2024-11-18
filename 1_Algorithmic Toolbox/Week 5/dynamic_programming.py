def DPChange(money, coins):
    MinNumCoins = [float('inf')] * (money + 1)
    MinNumCoins[0] = 0

    # Loop over each amount from 1 to money
    for m in range(1, money+1):
        # Loop over each coin
        for coin in coins:
            if m >= coin:
                NumCoins = MinNumCoins[m-coin] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(input())
    coins = list(map(int, input().split()))
    print(DPChange(m, coins))