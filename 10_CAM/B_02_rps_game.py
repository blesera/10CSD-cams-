import random

# Display instruction
def instructions():

    print('''
instructions go here.
-  code will ask the user for a choice between rock, paper and scissors.
- Once the user enters their choice, the code will randomly choose one of those options as the computer's turn. 
- The code then prints out the chosen option and the user's choice.
- Finally, it loops back to ask for another choice from the user.
    ''' )

# Main routine goes here

# Display instructions if required
want_instructions = input ("Press <enter> to read the instructions "
                           " or any key to continue ")

if want_instructions =="":
    instructions()

print("program continues")

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors):")

    print(f"Player: {player}")
    print(f"computer: {computer}")

  # compares user / computer choice and returns
  # result (win / lose / tie)
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("play again? :").lower() == "yes":
        running = False


    print("Thanks for playing!")


