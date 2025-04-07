#1)https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

#2)https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    return [i for i in l if type(i) is int]

#3)https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
def descending_order(num):
    num = str(num)
    return int("".join(sorted(num,reverse = True)))

#4)https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
def is_square(n):    
    if n < 0:
        return False
    return n ** 0.5 %1 ==0.0

#5)https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
def get_middle(s):
    if len(s) % 2 == 0:
        s1 = s[len(s) // 2 - 1]
        s2 = s[len(s) // 2]
        return s1 + s2
    else:
        s3 = s[len(s) // 2]
        return s3