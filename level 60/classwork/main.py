# 1) https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

# 2) 


# 3https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

# 4) https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(lst):
    non_zeroes = [i for i in lst if i != 0]
    zeroes = [x for x in lst if x == 0]
    
    return non_zeroes + zeroes

