# 1) https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/python
def count_red_beads(n):
    return (n - 1) * 2

# 2) https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python
def generate_shape(n):
    return "\n".join(n * "+" for i in range(n))  

# 3) https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python
def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else"Car Dead"

# 4) https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python
def adjacent_element_product(array):
    listn = []
    
    for i in range(len(array) - 1):
        listn.append(array[i] * array[i + 1])
        
    return max(listn)

# 5) https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python
def filter_string(st):
    return int("".join(i for i in st if i.isdigit()))