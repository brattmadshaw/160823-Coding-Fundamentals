# challenge - make a function that does addittion of 2 numbers that we pass as arguments

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 ** num2

def divide_numbers(num1, num2):
    return num1 / num2

print(add_numbers(5,2))
print(subtract_numbers(4,3))
print(multiply_numbers(3,4))
print(divide_numbers(2,5))

def fruit_list(*fruits):
    print("the fruits are: ")
    for fruit in fruits:
        print(fruit)

fruit_list("apple", "orange", "pear")

def numbers_list(*numbers):
    for i in numbers:
        print(i)

numbers_list(1,2,3,4,5,6,7)

#keyword arrguements kwargs 
#send args as key:value pairs - therefore the **** does not matter
#we define the alue when we pass the arguments.

def fruit_list(fruit1, fruit2, fruit3):
    print(f"fav = {fruit1}")
    print(f"fav2 = {fruit2}")
    print(f"fav3 = {fruit3}")

fruit_list(fruit1 = "apple", fruit3 = "pear", fruit2 = "orange")