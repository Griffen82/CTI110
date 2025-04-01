# Michael Urbi
# March 27, 2025
# P4HW2
# Add onto P3HW2 to enter multiple employees and return a total payout

name = input("Enter employee's name or ""Done"" to terminate: ")
employee = []
co_ovtp = []
co_rpay = []
co_gross = []

while name != "Done":
    employee.append(name)
    
    hours = float(input('How many hours did '+name+' work?: '))
    pay = float(input("What is "+name+"'s pay rate?: "))

    print()
    print(f'{'Employee name: ':<10} {name}')
    print()

    if hours>40:
        ovtm = hours - 40
        hrs = 40
    else:
        ovtm = 0
        hrs = hours
    
    ovtp = ovtm * (pay * 1.5)
    opay = str(f'{ovtp:.2f}')
    regpay = pay * hrs
    rpay = str(f'{regpay:.2f}')
    gross = ovtp + regpay
    gpay = str(f'{gross:.2f}')

    co_ovtp.append(ovtp)
    co_rpay.append(regpay)
    co_gross.append(gross)
    
    print(f'{'Hours Worked':<15} {'Pay Rate':<10} {'Overtime':<10} {'Overtime Pay':<15} {'RegHour Pay':<15} {'Gross Pay'}')
    print('-'*80)
    print(f'{hours:<15} {pay:<10} {ovtm:<10} {'$'+opay:<15} {'$'+rpay:<15} {'$'+gpay}')

    name = input("Enter employee's name or ""Done"" to terminate: ")


print()
print(f'Total number of employees entered: {len(employee)}')
print(f'Total amount paid for overtime: ${sum(co_ovtp)}')
print(f'Total amount paid for regular hours: ${sum(co_rpay)}')
print(f'Total amount paid in gross: ${sum(co_gross)}')
