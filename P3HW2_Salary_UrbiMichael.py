# Michael Urbi
# March 13, 2025
# P3HW2
# Program asking for employee information and outputting hours and pay

emp = input("Enter employee's name: ")
hours = float(input('Enter number of hours worked: '))
pay = float(input("Enter emplyee's pay rate: "))

print('-'*40)
print(f'{'Employee name: ':<20} {emp}')
print()

if hours>40:
    ovtm = hours - 40
    hrs = 40
else:
    ovtm = 0
    hrs = hours
    
ovtp = ovtm * (pay * 1.5)
regpay = pay * hrs
gross = ovtp + regpay

print(f'{'Hours Worked':<10} {'Pay Rate':>10} {'Overtime':>10} {'Overtime Pay':>15} {'RegHour Pay':>15} {'Gross Pay':>12}')
print('-'*80)
print(f'{hours:<10} {pay:>10} {ovtm:>10} {ovtp:>15.2f} {regpay:>15.2f} {gross:>12.2f}')
