# this will take users input and add into the variable 'age' 
age = int(input("Enter your age:"))

# variable 'age' will then be put into correct category based on value, using ELIF statement this will now display the correct value in comparison to IF statement.
if age >= 18:
    print("You are in category A")
elif age >= 16:
    print("You are in category B")
else:
    print("You are in category C")
