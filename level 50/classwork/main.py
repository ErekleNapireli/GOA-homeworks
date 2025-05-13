# 1) ჩამოთვალეთ ყველა დღეს ნასწავლი error'ის ტიპი და ახსენით რა რა შემთხვევაში გამოდის
# დღეს ვისწავლეთ 5 ერორის ტიპი, ესენია: SyntaxError,NameError,IndexError,ValueError და TypeError
# SyntaxError გამოდის იმ შემთხვევაში როცა არასწორი სინტაქსი გვაქვს მითითებული ან რამე გვაკლია 
# NameError არის არასწორი ცვლადის სახელის გამოტანა
# IndexError არის არასწორი ინდექსის გამოყენება
# ValueError არის არასწორი ვალუის გამოყენება 
# TypeError არის არასწორი ვალუების გამოყენება და მიმატება მაგალითად
# 2) დაწერეთ ისეთი კოდი სადაც იქნება NameError და გაუმკლავდით try/except'ით
try:
    name = "Erekle"
    print (last_name)
except NameError:
    print("The variable is not defined")

# 3) დაწერეთ ისეთი კოდი სადაც იქნება IndexError და გაუმკლავდით try/except'ით
try:
    listn = ["keyboard","mouse"]
    print(listn[3])
except IndexError:
    print("Out-of-range index")

# 4) დაწერეთ ისეთი კოდი სადაც იქნება ValueError და გაუმკლავდით try/except'ით
try:
    int("Hello world")
except ValueError:
    print("Inappropriate value")

# 5) კომენტარებით ახსენით რაში გვადგება try/except
# try/except არის გამოსადეგი რომ Error-ის მიუხედავად მაინც გავაგრძელოთ კოდი და ვნახოთ შედეგი. 