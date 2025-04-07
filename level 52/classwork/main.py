# 1) https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
    total = 0  
    
    for i in range(number):  
        if i % 3 == 0 or i % 5 == 0:  
            total += i 
            
    return total
# 2) შექმენით ცვლადი რომელსაც მნიშვნელობად მიცემთ lambda ფუნქციას რომელიც აბრუნებს "Hello world!"ს
greeting = lambda: "Hello there"
print(greeting())  

# 3) შექმენით ცვლადი რომელსაც მნიშვნელობად მიცემთ lambda ფუნქციას რომელიც იღებს 2 პარამეტრს და აბრუნებს მათ ჯამს
sum1 = lambda num1 , num2: num1 + num2
print(sum1(4,5))