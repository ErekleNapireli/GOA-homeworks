#1) გაიხსენეთ და ახსენით წესები რომლებიც მუშაობს ყველა ლოგიკურ ოპერატორზე რაც დღეს ვისწავლეთ (and, or, not)
# and ნიშნავს და'ს,or ნიშნავს ან'ს, not ნიშნავს არ არის

#2) შექმენით and ოპერატორის მეშვეობით 5 სხვადასხვა მაგალითი
num1 = 20
num2 = 30
if num1 == 20 and num2 == 30:
    print("True")

if num1 and num2 == 30:
    print("True")
print("False")

if num1 >= 20 and num2 == 10:
    print("True")
print("False")

if num2 and num1 > 10:
    print("True")
print("False")

if num1 and num2 >= 20:
    print("True")
print("False")

#3) შექმენით or ოპერატორის მეშვეობით 5 სხვადასხვა მაგალითი
num3 = 75
num4 = 50

if num3 or num4 == 50:
    print("50")
print("False")

if num3 or num4 >= 49:
    print("True")
print("False")

if num3 == 50 or num4 > 40:
    print("True")
print("False")

if num3 or num4 <100:
    print("True")
print("False")

if num3 <20 or num4 > 30:
    print("True")
print("False")

#4)შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ 5 მაგალითი
numx1 = 30
numx2 = 40
if numx1 and numx2 == 50 or numx1 and numx2 > 20:
    print("True")
print("False")

if numx1 and numx2 == 100 or numx1 and numx2 >= 40:
    print("True")
print("False")

if numx1 and numx2 == 50 or numx1 and numx2 >20:
    print("True")
print("False")


if numx1 or numx2 == 50 and numx1 and numx2 > 20:
    print("True")
print("False")


if numx1 and numx2 == 20 and numx1 and numx2 > 20:
    print("True")
print("False")

