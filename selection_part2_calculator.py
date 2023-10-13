print('''Welcome to the lab2 calculator.py
please select from the menu below
1. Add +
2. Subtract -
3. Multiply *
4. Divide /
5. Square s 
''')

calculation = input('please select your calculation choice (1-5): ')

print('you have selected', calculation)

number_one = float(input('please enter a number: '))
number_two = float(input('please enter a second number: '))

if calculation == '1':
    print(number_one + number_two)
elif calculation == '2':
    print(number_one - number_two)
elif calculation == '3':
    print(number_one * number_two)
elif calculation == '4':
        print(number_one / number_two)
elif calculation == '5':
    print(number_one ** 2)
else:
    print("Invalid choice. Please select a number between 1 and 5.")
