# 6kyu:
# 1) https://www.codewars.com/kata/58539230879867a8cd00011c/train/python
def find_children(dancing_brigade):
    my_dict = {}
    list1 = []
    
    for i in dancing_brigade:
        if i.isupper():
            my_dict[i] = ""
            
    for i in dancing_brigade:
        if i.islower():
            my_dict[i.upper()] += i
            
    for x, y in my_dict.items():
        list1.append(x + y)
        
    return "".join(sorted(list1))

# 2) https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python
def string_transformer(s):
    return " ".join(s.swapcase().split(" ")[::-1])

# 3) https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/train/python
def hamming(a,b):
    x = 0
    
    for i in range(len(b)):
        if a[i] != b[i]:
            x += 1
    return x
