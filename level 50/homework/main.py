#1)

#2)ივარჯიშეთ exception handling'ზე, საკლასო დავალებაში მოცემული დავალებებიდან, მეორედან მეოთხეს ჩათვლით თავიდან გააკეთეთ სხვანაირი მაგალითებით (სხვა ტიპის მაგალითები მოიყვანეთ, უბრალოდ ცვლადის სახელები არ შეცვალოთ)
# 2. დაწერეთ ისეთი კოდი სადაც იქნება NameError და გაუმკლავდით try/except'ით
try:
    name = "Erekle"
    print (last_name)
except NameError:
    print("The variable is not defined")

# 3. დაწერეთ ისეთი კოდი სადაც იქნება IndexError და გაუმკლავდით try/except'ით
try:
    listn = ["keyboard","mouse"]
    print(listn[4])
except IndexError:
    print("Out-of-range index")

# 4. დაწერეთ ისეთი კოდი სადაც იქნება ValueError და გაუმკლავდით try/except'ით
try:
    int("Hello world")
except ValueError:
    print("Inappropriate value")

#3) შექმენით ფუნქცია რომელიც იღებს რიცხვებს, ზოგი იქნება სტრინგი ზოგი იქნება ინტეჯერი (მაგ: [10, "10"]) და გამოიტანეთ მათი ჯამი. (exception'ებს გაუმკლავდით try/except'ის გარეშე. hint: გამარტივებისთვის გამოიყენეთ list comprehension
def summation(listn):
    count = 0

    for i in listn:
        count += int(i)

    return count

list1 = ["10", 11, "123", 22, 143, "70"]
print(summation(list1))
# 4) https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
def str_count(strng, letter):
    return strng.count(letter)
#;
def str_count(strng, letter):
    count = 0
    for i in strng:
        if i == letter:
            count += 1
            
    return count

# 5) https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/python
def is_even(n): 
    if n % 2 == 0:
        return True
    return False