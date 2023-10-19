### Part 1

# this will take users input and add into the variable 'age' 
age = int(input("Enter your age:"))

# variable 'age' will then be put into correct category based on value, using IF statement this will display both A and B over the age of 18
if age >= 18:
    print("You are in category A")
elif age >= 16:
    print("You are in category B")
else:
    print("You are in category C")


### Part 2

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

number_one = float(input('please enter the first number: '))
number_two = float(input('please enter the second number: '))

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
    print("Invalid choice. Please select a calculation between 1 and 5.")
