# Set min and max values
min_value = 1
max_value = 100

# Initialize attempts counter
attempts = 0

while attempts < 3:
    user_input= input(f"Enter a number between {min_value} and {max_value}: ")

    if user_input.isdigit():
        user_input = int(user_input)
        if min_value <= user_input <= max_value:
            print(f"User entered: {user_input}")
            break
        else:
            print("Value out of range. Try again.")
    else:
        print("Please enter a number only")
    
    # Add an attempt
    attempts += 1

if attempts == 3:
    print("Closing program...")
