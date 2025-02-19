# 1) https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python
def in_asc_order(arr):
    return arr == sorted(arr)

# 2) https://www.codewars.com/kata/5663f5305102699bad000056/train/python
def mxdiflg(a1, a2):
    listn = []
    try:
        for x in a1:
            for y in a2:
                listn.append(abs(len(x) - len(y)))
        return max(listn)
    except:
        return -1 
    
# 3) https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python
def fizzbuzz(n):
    res = []
    
    for i in range(1,n + 1):
        if i % 3 == 0 and i % 5 ==0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(i)
        
    return res

# 4) https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
def factorial(n):
    if n == 0:
        return 1
    
    res = n
    
    for i in range(1,n):
        res *= i
        
    return res

# 5) https://www.codewars.com/kata/5300901726d12b80e8000498/train/pythondef fizzbuzz(n):
def fizzbuzz(n):
    res = []
    
    for i in range(1,n + 1):
        if i % 3 == 0 and i % 5 ==0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(i)
        
    return res

# 6) https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python

# 7) https://www.codewars.com/kata/535474308bb336c9980006f2/train/python

# 8) https://www.codewars.com/kata/580a4734d6df748060000045/train/python
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"
    
# 9) https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python

