# Michael Urbi
# March 27, 2025
# P4HW2
# Add onto P3HW2 to enter multiple employees and return a total payout

name = input("Enter employee's name or ""Done"" to terminate: ")
done = 0
employee = []

while name != done:
    employee.append(name)
    print(employee)
    name = input("Enter employee's name or ""Done"" to terminate: ")
else:
    print(employee)
