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

direction = input('You\'re at a crossroad, where do you want to go? "left" or "right?"\n ').lower()
if direction == "left":
  water = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "swim" to swim across or type "wait" to wait for a boat.\n ').lower()
  if water == "wait":
    door = input("You arrived at the island unharmed. There is a house with 3 doors. One blue, one red and one yellow. Which colour do you choose?\n ").lower()
    if door == "red":
      print("Burned by fire. Game Over")
    elif door == "blue":
      print("Eaten by beasts. Game Over")
    elif door == "yellow":
      print("You Win!")
    else:
      print("Game Over")
  else:
    print("Attacked by trout. Game over")
else:
  print("Fall into a hole. Game Over.")
