
#2) შექმენით ფუნქცია რომელიც დააბრუნებს "You got discount" თუ მომხმარებელი არის არასრულწლოვანი, სხვა შემთხვევაში დააბრუნებს "You didn't get discount"

def check_discount(age):
    if age < 18:
        return "You got discount"
    else:
        return "You didn't get discount"

age = int(input("Enter your age: "))
print(check_discount(age))\

#3) შექმენით ფუნქცია manual_reverse, რომელიც არგუმენტად მიიღებს string'ს და დააბრუნებს ამ string'ს ოღონდ შეტრიალებულად

def manual_reverse(string):
    return string[::-1]
input_string = input("Enter a string: ")
print(manual_reverse(input_string))