#Codewars პასუხები:
#1)

#2)
def dna_to_rna(dna):
    return dna.replace("T", "U")
#3)
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False
#4)
def bmi(weight, height):
    bmi1 = weight / height ** 2
    if bmi1 <= 18.5:
        return "Underweight"
    elif bmi1 <= 25.0: 
        return "Normal"
    elif bmi1 <= 30.0:
        return "Overweight"
    else:
        return "Obese"