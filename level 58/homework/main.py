# 1)https://www.codewars.com/kata/58bf9bd943fadb2a980000a7
def who_is_paying(name):
    return [name, name[:2]] if name != name[:2] else [name]

# 2)https://www.codewars.com/kata/59342039eb450e39970000a6
# 3)https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
def is_uppercase(inp):
    return inp == inp.upper()

# 4)https://www.codewars.com/kata/53d16bd82578b1fb5b00128c
def grader(score):
    if score > 1 or score < 0.6:
        return "F"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
# 5)https://www.codewars.com/kata/570669d8cb7293a2d1001473
def if_chuck_says_so():
    return bool("")

