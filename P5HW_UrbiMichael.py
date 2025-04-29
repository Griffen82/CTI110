# Michael Urbi
# April 17, 2025
# P5HW
# Creating a short adventure game using what we have learned thus far

import random
# On April 27, 2025, used ChatGPT to help with some debugging and cleaning of the code.
# https://chatgpt.com/share/680efa6a-86c8-8001-970d-9d1aeab58f25

# Gear Dictionaries
armor = {"Defense":10}
cloak = {"Defense":8}
robe = {"Defense":6}
weapons = {
    "dagger": {"Attack":4},
    "spear": {"Attack":8},
    "staff": {"Attack":4},
    "sword": {"Attack":6}}

# Game Over Function
def game_over(ending):
    if ending == 0:
        print("You have died. Would you like to play again?")
    if ending == 1:
        print("You ignore the conflict. Your next few days are peaceful before dark omens arise.")
    if ending == 3:
        print("After the bout with the bandit leader. You go about to make sure the children are unharmed.")
        print("As you check them over, you notice that both children have nonhuman characteristics; noticably, thier ears look elvish.")
        print("The children also have pale skin. Confused, you look to the fallen bandit leader. The leader is also a pale skinned elf.")
        print("Still confused, you know you will have questions for the woman when you get the children back.")
        print("However, those questions will have to wait for another time.")
        print("Thanky you for playing this opening act.")

## Character Function
def char_create():
    bg = {}
    gear = {}
# Name your character
    name = input("Please enter your name: ")
# Choose a lineage
    print("1. Urchin; Str:5, Agi:6, Vit:4, Int:3, Luck:6")
    print("2. Tradesman; Str:4, Agi:4, Vit:6, Int:6, Luck:4")
    print("3. Noble; Str:3, Agi:5, Vit:5, Int:7, Luck:4")
    lineage = int(input("Please select a Lineage:"))
    while lineage < 1 or lineage > 3:
        print("Invalid selection, please select again.")
        lineage = int(input("Please select a Lineage:"))
    else:
        if lineage == 1:
            char = {
                "Name":name,
                "Str":5,
                "Agi":6,
                "Vit":4,
                "Int":3,
                "Luck":6}
            bg.update({"Lineage":"Urchin"})
        elif lineage == 2:
            char = {
                "Name":name,
                "Str":4,
                "Agi":4,
                "Vit":6,
                "Int":6,
                "Luck":4}
            bg.update({"Lineage":"Tradesman"})
        elif lineage == 3:
            char = {
                "Name":name,
                "Str":3,
                "Agi":5,
                "Vit":5,
                "Int":7,
                "Luck":4}
            bg.update({"Lineage":"Noble"})
# Add a vocation and vocational skill
    
    print("1. Champion: +2 Str. Start with armor and sword.")
    print("2. Thief: +2 Agi. Start with cloak and dagger.")
    print("3. Guard: +2 Vit. Start with armor and spear.")
    print("4. Mage: +2 Int. Start with robe and staff.")
    print("5. Con: +2 Luck. Start with robe and dagger.")
    voc = int(input("Please select a vocation: "))
    while voc < 1 or voc > 5:
        print("Invalid selection, please select again.")
        voc = int(input("Please select a vocation: "))
    else:
        if voc == 1:
            iStr = int(char.get("Str"))
            nStr = iStr + 2
            char.update({"Str":nStr})
            gear = {"Armor":armor, "Weapon":"sword"}
            bg.update({"Vocation":"Champion"})
            print("1. Battlecry: Heal d10 damage and add d6 damage to next attack.")
            print("2. Heavy Strike: Add double Str to next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill":"Battlecry"})
                elif vocskl == 2:
                    gear.update({"Skill":"Heavy_Strike"})
        elif voc == 2:
            iAgi = int(char.get("Agi"))
            nAgi = iAgi + 2
            char.update({"Agi":nAgi})
            gear = {"Armor":cloak, "Weapon":"dagger"}
            bg.update({"Vocation":"Thief"})
            print("1. Vital Strike: % chance to deal lethal damage.")
            print("2. Shadows: % chance to avoid the next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": "Vital_Strike"})
                elif vocskl == 2:
                    gear.update({"Skill": "Shadows"})
        elif voc == 3:
            iVit = int(char.get("Vit"))
            nVit = iVit + 2
            char.update({"Vit":nVit})
            gear = {"Armor":armor, "Weapon":"spear"}
            bg.update({"Vocation":"Guard"})
            print("1. Lunge: Add your Vit stat to damage.")
            print("2. Parry: % chance to avoid the next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": "Lunge"})
                elif vocskl == 2:
                    gear.update({"Skill": "Parry"})
        elif voc == 4:
            iInt = int(char.get("Int"))
            nInt = iInt + 2
            char.update({"Int":nInt})
            gear = {"Armor":robe, "Weapon":"staff"}
            bg.update({"Vocation":"Mage"})
            print("1. Firebolt: Attack deals 3x Int damage.")
            print("2. Ice Wall: % chance to avoid the next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": "Firebolt"})
                elif vocskl == 2:
                    gear.update({"Skill": "Ice_Wall"})
        elif voc == 5:
            iLuck = int(char.get("Luck"))
            nLuck = iLuck + 2
            char.update({"Luck":nLuck})
            gear = {"Armor":robe, "Weapon":"dagger"}
            bg.update({"Vocation":"Con"})
            print("1. Confusion: % chance enemy hurts themself.")
            print("2. Beginners Luck: % chance attack deals triple damage.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": "Confusion"})
                elif vocskl == 2:
                    gear.update({"Skill": "Beginners_Luck"})
    player = {"Stats":char,
              "Background":bg,
              "Gear":gear} 
    print(char)
    print(bg)
    print(gear)
    print("Thank you for creating your character. Let us begin...")
    return(player)
    
## Combat Function
    
def combat(player, enemy):
    print("-"*150)
    input("Press Enter to initiate combat")
    def dice(sides):
       return random.randint(1, sides) 
    print(player["Stats"])
    print(player["Gear"])
    print(enemy)

    def dialog(option, Dam, cHP, ecHP):
        if option == 0:
            game_over(0)
        elif option == 1:
            print("Your attack missed the enemy.")
        elif option == 2:
            print("You've struck the enemy for", Dam, "Damage.")
            print("The enemy has ", ecHP, "left.")
        elif option == 3:
            print("You've confused the enemy. The enemy attacks themself for", Dam, "Damage.")
            print("The enemy has ", ecHP, "left.")
        elif option == 5:
            print("The enemy missed you.")
        elif option == 6:
            print("The enemy bit you for", Dam, "Damage.")
            print("You have ", cHP, "HP left.")
        elif option == 7:
            print("The enemy stabbed you for", Dam, "Damage.")
            print("You have ", cHP, "HP left.")
        elif option == 8:
            print("The enemy struck you for", Dam, "Damage.")
            print("You have ", cHP, "HP left.")
        elif option == 10:
            print("Enemy Defeated.")
            print("Continuing our tale...")
            print("-"*150)
    
# Skill abilities for combat
    def Skill(vocsk, player, cHP, Def, pAct, enemy, ecHP, eDef, eAct):
        pAct = 0
        eAct = 0
        if vocsk == "Battlecry":
            heal = dice(10)
            cHP = cHP + heal
            print("You heal", heal, "HP.")
            roll = player["Stats"]["Agi"] + dice(20)
            print("Your current Health: ", cHP)
            if roll >= eDef:
                dam = dice(weapons[player["Gear"]["Weapon"]]["Attack"]) + dice(6) + player["Stats"]["Str"]
                ecHP = ecHP - (dam)
                dialog(2, dam, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)
            else:
                dialog(1, 0, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Heavy_Strike":
            roll = player["Stats"]["Agi"] + dice(20)
            print(roll)
            if roll >= eDef:
                dam = dice(weapons[player["Gear"]["Weapon"]]["Attack"]) + (2 * player["Stats"]["Str"])
                ecHP = ecHP - (dam)
                dialog(2, dam, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)
            else:
                dialog(1, 0, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Vital_Strike":
            roll = player["Stats"]["Agi"] + dice(20)
            if roll >= eDef:
                gamble = dice(100)
                if gamble <= 15 * (player["Stats"]["Agi"]):
                    ecHP = ecHP - 9999
                    dialog(2, "lethal", cHP, ecHP)
                    return (cHP, ecHP, Def, pAct, eAct)
                else:
                    dam = dice(weapons[player["Gear"]["Weapon"]]["Attack"]) + player["Stats"]["Str"]
                    ecHP = ecHP - dam
                    dialog(2, dam, cHP, ecHP)
                    return (cHP, ecHP, Def, pAct, eAct)
            else:
                dialog(1, 0, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Shadows":
            gamble = dice(100)
            if gamble <= 15 * (player["Stats"]["Agi"]):
                print("You conceal yourself in a nearby shadow.")
                Def = 9999
                return (cHP, ecHP, Def, pAct, eAct)
            else:
                print("You could not conceal yourself in time.")
                return (cHP, ecHP, Def, pAct, eAct)
                
        if vocsk == "Lunge":
            roll = player["Stats"]["Agi"] + dice(20)
            if roll >= eDef:
                dam = dice(weapons[player["Gear"]["Weapon"]]["Attack"]) + player["Stats"]["Vit"] + player["Stats"]["Str"]
                ecHP = ecHP - dam
                dialog(2, dam, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)
            else:
                dialog(1, 0, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Parry":
            gamble = dice(100)
            if gamble <= 15 * (player["Stats"]["Vit"]):
                Def = 9999
                print("You go to parry the next blow.")
                return (cHP, ecHP, Def, pAct, eAct)
            else:
                print("You missed parrying the blow.")
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Firebolt":
            roll = player["Stats"]["Int"] + dice(20)
            if roll >= eDef:
                dam = (3 * (player["Stats"]["Int"]))
                ecHP = ecHP - dam
                dialog(2, dam, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)
            else:
                dialog(1, 0, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Ice_Wall":
            gamble = dice(100)
            if gamble <= 15 * (player["Stats"]["Int"]):
                print("You cast an Ice Wall between you and the enemy.")
                Def = 9999
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Confusion":
            gamble = dice(100)
            if gamble <= 15 * (player["Stats"]["Luck"]):
                dam = dice(enemy["Attack"])
                ecHP = ecHP - dam
                dialog(3, dam, cHP, ecHP)
                pAct = 2
                eAct = -1
                return (cHP, ecHP, Def, pAct, eAct)

        if vocsk == "Beginners_Luck":
            gamble = dice(100)
            if gamble <= 15 * (player["Stats"]["Luck"]):
                dam = ((3 * dice(weapons[player["Gear"]["Weapon"]]["Attack"])) + player["Stats"]["Str"])
                ecHP = ecHP - dam
                dialog(2, dam, cHP, ecHP)
                return (cHP, ecHP, Def, pAct, eAct)
            else:
                roll = roll = player["Stats"]["Agi"] + dice(20)
                if roll >= eDef:
                    dam = (dice(weapons[player["Gear"]["Weapon"]]["Attack"]) + player["Stats"]["Str"])
                    ecHP = ecHP - dam
                    dialog(2, dam, cHP, ecHP)
                    return (cHP, ecHP, Def, pAct, eAct)
                else:
                    dialog(1, 0, cHP, ecHP)
                    return (cHP, ecHP, Def, pAct, eAct)
            
    def defense(protection):
        return protection["Defense"]

    def calculate_hp(vit):
        return vit * 10

    health = int(player["Stats"]["Vit"])
    cHP = calculate_hp(health)

    eVit = int(enemy["Vit"])
    ecHP = calculate_hp(eVit)

    def calculate_wea_dam(weapon):
        dice_size = weapon

        damage = random.randint(1, dice_size)
        print("Weapon damage: ", damage)
        return (damage)

    Def = defense(player["Gear"]["Armor"])
    eDef = int(enemy["Defense"]) + 5

    cAct = 1
    pAct = 1
    eAct = 0
    
    while cAct == 1:
        if pAct == 1:
            Def = defense(player["Gear"]["Armor"]) + 5
            print("Your current health: ", cHP)
            print("Enemy current health: ", ecHP)
            print("1. Weapon Attack")
            skl = player["Gear"]["Skill"]
            print("2.", skl)
            print("3. Guard")
            print("4. Run")
            action = int(input("Choose your action:"))
            if action == 1:
                roll = player["Stats"]["Agi"] + dice(20)
                if roll >= eDef:
                    Att = int(player["Stats"]["Str"])
                    weapon_name = player["Gear"]["Weapon"]
                    wea = int(calculate_wea_dam(weapons[player["Gear"]["Weapon"]]["Attack"]))
                    dam = Att + wea
                    ecHP = ecHP - (dam)
                    dialog(2, dam, cHP, ecHP)
                    if ecHP <= 0:
                        dialog(10, 0, cHP, ecHP)
                        cAct = 0
                    else:
                        pAct = pAct - 1
                        eAct = 1
                else:
                    dialog(1, 0, cHP, ecHP)
                    pAct = pAct - 1
                    eAct = 1
            elif action == 2:
                result = Skill(player["Gear"]["Skill"], player, cHP, Def, pAct, enemy, ecHP, eDef, eAct)
                cHP, ecHP, Def, pAct, eAct = result
                if ecHP <= 0:
                    dialog(10, 0, cHP, ecHP)
                    cAct = 0
                else:
                    pAct = pAct - 1
                    eAct = 1
            elif action == 3:
                print("You take a defensive position against the next attack.")
                Def = Def + 10
                pAct = pAct - 1
                eAct = 1
            elif action == 4:
                roll = d20
                if roll >= 11:
                    print("You have fled this fight. Continuing our story.")
                    pAct = 0
                    cAct = 0
                else:
                    print("You could not run away.")
                    pAct = pAct - 1
                    eAct = 1
        else:
            print("Your defense is ", Def)
            if ecHP >= 4:
                roll = enemy["Agi"] + dice(20)
                if roll >= Def:
                    dam = enemy["Attack"] + dice(6)
                    cHP = cHP - dam
                    dialog(8, dam, cHP, ecHP)
                    if cHP <= 0:
                        eAct = 0
                        cAct = 0
                    else:
                        pAct = 1
                        eAct = eAct - 1
                else:
                    dialog(5, 0, cHP, ecHP)
                    pAct = 1
                    eAct = eAct - 1
            else:
                if dice(20) >= 19:
                    print("The enemy fled before being defeated.")
                    cAct = 0
                else:
                    roll = enemy["Agi"] + dice(20)
                    if roll >= Def:
                        dam = enemy["Str"] + dice(6)
                        cHP = cHP - dam
                        dialog(8, dam, cHP, ecHP)
                        if cHP <= 0:
                            dialog(10, 0, cHP, ecHP)
                            cAct = 0
                        else:
                            pAct = 1
                            eAct = eAct - 1
                    else:
                        dialog(5, 0, cHP, ecHP)
                        pAct = 1
                        eAct = eAct - 1
    return cHP
# Story function
def story(player):
    
# Enemy dictionaries
    Wolf = {
        "Name":"Wolf",
        "Str":4,
        "Agi":7,
        "Vit":4,
        "Int":2,
        "Luck":3,
        "Attack":6,
        "Defense":8}
    Bandit = {
        "Name":"Bandit",
        "Str":4,
        "Agi":5,
        "Vit":3,
        "Int":3,
        "Luck":3,
        "Attack":8,
        "Defense":10}
    Goblin = {
        "Name":"Goblin",
        "Str":3,
        "Agi":4,
        "Vit":2,
        "Int":4,
        "Luck":5,
        "Attack":4,
        "Defense":5}
    Boss = {
        "Name":"Boss",
        "Str":5,
        "Agi":6,
        "Vit":6,
        "Int":5,
        "Luck":4,
        "Attack":10,
        "Defense":8}

# Finale Function
    def finale(player):
        print("With the bandit down. You saved one of the children. However, you notice that the only ones left standing are you and the bandit leader.")
        print('"I do not know who you are, nor do I care. This is the only time I will ofter to let you leave with your life." The bandit leader proclaims.')
        print('"I have come to rescue the children. Give them back and you can leave." You declare. Hoping the bravado will convince them to surrender the child.')
        print('"You are a fool who has no idea what this is actually about." The bandit then smirks, "Fortunately for you, you will be dead long before it matters."')
        print("The leader takes a stance, and you know that diplomancy no longer applies. You prepare yourself to face this last foe.")
        result = combat(player, Boss)
        if result <= 0:
            game_over(0)
        else:
            game_over(3)
# Chapter Three Function
    def chapter_three(player):
        print("After defeating the goblin, you sneak closer and can see other goblins arguing with the bandits.")
        print("There are 2 bandits with carriers on their back. You can see the children, they appear asleep.")
        print('Straining to hear, you can barely catch the argument. "Pay big toll to pass camp," says a goblin.')
        print('"We already paid your toll, filth. Now let us pass before you lose the ability to spend it, " one of the bandits demands.')
        print('"You small, goblins large! Easy fight to get rid of you!" Shouts the goblin')
        print('The bandit leader responds. "Outnumbering us means nothing, maggot. This is your last chance to let us pass before we purge this hovel."')
        print("Sensing a potential advantage, you stealthily pick up a small stone and throw it while hiding at the bandit leader and mimicing the goblin.")
        print('"Kill them, get big pay."')
        print("The shout and rock throw both groups into chaos. The goblins and bandits begin fighting each other.")
        print("Unfortunately, the bandit leader spoke true. The pair of bandits quickly begin mowing down the goblins.")
        print("Before losing the advantage of the chaos. You advance on the other bandit to try and take him down.")
        result = combat(player, Bandit)
        if result <= 0:
            game_over(0)
        else:        
            finale(player)
        
# Chapter Two Function
    def chapter_two(player):
        print("After dispatching the wolf, you quickly examine the corpse.")
        print("It may have been one of the bandits, or an unfortunate bystander.")
        print("You decide to come back later as you are losing time for the children.")
        print("Quickly picking up the trail, you follow it to the mouth of a cave. Bizarrely, you can see light deeper into the cave.")
        print("Going into the cave, you can hear an argument deeper into the cave. Maybe something is delaying the bandits.")
        print("As you get closer to the heated argument, the cave sharply turns; and you are immediately confronted with a Goblin.")
        result = combat(player, Goblin)
        if result <= 0:
            game_over(0)
        else:
            chapter_three(player)
        
# Chapter One Function
# ChatGPT aid on April 28, 2025 to debug. https://chatgpt.com/share/68101902-f920-8001-b3ba-40e50d228c42
    def chapter_one(player):
        print("As you arrive on the scene, you see a large heavy cart on its side.")
        print("One of the animals pulling the cart is also on its side.")
        print("Just beyond the overturned cart you see, on the edge of the road, a woman tending to an injured man.")
        print('She becomes aware of your approach: "Please help me! My husband is unconscious, but bandits kidnapped my children!"')
        print("She points into the forest at an easy-to-follow trail. The bandits apparently favor speed over stealth now.")    
        
        answer = input("Choose to help the woman treat her husband, chase the bandits, or ignore. (Help/Chase/Ignore): ")
        
        if answer.lower() == "help":
            print('She looks at you conflicted: "My husband will be okay, but I am unable to get my children back from the bandits. Please go after them."')
            ansr = input("What will you do? (Chase/Ignore): ")
            
            if ansr.lower() == "chase":
                print("You follow the trail...")
                print("After around 100 meters, you find a lone wolf eating a corpse. Before you can get away unnoticed, it growls and lunges at you.")
                result = combat(player, Wolf)
                if result <= 0:
                    game_over(0)
                else:
                    chapter_two(player)
            else:
                game_over(1)

        elif answer.lower() == "chase":
            print("You follow the trail...")
            print("After around 100 meters, you find a lone wolf eating a corpse. Before you can get away unnoticed, it growls and lunges at you.")
            result = combat(player, Wolf)
            if result <= 0:
                game_over(0)
            else:
                chapter_two(player)

        else:
            game_over(1)

    
# Story, Prolog
    def prolog(player):
        print()
        print("You begin your adventure travelling a quiet forest path towards the port city, Cragspire.")
        print("Expecting to make it to Cragspire before nightfall; you imagine the food and revlery of the port city.")
        print("You unexpectly hear a loud noise; followed quickly by a scream and bleating of draft animals.")
        ansr = input("Do you rush towards the disturbance, or find a way around to continue?(Rush/Ignore)")
        if ansr.lower() == "rush":
              chapter_one(player)
        else:
            game_over(1)

    prolog(player)
## Main Game function

def start_game():
    opt = 'y'
    while (opt == 'y'):
        print("Menu")
        print("1. Play Game")
        print("2. Exit")
        value = int(input("Please select option 1 or 2: "))
        if value == 1:
            print("Play Game.")
            player = char_create()
            story(player)


            
        elif value == 2:
            print("Thank you for playing.")
            print("Goodbye")
            opt = 'n'
        else:
            print("Incorrect option, press any key to continue.")

start_game()
