rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type (0) for Rock, (1) for Paper or (2) for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(computer_choice)

if user_choice == computer_choice:
    print(f"Your choice is: {options[user_choice]}")
    print(f"Computer's choice is: {options[computer_choice]}")
    print("Draw!")
elif user_choice == 0 and computer_choice == 2:
    print(f"Your choice is: {options[user_choice]}")
    print(f"Computer's choice is {options[computer_choice]}")
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print(f"Your choice is: {options[user_choice]}")
    print(f"Computer's choice is {options[computer_choice]}")
    print("You Lost!")
elif user_choice > computer_choice:
    print(f"Your choice is: {options[user_choice]}")
    print(f"Computer's choice is {options[computer_choice]}")
    print("You Win!")
elif computer_choice > user_choice:
    print(f"Your choice is: {options[user_choice]}")
    print(f"Computer's choice is {options[computer_choice]}")
    print("You Lost!")