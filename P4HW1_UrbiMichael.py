# Michael Urbi
# March 25, 2025
# P4HW1
# Edit a previous program to incorperate loops.

nmbr = int(input("How many scores do you want to enter? "))

for i in range (1, nmbr+1):
    score = float(input(f'Enter score #{i}: '))
    while score < 0 or  score > 100:
        print("Invalid Score entered!!!!")
        print("Score should be between 0 and 100.")
        print()
        score = float(input(f'Enter score #{i} again: '))
    grades = []
    grades.insert(i-1, score)
    print(grades)
