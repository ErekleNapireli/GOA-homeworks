# 6kyu:
# 1) https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/python

# 2) https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python
def good_vs_evil(good, evil):
    good = [int(i)for i in good.split()]
    evil = [int(i)for i in evil.split()]
    
    good_score = 0
    evil_score = 0
    
    for i in range(len(good)):
        match i:
            case 0:
                good_score += good[i]
            case 1:
                good_score += good[i] * 2
            case 2:
                good_score += good[i] * 3
            case 3:
                good_score += good[i] * 3
            case 4:
                good_score += good[i] * 4
            case 5:
                good_score += good[i] * 10
    
    for i in range(len(evil)):
        match i:
            case 0:
                evil_score += evil[i]
            case 1:
                evil_score += evil[i] * 2
            case 2:
                evil_score += evil[i] * 2
            case 3:
                evil_score += evil[i] * 2
            case 4:
                evil_score += evil[i] * 3
            case 5:
                evil_score += evil[i] * 5
            case 6:
                evil_score += evil[i] * 10
    
    if good_score == evil_score:
        return "Battle Result: No victor on this battle field"
    elif good_score > evil_score:
        return "Battle Result: Good triumphs over Evil"
    elif evil_score > good_score:
        return "Battle Result: Evil eradicates all trace of Good"


# 3) https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
