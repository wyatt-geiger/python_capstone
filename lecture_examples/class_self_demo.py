class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa
    
    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

alex = Student('Alex', 'abcdef', '3.7')
print(alex.name)
print(alex.school_id)
print(alex.gpa)
print(alex)

sam = Student('Sam', 'qwerty', '2.6')
print(sam)

tom = Student('Tom', 'zorkle', '3.2')
print(tom.gpa)
print(tom)

print('-----')

# dice roll

import random # imports random numbers

class Dice:
    def __init__(self, sides): # you can also set sides=6, making it the default value if no other number is specified
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

dice = Dice(6) # 6 specifies the number of sides on the die
print(dice.roll())