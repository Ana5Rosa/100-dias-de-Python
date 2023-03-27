import random

rock_Player = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
rock_Computer = '''
  _______
 (____   '---
(_____)
(_____)
 (____)
  (___)__.---

'''

paper_Player = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) 
'''

paper_Computer = '''
       _______   
  ____(____   '---    
 (______
(_______
 (_______
   (__________.---
'''

scissors_Player = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

scissors_Computer = '''
       _______
  ____(____   '---   
 (______
(__________
      (____)
       (___)__.---
'''

moves_Computer = [rock_Computer, paper_Computer, scissors_Computer]
moves_Player = [rock_Player, paper_Player, scissors_Player]

move = int(input("Enter 0 for rock, 1 for paper and 2 for scissors:\n"))
if move >= 0 and move <= 2:
    print(moves_Player[move])
    computer_move = random.randint(0, 2)
    print(moves_Computer[computer_move])
    if move == computer_move:
        print("A tie")
    elif (move == 0 and computer_move == 1) or (move == 1 and computer_move == 2) or (move == 2 and computer_move == 0):
        print("Computer wins!!\n GAME OVER")
    else:
        print("You wins!!")
else:
    print("Response different than expected. Restart the game.")

