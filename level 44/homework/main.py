#1)
def longest(a1, a2):
    combined = set(a1 +a2 )
    sorted_str = "".join(sorted(combined))
    return sorted_str

#2)
def open_or_senior(data):
    listn = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            listn.append("Senior")
        else:
            listn.append("Open")
    return listn

#3)
def find_next_square(sq):
    sq = sq ** 0.5
    sq = sq + 1
    sq = sq ** 2
    
    if str(sq)[-2:] != ".0":
        return -1
    return sq

#4)

#5)
def reverse_words(text):
    return " ".join([i[::-1]for i in text.split(" ")])