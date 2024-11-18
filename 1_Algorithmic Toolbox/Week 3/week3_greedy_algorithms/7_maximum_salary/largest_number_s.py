from sys import stdin

def largest_number_naive(numbers):
    salary = ""
    while len(numbers) != 0:
        max_number = -999999
        for number in numbers:
            if number >= max_number:
                max_number = number
        salary = salary+str(max_number)
        max_index = numbers.index(max_number)
        del numbers[max_index]
    return int(salary)

def is_better(number, max_number):
    if max_number < 0:
        return True
    else:
        return int(str(number) + str(max_number)) > int(str(max_number) + str(number))

def largest_number_efficient(numbers):
    salary = ""
    while len(numbers) != 0:
        max_number = -999999
        for number in numbers:
            if is_better(number, max_number):
                max_number = number
        salary = salary+str(max_number)
        max_index = numbers.index(max_number)
        del numbers[max_index]
    return int(salary)

if __name__ == "__main__":
    input = stdin.read()
    _, *input_numbers = map(int, input.split())
    #print(largest_number_naive(input_numbers))
    print(largest_number_efficient(input_numbers))
