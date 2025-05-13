# ყველა დავალებაში გამოიყენეთ map ან filter.
# 1) შექმენით რაიმე list'ი რომელშიც იქნება integer'ები და შემდეგ ამოწერეთ მხოლოდ ისეთი რიცხვები რომლებიც მეტია ან ტოლია 40'ის.
list1 = [25, 58, 0, 10, 40]
greater_or_equal_to_40 = list(filter(lambda a: a >= 40 , list1))
print(greater_or_equal_to_40)

# 2) შექმენით რაიმე list'ი რო   მელშიც იქნება integer'ები და შემდეგ გამოიტანეთ list'ი სადაც იქნება ყველა რიცხვის კვადრატი.
doubled_list = [20, 5, 15, 29]
doubled = list(map(lambda w: w ** 2 , doubled_list))
print(doubled)
# 3) შექმენით რაიმე list'ი რომელშიც იქნება string'ები და შემდეგ ამოწერეთ მხოლოდ ისეთები რომლებიც მთავრდება "a" სიმბოლოთი.
fruits = ["apple", "banana", "pineapple", ]
ends_with_a = list(filter(lambda x: x.endswith("a") , fruits))
print(ends_with_a)


# 4) https://www.codewars.com/kata/515e188a311df01cba000003/train/python
def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

# 5) https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python
def move(position, roll):
    return position + (roll * 2)
    
# 6) https://www.codewars.com/kata/5875b200d520904a04000003/train/python
def enough(cap, on, wait):
    total_people = on + wait
    if total_people <= cap:
        return 0  
    else:
        return total_people - cap 

# 7) https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python
def between(a,b):
    return list(range(a, b +1))

# 8) https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python
def say_hello(name):
    return "Hello, " + name