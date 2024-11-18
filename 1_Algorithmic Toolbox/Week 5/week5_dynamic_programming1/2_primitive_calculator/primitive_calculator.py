def compute_operations(n):
    operations = ["plus", "multiply_by_two", "multiply_by_three"]
    
    num_operations = [0, 0] + [float('inf')] * (n-1)
    
    for i in range(2, n + 1):
        operations1, operations2, operations3 = float('inf'), float('inf'), float('inf')
        if i % 3 == 0:
            operations3 = num_operations[i // 3] + 1
        if i % 2 == 0:
            operations2 = num_operations[i // 2] + 1

        operations1 = num_operations[i - 1] + 1
        num_operations[i] = min(operations1, operations2, operations3)
    
    # print(num_operations)

    nums = [n]

    while n != 1:
        if n % 3 == 0 and num_operations[n] == num_operations[n // 3] + 1:
            nums.append(n // 3)
            n = n // 3
        elif n % 2 == 0 and num_operations[n] == num_operations[n // 2] + 1:
            nums.append(n // 2)
            n = n // 2
        else:
            nums.append(n - 1)
            n = n - 1
    
    return nums[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
