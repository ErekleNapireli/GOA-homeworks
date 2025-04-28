#1)
def abbrev_name(name):
    return name[0].upper() + '.' + name.split()[1][0].upper()


#3)
def simple_multiplication(number) :
    if number %2 !=0:
        return number * 9
    elif number%2 ==0:
        return number * 8

#4)
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

#5)
def invert(lst):
    res = []
    
    for i in lst:
        res.append(-i)
        
    return res
