#1)
def fake_bin(x):
    return x.replace("1", "0").replace("2","0").replace("3", "0").replace("4","0").replace("5", "1").replace("6","1").replace("7", "1").replace("8","1").replace("9", "1")

#2)
def string_to_array(s):
    return s.split(" ")


# შექმენით manual_min ფუნქცია

def manual_min(numbers):

    min_value = float('inf')

    for i in numbers:
        min_value = i if i < min_value else min_value

    return min_value

print(manual_min([5, 2, 9, 1, 7]))

# შექმენით manual_max ფუნქცია

def manual_max(numbers):

    max_value = float('inf')

    for i in numbers:
        max_value = i if i > max_value else max_value

    return max_value

print(manual_max([5, 2, 9, 1, 7]))