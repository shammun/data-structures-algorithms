from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def mergeSortAndCount(arr, s, e):
    if e - s + 1 <= 1:
        return 0
    
    m = (s + e) // 2

    # Sort and count inversions in left half
    left_inversions = mergeSortAndCount(arr, s, m)

    # Sort and count inversions in right half
    right_inversions = mergeSortAndCount(arr, m+1, e)

    # Merge and count inversions
    inversions = mergeAndCount(arr, s, m, e)

    return left_inversions + right_inversions + inversions

def mergeAndCount(arr, s, m, e):
    left = arr[s:m+1]
    right = arr[m+1:e+1]
    left_index = 0
    right_index = 0
    inversions = 0
    k = s

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr[k] = left[left_index]
            left_index += 1
        else:
            arr[k] = right[right_index]
            right_index += 1
            inversions += len(left) - left_index
        k += 1
    
    while left_index < len(left):
        arr[k] = left[left_index]
        left_index += 1
        k += 1

    while right_index < len(right):
        arr[k] = right[right_index]
        right_index += 1
        k += 1
        
    return inversions

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # print(inversions_naive(elements))
    print(mergeSortAndCount(elements, 0, len(elements)-1))
