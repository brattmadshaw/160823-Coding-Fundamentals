### Asset Tracking System v1


### Creating a login message
print("""
Welcome to the ISMSAsset Tracking System v1.
      
    Warning, Unauthorised Acess is Prohibited with severse penalties. By logging into the system you are legally responsible.

Please select from the option below:
1. Login
2. Quit
      
""")

### Login loop

while True:
    login_choice = input("Please select from the options 1 or 2: ")

    if login_choice == "1":
        print("You are now logging into the system...")
        break 

    elif login_choice == "2":
        print("Quitting...")
        quit()

    else:
        print("Invalid choice selection. ")

### authentication loop

while True:
    print("Please enter your login information")
    username = input("Username: ")
    password = input("Password: ")

    if username == "mbradshaw2112" and password == "password112":
        print("Valid credentials")
        break
    else:
        print("Invalid crdentials")

while True:
    print("Welcome to the ISMS Dashboard")
    break
