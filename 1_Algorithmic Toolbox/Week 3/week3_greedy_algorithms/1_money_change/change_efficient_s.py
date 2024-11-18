def change(money):
    sum = 0
    sum += money // 10
    sum += money % 10 // 5
    sum += money % 5
    return sum

if __name__ == "__main__":
    money = int(input())
    print(change(money))