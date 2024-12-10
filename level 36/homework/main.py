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

#3)
def remove_exclamation_marks(s):
    return s.replace("!","")

#5)
def get_volume_of_cuboid(length, width, height):
    return length * width * height