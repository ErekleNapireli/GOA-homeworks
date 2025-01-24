# prices = [10, 20, 30]
# discount_prices = list(map(lambda price: price * 0.9 >=18,prices))
# return (discounted_price)


# Level 54:
# კითხვებზე პასუხი (კომენტარებით):
# 1) რომლებია mutable მონაცემთა ტიპები?
# mutable monacemta tipebia: list,dictionary,set

# 2) რომლებია immutable მონაცემთა ტიპები?
# immutable monacemta tipebia:integer,float,string,tuple

# 3) რა ეწოდება lambda ფუნქციას მეორენაირად?
# anonymous function

# 4) რა განსხვავებაა map'სა და filter'ს შორის?
# map ighebs argumentad da abrunebs axal monacemebs,xolo filter abrunebs

# mxolod mat romlebic True aris
# 5) რა ჰქვია ორი სტრინგის შეერთებას?
# concatination(konkatinacia)

# MAPS
# გამოიყენეთ map ფუნქცია რომ შექმნათ list'ი სადაც იქნება ამ რიცხვების კვადრატები: [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) 

# დაწერეთ პროგრამა mapის გამოყენებით რომ გადაიყვანოთ ამ list'ში მოცემული celsius'ები fahrenheit'ში: [0, 20, 30, 40] (1 celsius == 33.8 fahrenheit)
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c:(9.0/5.0*c)+32.0, celsius))
print(fahrenheit)

# გამოიყენეთ map ფუნქცია რომ გაადიდოთ ყველა სიტყვის პირველი ასო ამ list'ში: ["hello", "world", "python"].
words = ["hello", "world", "python"]
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(capitalized_words)

# FILTERS
# გამოიყენეთ filter ფუნქცია რომ ამოწეროთ მხოლოდ ლუწი რიცხვები list'იდან: [1, 2, 3, 4, 5, 6, 7, 8].
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums1 = list(filter(lambda num: num % 2 == 0,nums1))
print(even_nums1)

# დაწერეთ პროგრამა filterის გამოყენებით რომ ამოწეროთ ისეთი string'ები რომლებიც შეიცავენ 4 სიმბოლოს ან მასზე მეტს: ["cat", "house", "tree", "car"].
listn = ["cat", "house", "tree", "car"]
strings= list(filter(lambda s: len(s) >= 4, listn))
print(strings)


# გამოიყენეთ filter ფუნქცია რომ ამოწეროთ სამის ჯერადი რიცხვები: [3, 9, 15, 22, 27, 30].
nums2 =[3, 9, 15, 22, 27, 30]
nums2_3jeradi = list(filter(lambda y: y % 3 == 0, nums2))
print(nums2_3jeradi)