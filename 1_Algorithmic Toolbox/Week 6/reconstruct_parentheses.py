import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def MinAndMax(i, j, operators, m, M, brackets):
    min_val = math.inf
    max_val = -math.inf
    min_k = max_k = None
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        if min_val > min(a, b, c, d):
            min_val = min(a, b, c, d)
            min_k = k
        if max_val < max(a, b, c, d):
            max_val = max(a, b, c, d)
            max_k = k
    brackets[i][j] = (min_k, max_k)
    return min_val, max_val

def parentheses_min_max(expression):
    digits = list(map(int, expression[0::2]))
    operators = list(expression[1::2])
    n = len(digits)
    
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    brackets = [[None] * n for _ in range(n)]
    
    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, operators, m, M, brackets)
    
    return M[0][n-1], brackets, digits

def construct_solution_for_max(i, j, brackets, operators, digits):
    if i == j:
        return str(digits[i])
    k = brackets[i][j][1]
    left_expr = construct_solution_for_max(i, k, brackets, operators, digits)
    right_expr = construct_solution_for_max(k+1, j, brackets, operators, digits)
    return f"({left_expr} {operators[k]} {right_expr})"

if __name__ == '__main__':
    expression = "5-8+7*4-8+9"  # Example expression
    max_value, brackets, digits = parentheses_min_max(expression)
    max_expr = construct_solution_for_max(0, len(digits) - 1, brackets, list(expression[1::2]), digits)
    
    # print("The value of the brackets:", brackets)
    print("Maximum value of the expression:", max_value)
    print("Expression with maximum value:", max_expr)
