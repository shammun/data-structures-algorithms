# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            # Check if it is empty
            if not opening_brackets_stack:
                return i + 1
            last, position = opening_brackets_stack.pop()
            
            if not are_matching(last, next):
                return i + 1
    
    # Check is there are additional opening brackets that were not matched
    # If it is not empty then return the first one's position
    if opening_brackets_stack:
        return opening_brackets_stack[0][1]
    
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
