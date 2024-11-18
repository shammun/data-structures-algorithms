def process_queries(s, queries):
    s = list(s)
    for i, j, k in queries:
        substring = s[i:j+1]
        del s[i:j+1]
        if k == 0:
            s = substring + s
        else:
            s = s[:k] + substring + s[k:]
    return "".join(s)

def main():
    s = input().strip()
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    result = process_queries(s, queries)
    print(result)

if __name__ == "__main__":
    main()