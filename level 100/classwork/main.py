# Level 100:
# https://www.codewars.com/kata/search/my-languages?q=&r%5B%5D=-8&xids=completed&beta=false&order_by=sort_date%20desc

# 1)
def divide_numbers(x,y):
    return  x / y
#1) https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    split_s = sentence.split()
    new_lst = []
    for s in split_s:
        if len(s) >= 5:
            new_lst.append(s[::-1])
        else:
            new_lst.append(s)
    return " ".join(new_lst)
# 2) https://www.codewars.com/kata/53697be005f803751e0015aa/train/python
def encode(st):
    new_st = ""
    for s in st:
        if s == "a":
            new_st += "1"
        elif s == "e":
            new_st += "2"
        elif s == "i":
            new_st += "3"
        elif s == "o":
            new_st += "4"
        elif s == "u":
            new_st += "5"
        else:
            new_st += s
    return new_st
    
def decode(st):
    new_s = ""
    for i in st:
        if i == "1":
            new_s += "a"
        elif i == "2":
            new_s += "e"
        elif i == "3":
            new_s += "i"
        elif i == "4":
            new_s += "o"
        elif i == "5":
            new_s += "u"
        else:
            new_s += i
    return new_s
