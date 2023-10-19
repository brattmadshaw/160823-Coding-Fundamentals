user_input = input("How many modules have you completed: ")
print(f"user has entered: {user_input}")
print("\033[93m[00] Debugging||: The data type of user_input is:", type(user_input))

user_input = int(user_input)
print(f"[00] Debugging||: Converting input '{user_input}' to data type:", type(user_input))

init_int = 0
print(f"[00] Debugging||: Initialised a variable named init_int '{init_int}' data type:", type(init_int))

score_list = []
print(f"[00] Debugging||: Initialised a list named score_list\n[0]Debugging: Existing Value: '{score_list}' data type:", type(score_list))

while init_int < user_input:
    print(f"[0]Debugging||: Running while loop while user_input '{user_input}' is greater than '{init_int}'")

    module_name = input(f"\033[0mModule {init_int + 1}\nPlease enter the name of the module: ")
    print(f"\033[93m[0]Debugging||: module_name '{module_name[0].upper()}{module_name[1:]}' added to list score_list")
    module_input = input(f"\033[0mPlease enter your grade: ")
    print(f"\033[93m[0]Debugging||: module_score '{module_input}' added to list score_list")

    # Add the module information to the list
    score_list.append((module_name, module_input))
    print (f"\033[93m[0]Debugging||: Updated list value: {score_list}")
    
    init_int += 1

print(f"\033[0mtotal choices: {score_list}")