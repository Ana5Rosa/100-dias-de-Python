print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input("Pirate, do you want to go left or right? Choose wisely!\n")
choice = choice.lower()

if choice == "left":
    choice = input("Did you hear anything? Do you want to swim or wait?\n")
    choice = choice.lower()

    if choice == "wait":
        choice = input("The spirit of the pirate DieChoosing appears to you and promises you safe passage to the treasure. But you need to choose one of three ports. Do you choose the blue, red or yellow door?\n")
        choice = choice.lower()
        if choice == "yellow":
            print("You enter the yellow door and you are back on your ship, docked in your city, safe and with a barrel full of gold at your feet.\nYou won!")
        elif choice == "blue":
            print("You enter the blue door and find yourself surrounded by wild beasts.\nYou didn't get the treasure, but the beasts liked you. Now you are one of them.\nYou almost won!")
        elif choice == "red":
            print("You go through the red door and you're back on your ship, but it's all holed up. Good luck emptying it.\nGame Over!")
        else: 
            print("The DieChoosing pirate spirit didn't understand what you said and decided you're too dumb to live free. Now you are his slave.")
    else:
        print("You fell under the siren's spell.")
        print("Your body now lies at the bottom of the sea")
        print("Game Over!")
else:
    print("Your ship was devoured by a Kraken")
    print("You are now the babysitter of the Kraken puppies")
    print("Game Over!")
