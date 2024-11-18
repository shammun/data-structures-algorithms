
def optimal_summands(n):
    summands = []
    i = 1
    sum_summands = 0

    while sum_summands <= n:
        if (sum_summands + i) <= n:
            summands.append(i)
            sum_summands += i
        else:
            summands[-1] += n - sum_summands
            break
        i += 1

    return summands

if __name__ == "__main__":
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)