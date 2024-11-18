def majority_element(arr):
    # Base case: if the array has only one element, it is the majority element
    if len(arr) == 1:
        return arr[0]

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively find the majority element in each half
    left_majority = majority_element(left_half)
    right_majority = majority_element(right_half)

    # If the left and right halves have the same majority element, it is the overall majority element
    if left_majority == right_majority:
        return left_majority

    # Otherwise, count the occurrences of each candidate majority element
    left_count = sum(1 for elem in left_half if elem == left_majority)
    right_count = sum(1 for elem in right_half if elem == right_majority)

    # Return the overall majority element, if it exists
    if left_count > len(arr) // 2:
        return left_majority
    elif right_count > len(arr) // 2:
        return right_majority
    else:
        return None

if __name__ == '__main__':
    input_elements = list(map(int, input().split()))
    print(majority_element(input_elements))