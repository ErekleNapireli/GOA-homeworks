#1) https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def friend(x):
    return [i for i in x if len(i) ==4]


#2) https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
def maskify(cc):
    length = len(cc)
    if length > 4:
        last = cc[-4:]
        return "#" * (length -4) + last
    else:
        return cc

#3) https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
def find_next_square(sq):
    root = sq ** 0.5
    
    if root == int(root):
        return (int(root) + 1) ** 2
    else:
        return -1

#4) https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python


#5) https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python