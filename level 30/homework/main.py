#Codewars answers are located in the codewars folder
#I couldn't solve the fifth problem

# 2) გააკეთეთ manual_replace ფუნქცია
def manual_replace(s1,char,replace_char):
    res = ""

    for i in s1:
        if i == char:
            res += replace_char
        else:
            res += i
        
    return res

print(manual_replace("Hello World", "o", "0"))

# 3) გააკეთეთ manual_len ფუნქცია
def manual_len(s):
    count = 0
    for i in s:
        count += 1
    return count

print(manual_len("123ww8i960"))
print(len("123ww8i960"))