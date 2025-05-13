# 1) https://www.codewars.com/kata/52ceafd1f235ce81aa00073a/train/python
def plural(n):
    if n == 1:
        return False
    else:
        return True
    
# 2) https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python
def problem(a):
    if a == str(a):
        return "Error"
    else:
        return a * 50 + 6
    
# 3) https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python
def multi_table(number):
    res = ""
    
    for i in range(1,11):
        res +=f"{i} * {number} = {i * number}\n"
        
    return res[:-1]

# 4) https://www.codewars.com/kata/595970246c9b8fa0a8000086/train/python
def capitalize_word (word : str) -> str:
    return word.capitalize()

# 5) https://www.codewars.com/kata/56200d610758762fb0000002/train/python
def add_five(num):
    total = num + 5
    return total
