#1)
def rental_car_cost(d):
    everyday_rent = 40 * d
    if d >= 7:
        return d * 40 - 50
    elif d >= 3:
        return d * 40 - 20
    else:
        return d * 40
    
#2)
def quarter_of(month):
    if month in range (1,4):
        return 1
    elif month in range (4,7):
        return 2
    elif month in range (7,10):
        return 3
    else:
        return 4
#3)
def remove_exclamation_marks(s):
    return s.replace("!","")

#4)
def points(games):
    res = 0
    
    for i in games:
        if int(i[0]) > int(i[-1]):
            res += 3
        elif int(i[0]) == int(i[-1]):
            res += 1
        
    return res
#5)
def get_volume_of_cuboid(length, width, height):
    return length * width * height

#6) შექმენით in keyword'ის manual ფუნქცია

def manual_in(x,collection):
    for i in collection:
        if i == x:
            return True
    return False

print(manual_in('1',"2453532"))