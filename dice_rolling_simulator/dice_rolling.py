# Import random
# Define a function to roll the dice
# Create a dictionary that will have the drawings of the dice

import random

def roll_dice():

  dice_drawing = {
    1: (
      "|------------|",
      "|            |",
      "|      1     |",
      "|     🟢     |",
      "|            |",
      "|____________|",
    ),
    2: (
      "|------------|",
      "|            |",
      "|  🟢        |",
      "|      2     |",
      "|        🟢  |",
      "|____________|",
    ),
    3: (
      "|------------|",
      "|      3     |",
      "|  🟢        |",
      "|     🟢     |",
      "|        🟢  |",
      "|____________|",
    ),
    4: (
      "|------------|",
      "|            |",
      "|  🟢    🟢  |",
      "|      4     |",
      "|  🟢    🟢  |",
      "|____________|",
    ),
    5: (
      "|------------|",
      "|      5     |",
      "|  🟢    🟢  |",
      "|     🟢     |",
      "|  🟢    🟢  |",
      "|____________|",
    ),
    6: (
      "|------------|",
      "|      6     |",
      "|  🟢    🟢  |",
      "|  🟢    🟢  |",
      "|  🟢    🟢  |",
      "|____________|",
    ),
  }

  roll = input("Roll the dice? (Yes/No): ")

  while roll.lower() == "Yes".lower():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"Dice rolled: {dice1} and {dice2}")
    print("\n".join(dice_drawing[dice1]))
    print("\n".join(dice_drawing[dice2]))
    roll = input("Roll again? (Yes/No): ")

roll_dice()