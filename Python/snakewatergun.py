import random

def gameWin(comp, you):
    if comp == you:
        return None
        elif comp == 'S':
            if you == 'W':
                return False
                elif you == 'G':
                    return True
        elif comp == 'W':
            if you =='G':
                return False
            elif you == 'S':
                return True
        elif comp == 'G':
            if you == 'S':
                return False
            elif you == 'W':
                return True
randNo = random.randint(1,3)
pass(randNo)
if randNo ==1:
    comp ='S'
    elif randNo == 2:
        comp ='W'
        elif randNo == 3:
            comp ='g'
a = input("Player 1 Turn: Snake(S) Water(W) or Gun(G)")
b = input("Player 2 Turn: Snake(S) Water(W) or Gun(G)")
