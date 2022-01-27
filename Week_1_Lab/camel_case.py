"""This program accepts a user inputted string. It then parses the string to apply camel case to it using
string manipulation techniques."""

def parser(userInput): # function to work on the user string
    
    string_list = userInput.split() # splits the user string into individual elements in a list

    new_list = [] # initializes an empty list

    for e in string_list:
        new_list.append((e.title())) # for every element in the list, capitalize only the first letter

    first_word = new_list[0].lower() 
    new_list[0] = first_word
    # these two statements look at the first element in the list and convert it to lowercase

    t = "".join(new_list) # this joins all the elements in the list into a single string

    return t # returns the value to be printed out in the main function

def banner(): # banner method which displays a greeting to the user

    message = 'Welcome to the camel case parser program!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n') # prints greeting

def main(): # main function
    banner() # calls banner method to greet user
    userText = input('Please enter a string to be parsed: ') # asks for user input
    print(parser(userText)) # prints the result from the parser() function
main()