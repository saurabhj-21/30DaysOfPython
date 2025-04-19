'''
This is a simple game of Snake, Water, Gun.
The rules are as follows:  
- You can choose between snake, water, or gun.
- The computer will randomly choose one of the three options.
- The winner is determined by the following rules:
  - Snake beats water
  - Water beats gun
  - Gun beats snake
- If both players choose the same option, it's a tie.


The game is played as follows:
- The player enters their choice (snake, water, or gun).
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (snake/water/gun): ")
dictionary = {
    "snake": 1,
    "water": -1,
    "gun": 0
}

reverseDictionary = {
    1: "snake",
    -1: "water",
    0: "gun"
}

you = dictionary[youstr]

print("You chose: ", youstr)
print("Computer chose: ", reverseDictionary[computer])

if (computer == -1 and you == 1):
    print("You Win!")

elif (computer == -1 and you == 0):
    print("You Lose!")

elif (computer == 1 and you == -1):
    print("You Lose!")

elif (computer == 1 and you == 0):
    print("You Win!")

elif (computer == 0 and you == -1):
    print("You Win!")

elif (computer == 0 and you == 1):
    print("You Lose!")

else:
    print("It's a Tie!")
