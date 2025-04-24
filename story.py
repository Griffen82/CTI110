def story():
    
# Enemy dictionaries
    Wolf = {
        "Name":"Wolf",
        "Str":"4",
        "Agi":"7",
        "Vit":"4",
        "Int":"2",
        "Luck":"3"}
    Bandit = {
        "Name":"Bandit",
        "Str":"4",
        "Agi":"5",
        "Vit":"3",
        "Int":"3",
        "Luck":"3"}
    Goblin = {
        "Name":"Goblin",
        "Str":"3",
        "Agi":"4",
        "Vit":"2",
        "Int":"4",
        "Luck":"5"}
    Boss = {
        "Name":"Boss",
        "Str":"5",
        "Agi":"6",
        "Vit":"6",
        "Int":"5",
        "Luck":"4"}
# Story, Act 1
    print("Introduction...")
    print("Conflict...")
    answer = input("Choose to help or ignore. (Help/Ignore)")
    if answer == "help":
        print("Follow trail...")
        print("Come across a lone wolf...")
#        combat(player, wolf)
    else:
        print("You ignore the conflict. Your next few days are peaceful before dark omens arise.")
    print("End Act 1")
story()
