# Michael Urbi
# March 13, 2025
# P3HW2
# Program asking for employee information and outputting hours and pay

# Ask user to input employee information; name, hours, and payrate.
# Calculate if the employee has earned overtime from the information given.
# Calculate the overtime pay, if any, regular pay, and gross pay for the employee.
# Display Employee name, hours worked, pay rate, overtime, overtime pay, regular hours, and gross pay.

emp = input("Enter employee's name: ")
hours = float(input('Enter number of hours worked: '))
pay = float(input("Enter emplyee's pay rate: "))

print('-'*40)
print(f'{'Employee name: ':<10} {emp}')
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

print(f'{'Hours Worked':<15} {'Pay Rate':<10} {'Overtime':<10} {'Overtime Pay':<15} {'RegHour Pay':<15} {'Gross Pay'}')
print('-'*80)
print(f'{hours:<15} {pay:<10} {ovtm:<10} {'$'+opay:<15} {'$'+rpay:<15} {'$'+gpay}')
