# 1) https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

# 2) https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python
def expression_matter(a, b, c):
    sum1 = a + b + c
    sum2 = a * b * c
    sum3 = a + (b * c)
    sum4 = (a + b) * c
    sum5 = a * (b + c)
    sum6 = (a * b) + c
    
    return max(sum1,sum2,sum3,sum4,sum5,sum6)

# 3) https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    
    res = int(a) + int(b)
    
    return str(res)

# 4) https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python


# 5) https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python
def reverse_list(l):
    return l[::-1]