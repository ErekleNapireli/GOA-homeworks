# 1) https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python
def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))
# 2) https://www.codewars.com/kata/50ee6b0bdeab583673000025/train/python
a = "code"
b = "wa.rs"
name = a + b
# 3) https://www.codewars.com/kata/55c28f7304e3eaebef0000da/train/python
def xor(a,b):
    return a != b
# 4) https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c/train/python

# 5) https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python
def get_real_floor(n):
    if n <=0:
        return n
    elif n < 13:
        return n -1
    else:
        return n - 2

# 6) https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python

# 7) https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

# 8) https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python

# 9) https://www.codewars.com/kata/56b29582461215098d00000f/train/python

# 10) https://www.codewars.com/kata/57202aefe8d6c514300001fd/train/python
def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    elif n >= 10:
        return n * 90
