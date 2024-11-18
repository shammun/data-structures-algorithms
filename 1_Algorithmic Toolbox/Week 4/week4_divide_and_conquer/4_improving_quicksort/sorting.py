from random import randint


def partition3(array, left, right):
    # write your code here
    pivot = array[left]
    i = left
    m1 = left
    m2 = right

    while i <= m2:
        if array[i] < pivot:
            array[i], array[m1] = array[m1], array[i]
            m1 += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[m2] = array[m2], array[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
