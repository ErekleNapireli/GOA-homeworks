# 1) https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def solution(text, ending):
    if ending in text[-1] in ending: 
        return True
    else:
        return False

# 2) https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(st):
    listn = []
    
    for i in range(len(st)):
        listn.append((st[i] * (i + 1)).capitalize())
        
    return "-".join(listn)

# 3) https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def DNA_strand(dna):
    new_dna = ""
    for i in dna:
        if i =="A":
            new_dna += "T"
        elif i =="T":
            new_dna += "A"
        elif i =="C":
            new_dna += "G"
        elif i == "G":
            new_dna += "C"
            
    return new_dna

# 4) https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    x = min(numbers)
    numbers.remove(x)
    y = min(numbers)
    return x + y

# 5) https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
def get_sum(a,b):
    if a ==b:
        return a
    
    if a> b:
        a, b = b, a
        
    return sum(range(a, b +1))