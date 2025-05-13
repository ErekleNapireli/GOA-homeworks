#1)
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"

#2)
def cockroach_speed(s):
    cms = int(s * 27.7778)
    return cms

#3)
def switch_it_up(number):
    dict = {
        0 : "Zero",
        1 : "One",
        2 : "Two",
        3 : "Three",
        4 : "Four",
        5 : "Five",
        6 : "Six",
        7 : "Seven",
        8 : "Eight",
        9 : "Nine",
    }
    return dict.get(number)

#4)
def square(n):
    return n ** 2

#5)
def remove_every_other(my_list):
    return my_list[::2]