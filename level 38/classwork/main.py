#1) შექმენით list comprehension რომელიც შექმნის list'ს რიცხვებით 1'დან 100'მდე
list1 = [ i for i in range (1,100)]
print(list1)

#2) შექმენით list comprehension რომელიც შექმნის list'ს რიცხვებით 1'დან 100'მდე, 2-2'ის გამოტოვებით. (ანუ: [1, 3, 5...])
list2 = [i for i in range (1,100,2)]
print(list2)

#3)შექმენით რაიმე list'ი სახელებით და შემდეგ შექმენით list comprehension რომელიც შექმნის სახელების ახალ list'ს სადაც არ იქნება ასო "a" და ყველა string'ს თავში ექნება "#".
names = ["mevludi","nika","rezi","erekle","aleqsandre","anano"]
list3 = ["#"+ i.replace("a", "") for i in names]

print(list3)

#4)
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

#5)
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"


