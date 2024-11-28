
#1) შექმენით ფუნქცია რომელიც ტერმინალში გამოიტანს goodbye world'ს
def goodbye():
    print("goodbye word")
    goodbye()

def name(name1):
    return "goodbye " + name1

print(name(input("Enter your name:")))

