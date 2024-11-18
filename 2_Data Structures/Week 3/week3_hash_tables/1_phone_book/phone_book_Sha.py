def add_contact(phone_book, number, name):
    phone_book[number] = name

def del_contact(phone_book, number):
    if number in phone_book:
        del phone_book[number]

def find_contact(phone_book, number):
    return phone_book.get(number, "not found")

def process_query(phone_book, query, results):
    operation = query[0]

    if operation == 'add':
        add_contact(phone_book, query[1], query[2])
    elif operation == 'del':
        del_contact(phone_book, query[1])
    elif operation == 'find':
        results.append(find_contact(phone_book, query[1]))

def main():
    phone_book = {}
    results = []

    n = int(input())

    for _ in range(n):
        query = input().split()
        process_query(phone_book, query, results)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()