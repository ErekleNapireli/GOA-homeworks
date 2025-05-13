#1) https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    elif l != w:
        return l * 2 + w * 2

#2) https://www.codewars.com/kata/5a023c426975981341000014/train/python
def other_angle(a, b):
    return 180 - (a + b)

#3) https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python/
def set_alarm(employed, vacation):
    if  employed == True and vacation == True:
        return False
    elif employed == True and vacation == False:
        return True
    elif employed == False and vacation == True:
        return False
    elif employed == False and vacation == False:
        return False

#4) https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python

def sum_mix(arr):
    num = 0
    for i in arr:
        num += int(i)
        
    return num

#5)https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
