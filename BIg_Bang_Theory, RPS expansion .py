import random

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
spock = """""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⢸⣿⣷⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⣿⣿⡆⠀⠀⠀⠀⣼⣿⣿⠀⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⢹⣿⣧⠀⠀⠀⣸⣿⣿⠃⣰⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠘⣿⣿⡄⠀⢀⣿⣿⡏⢠⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡀⢻⣿⣧⠀⣸⣿⡟⢀⣾⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⣸⣿⣿⣶⣿⣿⠁⣼⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣷⣦⣀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀"""""

lizard = """""
⠀                       )/_
             _.--..---"-,--c_
        \L..'           ._O__)_
,-.     _.+  _  \..--( /           
  `\.-''__.-' \ (     \_      
    `'''       `\__   /
                ')⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""""

Game = [rock, paper, scissors, spock, lizard]

print(" Welcome to Rock, Paper, Scissors, Lizard, Spock\n "
      " 'Big Bang Theory expansion'")

players_choice = int(input("Type '0' for Rock\n"
                       "Type '1' for Paper\n"
                       "Type '2' for Scissors\n"
                       "Type '3' for Spock\n"
                       "Type '4' for Lizard\n"
                       "What do you choose? "))

print(Game[players_choice])

computer_choice = random.randint(0,4)

print("Computer chose: ")
print(Game[computer_choice])

if (computer_choice == players_choice or players_choice == computer_choice):
    print("You tie")
elif(players_choice == 2 and computer_choice == 1):
    print("Scissors cuts paper\n"
          "You Win")
elif(players_choice == 1 and computer_choice == 0):
    print("Paper cover Rock\n"
          "You Win")
elif(players_choice == 0 and computer_choice == 4):
    print("Rock crushes lizard\n"
          "You Win")
elif(players_choice == 4 and computer_choice == 3):
    print("Lizard poisons Spock\n"
          "You Win")
elif(players_choice == 3 and computer_choice == 2):
    print("Spock smashes scissors\n"
          "You Win")
elif(players_choice == 2 and computer_choice == 4):
    print("Scissors decapitates lizard\n"
          "You Win")
elif(players_choice == 4 and computer_choice == 1):
    print("Lizard eats paper\n"
          "You Win")
elif(players_choice == 1 and computer_choice == 3):
    print("Paper disproves Spock\n"
          "You Win")
elif (players_choice == 3 and computer_choice == 0):
    print("Spock vaporizes rock\n"
          "You Win")
elif (players_choice == 0 and computer_choice == 2):
    print("Rock cruches scissors\n"
          "You Win")
else:
    print("You Lose")





