# 1) https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python
def greet(language):
    my_dict = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    return my_dict.get(language, 'Welcome')

# 2) https://www.codewars.com/kata/55ca77fa094a2af31f00002a/train/python
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# 3) https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
def two_sort(array):
    return '***'.join(sorted(array)[0])
# 4) https://www.codewars.com/kata/56170e844da7c6f647000063/train/python
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"
# 5) https://www.codewars.com/kata/50654ddff44f800200000007/train/python
def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
# 6) https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/train/python
def fix_the_meerkat(arr):
    return arr[::-1]
