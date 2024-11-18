import math

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        assert b != 0, 'Division by zero'
        return a // b
    
def min_and_max(i, j, operators, m, M):
    min_val = math.inf
    max_val = -math.inf

    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], operators[k])
        b = evaluate(M[i][k], m[k+1][j], operators[k])
        c = evaluate(m[i][k], M[k+1][j], operators[k])
        d = evaluate(M[i][k], M[k+1][j], operators[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def parentheses_min_max(expression):
    digits = list(map(int, expression[0::2]))
    operators = expression[1::2]
    n = len(digits)

    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]

    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, operators, m, M)

    return M[0][n-1]

if __name__ == '__main__':
    expression = input()
    max_value = parentheses_min_max(expression)
    print(max_value)