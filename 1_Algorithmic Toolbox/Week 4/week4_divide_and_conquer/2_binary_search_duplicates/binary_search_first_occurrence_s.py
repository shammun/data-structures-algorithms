
def binary_search_with_duplicates(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def main():
    n = int(input())
    sorted_array = list(map(int, input().split()))

    m = int(input())
    queries = list(map(int, input().split()))

    results = []
    for query in queries:
        results.append(binary_search_with_duplicates(sorted_array, query))

    print(*results)

if __name__ == '__main__':
    main()