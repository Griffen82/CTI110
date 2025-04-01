# Michael Urbi
# March 27, 2025
# P4HW2
# Add onto P3HW2 to enter multiple employees and return a total payout

word = '"Done"'

# Input first employee
name = input(f"Enter employee's name or {word} to terminate: ")
employee = []
co_ovtp = []
co_rpay = []
co_gross = []

while name != "Done":
    employee.append(name)
    # Enter how many hours and the employee's payrate
    hours = float(input('How many hours did '+name+' work?: '))
    pay = float(input("What is "+name+"'s pay rate?: "))

    print()
    print(f'{'Employee name: ':<10} {name}')
    print()
    # Calculate if employee has overtime
    if hours>40:
        ovtm = hours - 40
        hrs = 40
    else:
        ovtm = 0
        hrs = hours
    # Calculate overtime pay, if any, regular pay, and gross pay
    ovtp = ovtm * (pay * 1.5)
    opay = str(f'{ovtp:.2f}')
    regpay = pay * hrs
    rpay = str(f'{regpay:.2f}')
    gross = ovtp + regpay
    gpay = str(f'{gross:.2f}')
    # Add pay rates to company total
    co_ovtp.append(ovtp)
    co_rpay.append(regpay)
    co_gross.append(gross)
    # Display employee's hours and pay
    print(f'{'Hours Worked':<15} {'Pay Rate':<10} {'Overtime':<10} {'Overtime Pay':<15} {'RegHour Pay':<15} {'Gross Pay'}')
    print('-'*80)
    print(f'{hours:<15} {pay:<10} {ovtm:<10} {'$'+opay:<15} {'$'+rpay:<15} {'$'+gpay}')
    # Ask for new employee or if Done
    name = input(f"Enter employee's name or {word} to terminate: ")

# When done, display total employees entered; total overtime, regular pay, and gross pay paid out
print()
print(f'Total number of employees entered: {len(employee)}')
print(f'Total amount paid for overtime: ${sum(co_ovtp)}')
print(f'Total amount paid for regular hours: ${sum(co_rpay)}')
print(f'Total amount paid in gross: ${sum(co_gross)}')
