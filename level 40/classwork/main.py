#1) https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence if char in vowels)
#2) https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string_):
    res  = ""
    for i in string_:
        if i not in "aeiouAEIOU":
            res += i
            
    return res
#3) https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    res = ""
    
    for i in str(num):
        res += str(int(i) ** 2)
        
    return int(res)