#1)
def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 =="rock":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "paper":
        return "Draw!"
    elif p1 == "rock" and p2 == "rock":
        return "Draw!"
    elif p1 == "scissors" and p2 == "scissors":
        return "Draw!"

#2)
def is_divisible(n,x,y):
    return n % x + n % y == 0

#5)
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"