def big_line():
    print('-=' * 20)

big_line()
print('IF STATEMENTS WITH FORMULA 1'.center(40))
big_line()

print('ENTERING DRIVER DATA'.center(40))
driver = input('\nEnter the name of a driver: ')
country = input('Enter his country: ')
age = int(input('Enter his age: '))
wins = int(input('Enter his wins: '))
wdc = int(input('Enter his World Titles: '))
monaco = input('Won in Monaco? (Y/N): ').upper()

big_line()
print(f'{driver} - {country} - {age} years - STATS'.upper().center(40))
if wins > 20:
    print(f'\n{driver} is a winning machine! {wins} wins!')
else:
    print(f'\n{driver} is not a winning machine... {wins} wins only')
if wdc > 0:
    print(f'{driver} is a World Champion! {wdc} titles!')
    if wdc >= 3:
        print(f'{driver} is a LEGEND! {wdc} titles!')
else:
    print(f'{driver} never won a WDC')
if monaco == 'Y':
    print(f'Winning in Monaco is a unique experience, and {driver} did it!')
elif monaco == 'N':
    print(f'{driver} never won a race in Monaco'.lower())
else:
    print('Please, enter a valid data!...')
big_line()


