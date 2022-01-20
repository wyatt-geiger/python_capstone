"""This program asks a user for their name and birth month. Using that information, the program prints out
a greeting, displays the length of the user's name, and checks if the user's birth month is the same as the
current month. If it is, the program displays a happy birthday message."""

import datetime # imports datetime object

name = input('What is your name? ')

month = input('What is your birthday month? ') # user inputs that are stored in to variables to be called upon later

length = str(len(name)) # this checks the length of the name and converts it to a string so it can be printed

def nameMonth(userName, nameLength, birthMonth): # a function to handle the printing and user inputs
    print('Hello, ' + userName + '!')
    print('The length of your name is ' + nameLength + ' characters, and you were born in the month of ' + birthMonth + '.')

    x = datetime.datetime.now() # this variable stores the current date

    if birthMonth == x.strftime("%B"): 
        print('It looks like it\'s your birthday month! Happy birthday ' + userName + '!')
    # this if statement looks at the birthday month entered by the user. %B is a wildcard that displays the current month as
    # its long-form name, e.g. September instead of Sept
    # if the user-inputted month matches the long-form month name of the current date, this happy birthday message is displayed
    # /!\ ISSUE /!\: the issue with this is that it requires the user to specifically enter the long form name of the month they were born in

nameMonth(name, length, month) # calls the above function and uses the user inputs