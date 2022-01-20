import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

bossHealth = 10

dice = Dice(6)
roll1 = dice.roll()
roll2 = dice.roll()

print(f'Your first roll is: {roll1}')
print(f'Your second roll is: {roll2}')

if roll1 + roll2 > bossHealth:
    print('Congratulations, you have defeated The Boss! You win!')
else:
    print('The Boss has defeated you! GAME OVER')

