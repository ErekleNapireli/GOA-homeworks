#1)
def friend(x):
    return [i for i in x if len(i) ==4]


#2)
def maskify(cc):
    lenght = len(cc)
    if lenght > 4:
        last = cc[-4:]
        return "#" * (lenght -4) + last
    else:
        return cc

#3)


#4)


#5)