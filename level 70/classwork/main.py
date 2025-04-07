#1) https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python 

def largest_pair_sum(numbers):
    max1 = numbers[0]
    max2 = 0
    
    for i in numbers[1:]:
        if i > max1:
            max1,max2 = i,max1
        elif i > max2:
            max2 = i
    return max1 + max2

#2) https://www.codewars.com/kata/52fba2a9adcd10b34300094c




listn = [
    [5,23,100,1],
    [50,10,8,9],
    [5,6,2,3],
    [11,7,4,49]
]

#3) https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

