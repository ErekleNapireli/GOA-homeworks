#1) https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string):
    string = "".join(sorted(string.lower()))
    
    for i in range(len(string) - 1):
        if string[i] == string[i +1]:
            return False
        
    return True

#2) https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")

#3) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    res = [i.capitalize() for i in string.split(" ")]
    return " ".join(res)

#4) https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
def find_short(s):
    list1 = [len(i) for i in s.split(" ")]
    return min(list1)
