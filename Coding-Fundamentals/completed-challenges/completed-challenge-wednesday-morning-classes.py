import random

options = ["Rock", "Paper", "Scissors"]

while True: 
    num_of_rounds = 1
    total_rounds = 3
    user_wins = 0
    computer_wins = 0

    while num_of_rounds <= total_rounds:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        user_choice_number = input("Enter the number of your choice: ")

        if user_choice_number.isdigit() and 1 <= int(user_choice_number) <= 3:
            user_choice = options[int(user_choice_number) - 1]
            computer_choice = random.choice(options)

            print(f"\nYou chose {user_choice}. Computer chose {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (
                (user_choice == "Rock" and computer_choice == "Scissors") or
                (user_choice == "Paper" and computer_choice == "Rock") or
                (user_choice == "Scissors" and computer_choice == "Paper")
            ):
                print("You win this round!")
                user_wins += 1
            else:
                print("Computer wins this round!")
                computer_wins += 1

            print(f"\nCurrent Scores - Computer: {computer_wins} User: {user_wins}\n")

            num_of_rounds += 1
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nGame Over! Final Scores:")
    print(f"Computer: {computer_wins} wins")
    print(f"You: {user_wins} wins")

    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break