import random

c = random.choice([0,1,2])
youstr=(input("Your move: "))
youdict={
    'snake':'1',
    'water':'0',
    'gun':'2'
}
you=int(youdict[youstr])

print(c)
if c==you:
    print("Its a draw")
else:
    if c==2 and you==0 :
        print('You Win')
    elif c==2 and you==1:
        print('You Lose')
    elif c==1 and you==2:
        print('You Win')
    elif c==1 and you==0:
        print('You Lose')
    elif c==0 and you==1:
        print('You Win')
    elif c==0 and you==2:
        print('You Lose')
    else:
        print('NR')
