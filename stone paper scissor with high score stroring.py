import random
def game():
    v=0
    youdict={
        "stone":0,
        "paper":1,
        "scissors":-1
    }
    revdict={
        0:"stone",
        1:"paper",
        -1:"scissors"
    }
    while True:
        c=random.choice([0,1,-1])
        youstr = input("Enter your move: ").strip().lower()
        if youstr not in youdict:
            print("Invalid move, try again.")
            continue
        you = int(youdict[youstr])
        print(f"Computer's Move: {revdict[c]}")
        diff=c-you
        if diff == -1 or diff==2:
            print("You Win")
            v+=1
        elif diff==1 or diff==-2:
            print("You Lose")
            break
        else:
            print("It's a Tie")
    return v


v=game()
print(f"Final Score: {v}")

f=open("Hi-score.txt", "w")
f.write(str(v))
f.close()