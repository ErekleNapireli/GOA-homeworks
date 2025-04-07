#1)
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    sum_numbers = sum(numbers)
    average = sum_numbers / len(numbers)
    return average

#2)
def smash(words):
    return " ".join(words)


#3)
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

#4)
def hero(bullets, dragons):
    if  bullets /2 >= dragons:
        return True
    else:
        return False

#5)
def better_than_average(class_points, your_points):
    x = sum(class_points) / len(class_points)
    return your_points >=x

#2)გააკეთეთ manual_find ფუნქცია

print("hello world".find("x"))

def manual_find(s,i):
    y=0
    for x in s:
        if i == x:
            return y
        else:
            y = y + 1
    return -1

print(manual_find("hello world","x"))

#3) გააკეთეთ manual_swapcase ფუნქცია

def manual_swapcase(s):
    res = ""

    for i in s:
        if i.islower():
            res = res + i.upper()
        else:
            res = res+ i.lower()

    return res

print(manual_swapcase("HelLO wOrLD"))

