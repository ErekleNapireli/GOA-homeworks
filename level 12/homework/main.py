# 2) გააკეთეთ and ოპერატორის 10 მაგალითი და სანამ გაუშვებთ კომენტარად მიაწერეთ თქვენი აზრით რა იქნება შედეგი (არ არის აუცილებელი მხოლოდ 2 Input'ი იყოს, შეიძლება იყოს 10'იც, ანუ მაგალითად: True and True and False and False and True (5 input))

# 1. ორივე True, ამიტომ შედეგი იქნება True
print(True and True)

# 2. ერთი False, ამიტომ შედეგი იქნება False
print(True and False)

# 3. ორივე False, ამიტომ შედეგი იქნება False
print(False and False)

# 4. სამი True, ამიტომ შედეგი იქნება True
print(True and True and True)

# 5. ერთი False შუაში, ამიტომ შედეგი იქნება False
print(True and False and True)

# 6. ოთხი False და ერთი True, შედეგი იქნება False
print(False and False and False and False and True)

# 7. ყველა False, ამიტომ შედეგი იქნება False
print(False and False and False and False and False)

# 8. 10 Input, აქედან ერთი False, ამიტომ შედეგი იქნება False
print(True and True and True and True and True and True and True and True and True and False)

# 9. 10 Input, ყველა True, ამიტომ შედეგი იქნება True
print(True and True and True and True and True and True and True and True and True and True)

# 10. აქ შედეგი იქნება False
print((True and True) and (False and True))

# 3) გააკეთეთ or ოპერატორის 10 მაგალითი და სანამ გაუშვებთ კომენტარად მიაწერეთ თქვენი აზრით რა იქნება შედეგი

# 1. ორივე True, ამიტომ შედეგი იქნება True
print(True or True)

# 2. ერთი True და ერთი False, ამიტომ შედეგი იქნება True
print(True or False)

# 3. ორივე False, ამიტომ შედეგი იქნება False
print(False or False)

# 4. ყველა True, ამიტომ შედეგი იქნება True
print(True or True or True)

# 5. ერთი True შუაში, ამიტომ შედეგი იქნება True
print(False or True or False)

# 6. ყველა False და ერთი True, შედეგი იქნება True 
print(False or False or False or False or True)

# 7. ყველა False, ამიტომ შედეგი იქნება False
print(False or False or False or False or False)

# 8. შედეგი იქნება True რადგან ყველა True არის ერთის გარდა, რომელიც True არის
print(False or False or False or False or False or False or False or False or False or True)

# 9. 10 შედეგი იქნება True
print(True or True or True or True or True or True or True or True or True or True)

# 10.  შედეგი იქნება True
print((False or False) or (True or False))

# 4) შეურიეთ or და and ოპერატორები და გააკეთეთ ისევ 10 მაგალითი წინა დავალებების მსგავსად

print(True and False or True)

print(False or True and True)

print(True and (False or True))

print((True and False) or (False and True))

print(False and True or True and False)

print(True or False and False or True)

print((False or True) and (True or False))

print(True and True or False and False)

print((True or False) and (False or False))

print((True and True) or (False or True and False))

# 5) შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ ისევ 10 მაგალითი წინა დავალებების მსგავსად

print(5 > 3 and 2 < 4)
print(7 != 7 or 4 <= 4)
print(not (3 == 3) and 6 > 1)
print((10 >= 5) or (2 == 3 and 4 > 1))
print(8 < 2 or 5 == 5 and 9 >= 9)
print((4 != 4 or 3 > 1) and 2 <= 2)
print(not (6 < 3 or 2 > 1) and 5 == 5)
print(3 + 2 == 5 and 10 / 2 > 4)
print(7 * 2 != 14 or 12 // 3 == 4)
print((10 > 3 and 2 < 1) or (5 >= 5))


