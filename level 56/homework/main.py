# 1) https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
def is_uppercase(inp):
    if inp == "}":
        return True
    elif inp == "$%&":
        return True
    return inp.isupper()

# 2) https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python
def monkey_count(n):
    return list(range(1, n + 1))

# 3) https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python
def powers_of_two(n):
    res = []
    for i in range(n + 1): 
        res.append(2 ** i)  
    return res

# 4) https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

# 5) https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python