# Michael Urbi
# April 17, 2025
# P5HW
# Creating a short adventure game using what we have learned thus far

import random

coin = random. randint(1, 2)
d4 = random.randint(1,4)
d6 = random.randint(1, 6)
d8 = random.randint(1, 8)
d10 = random.randint(1, 10)
d100 = random.randint(1, 100)

char = {}
    
#Gear Dictionaries
weapon = 0
skill = 0
armor = {
    "Defense":10}
cloak = {
    "Defense":8}
robe = {
    "Defense":6}
dagger = {
    "Attack":d4}
spear = {
    "Attack":d8}
staff = {
    "Attack":d4}
sword = {
    "Attack":d6}
gear = {
    "Armor":armor,
    "Weapon":weapon,
    "Skill":skill}

def char_create():
# Name your character
    name = input("Please enter your name: ")
# Choose a lineage
    print("1. Urchin; Str:5, Agi:6, Vit:4, Int:3, Luck:6")
    print("2. Tradesman; Str:4, Agi:4, Vit:6, Int:6, Luck:4")
    print("3. Noble; Str:3, Agi:5, Vit:5, Int:7, Luck:4")
    lineage = int(input("Please select a Lineage:"))
    while lineage < 1 or lineage >= 4:
        print("Invalid selection, please select again.")
        lineage = int(input("Please select a Lineage:"))
    else:
        if lineage == 1:
            char = {
                "Name":name,
                "Str":"5",
                "Agi":"6",
                "Vit":"4",
                "Int":"3",
                "Luck":"6"}
        elif lineage == 2:
            char = {
                "Name":name,
                "Str":"4",
                "Agi":"4",
                "Vit":"6",
                "Int":"6",
                "Luck":"4"}
        elif lineage == 3:
            char = {
                "Name":name,
                "Str":"3",
                "Agi":"5",
                "Vit":"5",
                "Int":"7",
                "Luck":"4"}
# Add a vocation and vocational skill
    print("1. Champion: +2 Str. Start with armor and sword.")
    print("2. Thief: +2 Agi. Start with cloak and dagger.")
    print("3. Guard: +2 Vit. Start with armor and spear.")
    print("4. Mage: +2 Int. Start with robe and staff.")
    print("5. Con: +2 Luck. Start with robe and dagger.")
    voc = int(input("Please select a vocation: "))
    while voc < 1 or voc >= 6:
        print("Invalid selection, please select again.")
        voc = int(input("Please select a vocation: "))
    else:
        if voc == 1:
            iStr = int(char.get("Str"))
            nStr = iStr + 2
            char.update({"Str":nStr})
            gear.update({"Armor":"armor"})
            gear.update({"Weapon":"sword"})
            print("1. Battlecry: Heal d10 damage and add d6 damage to next attack.")
            print("2. Heavy Strike: Add double Str to next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill":'Battlecry()'})
                elif vocskl == 2:
                    gear.update({"Skill":'Heavy_Strike'})
        elif voc == 2:
            iAgi = int(char.get("Agi"))
            nAgi = iAgi + 2
            char.update({"Agi":nAgi})
            gear.update({"Armor":"cloak"})
            gear.update({"Weapon":"dagger"})
            print("1. Vital Strike: % chance to deal lethal damage.")
            print("2. Shadows: % chance to avoid the next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": 'Vital_Strike()'})
                elif vocskl == 2:
                    gear.update({"Skill": 'Shadows()'})
        elif voc == 3:
            iVit = int(char.get("Vit"))
            nVit = iVit + 2
            char.update({"Vit":nVit})
            gear.update({"Armor":"armor"})
            gear.update({"Weapon":"spear"})
            print("1. Lunge: Add your Vit stat to damage.")
            print("2. Parry: % chance to avoid the next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": 'Lunge'})
                elif vocskl == 2:
                    gear.update({"Skill": 'Parry()'})
        elif voc == 4:
            iInt = int(char.get("Int"))
            nInt = iInt + 2
            char.update({"Int":nInt})
            gear.update({"Armor":"robe"})
            gear.update({"Weapon":"staff"})
            print("1. Firebolt: Attack deals 3x Int damage.")
            print("2. Ice Wall: % chance to avoid the next attack.")
            vocskl = int(input("Please select a vocational skill (1 or 2): "))
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": 'Firebolt'})
                elif vocskl == 2:
                    gear.update({"Skill": 'Ice_Wall()'})
        elif voc == 5:
            iLuck = int(char.get("Luck"))
            nLuck = iLuck + 2
            char.update({"Luck":nLuck})
            gear.update({"Armor":"robe"})
            gear.update({"Weapon":"dagger"})
            print("1. Confusion: % chance enemy hurts themself.")
            print("2. Beginners Luck: % chance attack deals triple damage.")
            vocskl = input("Please select a vocational skill (1 or 2): ")
            while vocskl < 1 or vocskl >= 3:
                print("Invalid selection, please select again.")
                vocskl = int(input("Please select a vocational skill (1 or 2): "))
            else:
                if vocskl == 1:
                    gear.update({"Skill": 'Confusion()'})
                elif vocskl == 2:
                    gear.update({"Skill": 'Beginners_Luck()'})
    print(char)
    print(gear)
    print("Thank you for creating your character. Let us begin...")

# Skill Dictionaries or Equations

##def Battlecry():
##    HP = curHP +d10
##    Attack = sword + d6
##Heavy_Strike = 2 * char[Str]
##def Vital_Strike():
##    gamble = d100
##    if gamble <= 5 * char[Agi]:
##        damage = 9999
##    else:
##        damage = dagger
##def Shadows():
##    gamble = d100
##    if gamble <= 5 * char[Agi]:
##        Defense = 9999
##    else:
##        Defense = cloak
##Lunge = spear + char[Vit]
##def Parry():
##    gamble = d100
##    if gamble <= 5 * char[Vit]:
##        Defense = 9999
##    else:
##        Defense = armor
##Firebolt = 3 * char[Int]
##def Ice_Wall():
##    gamble = d100
##    if gamble <= 5 * char[Int]:
##        Defense = 9999
##    else:
##        Defense = robe
##def Confusion():
##    gamble = d100
##    if gamble <= 5 * char[Luck]:
##        ecHP = ecHP - eAtt
##        eAct = 0
##    else:
##        eAct = 1
##def Beginners_Luck():
##    gamble = d100
##    if gamble <= 5 * char[Luck]:
##        damage = 3 * dagger
##    else:
##        damage = dagger

def start_game():
    opt = 'y'
    while (opt == 'y'):
        print("Menu")
        print("1. Play Game")
        print("2. Exit")
        value = int(input("Please select option 1 or 2: "))
        if value == 1:
            print("Play Game.")
            char_create()
        elif value == 2:
            print("Thank you for playing.")
            print("Goodbye")
            opt = 'n'
        else:
            print("Incorrect option, press any key to continue.")
start_game()
