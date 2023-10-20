#num variable to store user input
num = int(input("Enter a number: "))

#inititalise factorial variable at 1
factorial = 1  

#while input is more than 0, times by factorial and minus 1
while num > 0:
    factorial *= num
    num -= 1
    print(f"{num}")

#output
print(f"Factorial for {num} is {factorial}")
