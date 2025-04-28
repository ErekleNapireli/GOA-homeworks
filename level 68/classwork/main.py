# Level 68:
# 1) https://www.codewars.com/kata/5fc7caa854783c002196f2cb/train/python
def speedify(st): 
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = [" "] * 125
    
    for i in range(len(st)):
        res[i + letters.find(st[i])] = st[i]
        
    return "".join(res).rstrip()
