def change_DP(money):
    coins = [1, 3, 5]
    minCoins = [float('inf')] * (money + 1)
    minCoins[0] = 0

    for m in range(1, money+1):
        for coin in coins:
            if m >= coin:
                numCoins = minCoins[m-coin] + 1
                if numCoins < minCoins[m]:
                    minCoins[m] = numCoins
    return minCoins[money]

if __name__ == "__main__":
    money = int(input())
    print(change_DP(money))