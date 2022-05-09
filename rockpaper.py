print("Rock Paper Scissors game")
a=input("Player 1 :")
b=input("Player 2 :")

c=a.lower()
d=b.lower()
#a="scissor"
#b="paper"

if c==d:
    print("Its a tie")
elif c=="scissor":
    if d=="paper":
        print("Player 1 is the winner")
    else:
        print("Player 2 is the winner")
elif c=="paper":
    if d=="scissor":
        print("Player 2 is the winner")
    else:
        print("Player 1  is the winner")
elif c=="rock":
    if d=="paper":
        print("Player 2 is the winner")
    else:
        print("Player 1 is the winner")        
