# set up a dictionary with two key/value pairs 
shakes = {
    1: {'flavor': 'Chocolate', 'price': 5},
    2: {'flavor': 'Strawberry', 'price': 4},
    3: {'flavor': 'Banana', 'price': 5}
}

#variables
budget = 10
counter = 0

#iteration 
while budget > 0:
    print(f"---------------------------------------------------------------")
    print(f"[1] Flavor: {shakes[1]['flavor']}, Price: ${shakes[1]['price']}")
    print(f"[2] Flavor: {shakes[2]['flavor']}, Price: ${shakes[2]['price']}")
    print(f"[3] Flavor: {shakes[3]['flavor']}, Price: ${shakes[3]['price']}")
    print(f"Your budget is: ${budget}")
    print(f"---------------------------------------------------------------")
    print(F"press [Q] to quit")
    print(f"---------------------------------------------------------------")
    choice = input("What can I fix you? ")
    print(f"---------------------------------------------------------------")
    
    choice = int(choice)
    if choice == 1:
        if budget >= 0:
            budget -= 5
            counter += 1
            print(f"You have had {counter} drink{'s' if counter > 1 else ''}.")
            print(f"Your budget is: ${budget}")
        else:
            print("Oh dear, you do not have enough money. You have been thrown out.")
            break
    elif choice == 2:
        budget -= 4 
        counter += 1
        print('you have had', counter, 'drinks')
        print (f"your budget is: $", budget)
    elif choice == 3:
        budget -= 5
        counter += 1
        print('you have had', counter, 'drinks')
        print (f"your budget is: $", budget)
    elif choice == "q":
        break
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')
    


