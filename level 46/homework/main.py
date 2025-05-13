#1)
def remove_duplicates(str1):
    res = ""

    for i in str1:
        if i not in res:
            res += i

    return res

print (remove_duplicates("Hello World!"))