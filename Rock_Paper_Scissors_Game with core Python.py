#Rock paper scissors game
import random

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors)in lowercase letters: ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        user_input = input("Invalid choice. Enter again (rock, paper, scissors)in lowercase letters: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


print("Welcome to Rock, Paper, Scissors!")
def play_game():
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    result = determine_winner(user, computer)
    print(result)
    playagain=input("Do you want to play again?(yes or no):").lower()
    if playagain=="yes":
        play_game()
    else:
        print("Thanks for playing")

if __name__ == "__main__":
    play_game()


