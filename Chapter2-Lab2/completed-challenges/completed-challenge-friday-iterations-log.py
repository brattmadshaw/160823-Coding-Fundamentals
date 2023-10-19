#version 1
count_the_inputs = 0
list_of_names = []

while count_the_inputs < 7:
    input_name = input("Enter a name: ")
    list_of_names.append(input_name)
    count_the_inputs += 1

for input_name in list_of_names:
    print(input_name, "is awesome")

#version 2
counter = 0 
while counter < 5: 
    name = input ("enter a name")
    print(name + " is awesome")
    counter += 1

#version 3
[print(f"{name} is awesome!") for name in [input("enter a name: ") for x in range(5)]]