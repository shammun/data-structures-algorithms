import random

def randomized_quicksort1(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_index = random.randint(0, len(arr)-1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort1(left) + middle + randomized_quicksort1(right)

def randomized_quicksort2(arr, s=0, e=None):
    if e is None:
        e = len(arr) - 1
        
    if e - s + 1 <= 1:
        return arr
    
    pivot_index = random.randint(s, e)
    arr[pivot_index], arr[e] = arr[e], arr[pivot_index]
    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1
    tmp = arr[e]
    arr[e] = arr[left]
    arr[left] = tmp
    # arr[e], arr[left] = arr[left], arr[e]
    randomized_quicksort2(arr, s, left-1)
    randomized_quicksort2(arr, left+1, e)
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    assert n == len(arr)
    #print("The array before sorting is:")
    #print(*arr)
    sorted_arr = randomized_quicksort2(arr)
    #print("The array after sorting is:")
    print(*sorted_arr)

if __name__ == "__main__":
    main()