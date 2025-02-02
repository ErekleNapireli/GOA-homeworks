# https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e/train/python
def shorten_to_date(long_date):
    date = long_date.split(",")
    
    return date[0].strip()
# https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python
def name_shuffler(str_):
    splited = str_.split(" ")
    reverse_name = splited[::-1]
    return " ".join(reverse_name)

# https://www.codewars.com/kata/526c7363236867513f0005ca
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# https://www.codewars.com/kata/529eef7a9194e0cbc1000255
# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

# https://www.codewars.com/kata/52fb87703c1351ebd200081f
def what_century(year):

    century = (int(year) - 1) // 100 + 1

    if 10 <= century % 100 <= 20:  
        suffix = "th"
    else:
        last_digit = century % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"

    return f"{century}{suffix}"
