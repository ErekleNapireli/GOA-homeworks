# 2) Use the map function to double the numbers in a list: [2, 4, 6, 8, 10].
numbers = [2, 4, 6, 8, 10]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) 

# 3) Write a program using map to concatenate "Hello, " to each name in a list: ["Alice", "Bob", "Charlie"].
string = ["Alice", "Bob", "Charlie"]
concatenate = list(map(lambda a:"Hello, " + a, string))
print(concatenate)

# 4) Use map to calculate the lengths of strings in a list: ["apple", "banana", "kiwi"].
len_list = ["apple", "banana", "kiwi"]
len_calc = list(map(len, len_list ))
print(len_calc)

# 5) Use the filter function to keep only positive numbers from a list: [-5, 3, -2, 7, 0, 10].
list_num = [-5, 3, -2, 7, 0, 10]
keep_positive = list(filter(lambda y: y >= 0, list_num))
print(keep_positive)

# 6) Write a program using filter to extract words starting with the letter "p" from a list: ["pear", "apple", "peach", "grape"].
fruits = ["pear", "apple", "peach", "grape"]
words_starting_with_p = list(filter(lambda word: word.startswith("p"), fruits))
print(words_starting_with_p)
# filter_p = list(filter(lambda ()))

# 7) Use filter to find numbers greater than 50 in a list: [10, 55, 42, 78, 65, 20].
num2 = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda u: u > 50 ,num2 ))
print(greater_than_50)
