import random

HP = 60
eHP = 40
cAct = 1
pAct = 1
eAct = 0

while cAct == 1:
    if pAct == 1:
        d6 = random.randint(1, 6)
        eHP = eHP - d6
        print("Enemy HP: ", eHP)
        pAct = pAct - 1
        eAct = 1
        if eHP <= 0:
            print("You have won.")
            cAct = 0
    else:
        d4 = random.randint(1, 4)
        HP = HP - d4
        print("Your HP: ", HP)
        eAct = eAct - 1
        pAct = 1
        if HP <= 0:
            print("You have died.")
            cAct = 0
print("End test.")
again = input("Would you like to run it again? ")
if again == "y":
    pAct = 1
    eAct = 0
