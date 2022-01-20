"""This program initializes an empty list of classes and asks the user to input some. Once the user
is finished inputting class names, the program prints out the list of classes that were entered."""

class_list = [] # initializing the empty list

print('Welcome to the class list program.')

def newClass(): # this function is used for entering new classes to the empty list
    while True:
        x = input('Please enter a class name to add to the list, or type EXIT: ')
        if x == 'EXIT' or x == 'exit':
            printList()
            break # if the user enters 'exit' or 'EXIT', the list of classes is printed and the while loop breaks
        else:
            class_list.append(x) 
            # if the user enters anything other than 'exit' or 'EXIT', the input is added
            # to the list as a new class

def printList(): # this function is used to print out the list of classes to the user
    
    if len(class_list) == 0: # this if statement checks if the list is empty. if it is, it loops back to the main function
        print('The class list is empty.')
        main()
    else: 
        print('Thank you for using this program. Here is the list of classes you entered: ')
        for e in class_list:
            print(e)
        main()
        # this else statement prints the list of classes entered. it then calls on the main function to ensure the user
        # does not want to add any more classes
        
def main(): # main function

    addClass = input('Would you like to add a class? Please enter Y or N: ')

    if addClass == 'Y' or addClass == 'y': # if the user chooses to enter a class, the newClass() function is called to enter a new class to the list
        newClass()
    elif addClass == 'N' or addClass == 'n': # if the user chooses not to enter a class, the program ends
        print('You have chosen not to enter any classes. Thank you for using this program.')
    else: # if the user does not enter a valid response, the program loops back to the main() function and starts over
        print('That is not a valid response.')
        main()
main()