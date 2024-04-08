
# Generates heading ( eg: ---- Heading ----)

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


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

