# this will take users input and add into the variable 'age' 
age = int(input("Enter your age:"))

# variable 'age' will then be put into correct category based on value, using IF statement this will display both A and B over the age of 18
if age >= 18:
    print("You are in category A")
if age >= 16:
    print("You are in category B")
else:
    print("You are in category C")