def majority_element(n, array):
    count = {}
    half = n // 2

    for i in array:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > half:
            return 1
    return 0

def main():
    n = int(input())
    array = list(map(int, input().split()))
    result = majority_element(n, array)
    print(result)   

if __name__ == '__main__':
    main()

