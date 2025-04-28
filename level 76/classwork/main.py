# https://www.codewars.com/kata/526233aefd4764272800036f
def matrix_addition(a, b):
    res = []
    
    for i in range(len(a)):
        row = []
        for x in range(len(a[i])):
            row.append(a[i][x] + b[i][x])
        res.append(row)
    return res

# https://www.codewars.com/kata/5503013e34137eeeaa001648
def diamond(n):
    if n % 2 == 0 or n < 0: return None

    result = []
    
    for i in range(1, n, 2):
        result.append(" " * ((n-i) // 2) + "*" * i + "\n")
    return "".join(result) + "*" * n + "\n" +  "".join(result[::-1])