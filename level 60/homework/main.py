

# 8kyu:
# 1) https://www.codewars.com/kata/56efc695740d30f963000557/train/python
def to_alternating_case(string):
    return string.swapcase()

# 2) https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python
def correct(s):
    return s.replace("5","S").replace("0","O").replace("1","I")
# 3) https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/python

# 4) https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
def is_palindrome(s):
    return s.upper() == s[::-1].upper()
# 5kyu:
# 1) https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1::] + i[0] + "ay")    
        else:
            res.append(i)
        
    return " ".join(res)
    
# + https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python