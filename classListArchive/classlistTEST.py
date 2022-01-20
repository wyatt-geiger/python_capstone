""""""

class_list = []

print('Welcome to the class list program.')

def newClass():
    while True:
        x = input('Please enter a class name to add to the list, or type EXIT: ')
        if x == 'EXIT' or x == 'exit':
            printList()
            break
        else:
            class_list.append(x)

def printList():
    
    if len(class_list) == 0:
        print('The class list is empty.')
        main()
    else:
        print('Thank you for using this program. Here is the list of classes you entered: ')
        for e in class_list:
            print(e)

def main():

    addClass = input('Would you like to add a class? Please enter Y or N: ')

    if addClass == 'Y' or addClass == 'y':
        newClass()
    elif addClass == 'N' or addClass == 'n':
        print('You have chosen not to enter any classes. Thank you for using this program.')
    else:
        print('That is not a valid response.')
        main()
main()