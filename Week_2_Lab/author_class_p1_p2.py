"""This program creates an Author class. It displays the name of an author and the books published by that author."""

class Author: # author class which handles the sample data
    def __init__(self, name): # initializes attributes of the Author class
        self.name = name # author's name
        self.book_list = [] # empty list which published books will be added to
    
    def publish(self, books):
        if self.book_list.__contains__(books): # if the list already contains a book by the same name, an error message is displayed
            print(f'/!\ Error: {books} will only be entered once. Duplicates are not permitted /!\\')
        else:
            self.book_list.append(books) # if there are no duplicates, the book is added to the list
    
    def __str__(self):
        book_list = ', '.join(self.book_list) # formats the list to remove brackets
        return f'-----\nAuthor Name: {self.name} \nBooks Published: {book_list}\n-----' # the final result message, which is called upon in the main function

def main(): # main function
    wyatt = Author('Wyatt') # sample data
    wyatt.publish('Onion Knight') # publish function is called, in which 'Onion Knight' is entered
    wyatt.publish('Dragon Quest')
    wyatt.publish('Onion Knight')

    print(wyatt) # result

main()