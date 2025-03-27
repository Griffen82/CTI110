# Michael Urbi
# March 25, 2025
# P4HW1
# Edit a previous program to incorperate loops.

#Ask user how many grades will be entered into program

nmbr = int(input("How many scores do you want to enter? "))

grades = []

# Ask user for each grade

for i in range (1, nmbr+1):
    score = float(input(f'Enter score #{i}: '))

# Validate the entered grade

    while score < 0 or  score > 100:
        print("Invalid Score entered!!!!")
        print("Score should be between 0 and 100.")
        print()
        score = float(input(f'Enter score #{i} again: '))

# If grade is valid, add to list

    grades.insert(i-1, score)

# Print lowest grade, modified list with lowest removed, average from new list
# and letter grade

print()
print("-"*15, "Results", "-"*15)

print(f"{"Lowest Grade":<14} : {min(grades)}")

grades.remove(min(grades))

print(f"{"Modified List":<14} : {grades}")

ave = (sum(grades)/len(grades))

print(f"{"Scores Average":<14} : {ave:.2f}")

if ave >= 90:
    print(f"{"Grade ":<14} : A")
elif ave >= 80:
    print(f"{"Grade ":<14} : B")
elif ave >= 70:
    print(f"{"Grade ":<14} : C")
elif ave >= 60:
    print(f"{"Grade ":<14} : D")
elif ave < 60:
    print(f"{"Grade ":<14} : F")

print("-"*40)
