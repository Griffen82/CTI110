#Michael Urbi
#Febuary 27, 2025
#P2HW2
#Program showing comprehension of list elements

#Ask user to input grades from Modules 1-6
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

#Store the information in a list
gradeslist = [mod1, mod2, mod3, mod4, mod5, mod6]
#print(gradelist)

#Display common inquiries of grades and sum of grades
print()
print("-"*12, "Results", "-"*12)

print(f"{"Lowest Grade:":<20} {min(gradeslist)}")


print(f"{"Highest Grade:":<20} {max(gradeslist)}")


print(f"{"Sum of Grades:":<20} {sum(gradeslist)}")


print(f"{"Average:":<20} {sum(gradeslist)/len(gradeslist):.2f}")
print("-"*40)
