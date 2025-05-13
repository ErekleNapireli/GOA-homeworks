# 7 kyu:
# https://www.codewars.com/kata/5fde1ea66ba4060008ea5bd9/train/python
def burner(c,h,o):
    water = co2 = methane = 0

    while h > 1 and o > 0:
        water += 1
        h -= 2
        o -= 1

    while c > 0 and o > 1:
        co2 += 1
        c -= 1
        o -= 2

    while c > 0 and h > 3:
        methane += 1
        c -= 1
        h -= 4

    return water,co2,methane

# https://www.codewars.com/kata/5bb804397274c772b40000ca/train/python
def stack_height_2d(l):
    if l == 0 : return 0
    return round(1 + (l - 1)*0.86602,3)

# https://www.codewars.com/kata/57b5907920b104772c00002a/train/python
def height(n):
    height = cat = 2000000
    for i in range(n):
        cat /= 2.5
        height += cat
    return f'{height:.3f}'