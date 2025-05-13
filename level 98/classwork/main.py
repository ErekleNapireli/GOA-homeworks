# 5kyu:
# 1) https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(lst):
    non_zeroes = [i for i in lst if i != 0]
    zeroes = [x for x in lst if x == 0]
    
    return non_zeroes + zeroes

# 2) https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
def generate_hashtag(s):
    s = '#' + s.title()
    s = ''.join(s.split())
    if len(s) in range(2,141):       
        return s
    else:
        return False
    
# 3) https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
def pig_it(text):
    res= []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + "ay")
        else:
            res.append(i)
            
    return " ".join(res)

# 4) https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

# 5) https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

# 6) https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
