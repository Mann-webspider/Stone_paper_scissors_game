import random

def play(char, hmm ):
    global c,p
    if (char == hmm ):
        print(f"{char} is yours and {hmm} is computer")
        return "game tie "


    if (char == "s" ) and (hmm == "sc") or (char == "p") and (hmm == "s") or (char == "sc") and (hmm == "p"):
        print(f"{char} is yours and {hmm} is computer")
        p = p+1
        return p ,"player wins"


    print(f"{char} is yours and {hmm} is computer")
    c = c + 1
    return c, "player lose"


c = 0
p = 0
t= 10
while (t!=0):
    char = input("       S for stone, P for paper, SC for scissor:            \n\n")
    hmm = random.choice(["s", "p", "sc"])
    print(play(char,hmm))
    print(f"points of player is {p}")
    print(f"points of computer is {c}")
    t = t-1

    