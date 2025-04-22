import random





def combat():
    
    cHP = 60
    Def = 16
    ecHP = 40
    eDef = 16
    cAct = 1
    pAct = 1
    eAct = 0
    while cAct == 1:
        if pAct == 1:
            d6 = random.randint(1, 6)
            d20 = random.randint(1, 20)
            print("1. Weapon Attack")
            print("2. ", "Skill")
            print("3. Guard")
            print("4. Run")
            action = int(input("Choose your action:"))
            if action == 1:
                roll = 6 + d20
                if roll >= eDef:
                    ecHP = ecHP - d6
                    while ecHP <= 0:
                        print("Enemy Defeated. Continuing our tale...")
                        cAct = 0
                    else:
                        print("Enemy health: ", ecHP)
                        pAct = pAct - 1
                        eAct = 1
                else:
                    print("You missed the enemy.")
                    pAct = pAct - 1
                    eAct = 1
            elif action == 2:
                gear = {
                    "Skill": ((2 * d6) + 6)}
                roll = 6 + d20
                if roll >= eDef:
                    ecHP = ecHP - gear['Skill']
                    while ecHP <= 0:
                        print("Enemy Defeated. Continuing our tale...")
                        cAct == 0
                    else:
                        print("You missed the enemy.")
                        pAct = pAct - 1
                        eAct = 1
                else:
                    print("You missed the enemy.")
                    pAct = pAct - 1
                    eAct = 1
            elif action == 3:
                Def = 26
                pAct = pAct - 1
                eAct = 1
            elif action == 4:
                roll = d20
                while roll >= 16:
                    print("You have fled this fight. Continuing our story.")
                    cAct = 0
                else:
                    print("You could not run away.")
                    pAct = pAct - 1
                    eAct = 1
        else:
            if ecHP >= 10:
                d6 = random.randint(1, 6)
                d20 = random.randint(1, 20)
                roll = 6 + d20
                if roll >= Def:
                    cHP = cHP - (4 + d6)
                    while cHP == 0:
                        print("You have died. Would you like to play again?")
                        cAct = 0
                    else:
                        print("Your health: ", cHP)
                        pAct = 1
                        eAct = eAct - 1
                else:
                    print("The enemy missed.")
                    pAct = 1
                    eAct = eAct - 1
            else:
                print("The enemy fled before being defeated.")
                cAct = 0
combat()
print("Test end")
again = input("Run test again?")
if again == 'Y':
    combat()
else:
    print("Thank you")
