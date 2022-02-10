from peewee import *

db = SqliteDatabase('chainsaw.sqlite') # initialize the database

class Juggler(Model): # create the Juggler class
    name = CharField()
    country = CharField()
    catches = IntegerField()
    # initializes the 3 fields for the Juggler class: name, country, catches

    class Meta:
        database = db
    
    def __str__(self): # resulting output
        return f'Name: {self.name}, Country: {self.country}, Record: {self.catches}'


def main():
    # menu options for the user to pick from
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record
    5. Display one record 
    6. Quit
    """
    # menu option 5 is added to display a single record

    db.connect() # connect to the database
    db.create_tables([Juggler]) # create the Juggler table in which data will be put into

    Juggler.delete().execute() # clear the database of any old information

    default_entries() # call upon the void method default_entries() to populate the database with some data

    while True: # menu displayed to the user
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5': # option 5 added to display only one record
            display_one_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')

def default_entries(): # void method used to populate database with default data

    janne = Juggler(name='Janne Mustonen', country='Finland', catches=98)
    janne.save()
    # create a record of a juggler and save it to the database

    ian = Juggler(name='Ian Stewart', country='Canada', catches=94)
    ian.save()

    aaron = Juggler(name='Aaron Gregg', country='Canada', catches=88)
    aaron.save()

    chad = Juggler(name='Chad Taylor', country='USA', catches=78)
    chad.save()

def display_one_record(): # method to display a single record
        
    view_name = input('What is the name of the juggler you want to view? ')

    if Juggler.select().where(Juggler.name.contains(view_name)): # if a record in the database contains the user input, the full record will be displayed
        for juggler in Juggler.select().where(Juggler.name.contains(view_name)):
            print(juggler)
    else:
        print('That record holder is not in the database, please try again.')


def display_all_records(): # method to display all records

    for juggler in Juggler.select():
        print(juggler)
    # display all records in the database

def add_new_record():

    while True:
        
        add_name = input('What is the name of the juggler you want to add? ')

        if Juggler.select().where(Juggler.name.contains(add_name)): # checks to see if the database contains a record with the given name
            print('That record holder is already in the database, please try again.')
        else:
            add_country = input('Where is the juggler from? ')

            add_catches = input('How many catches did the juggler make? ')

            new_record = Juggler(name=add_name, country=add_country, catches=add_catches) # records all the user input and saves it to the database
            new_record.save()
            print('Success!')
            break

def edit_existing_record():

    update_holder = input('Which record holder would you like to update? ')

    if Juggler.select().where(Juggler.name.contains(update_holder)): # searches the database to find a record that contains the user input

        for juggler in Juggler.select().where(Juggler.name.contains(update_holder)):
            jug_name = juggler.name

        update_catches = input('What is the new number of catches? ')
        # if the record is found, the program allows the user to change the number of catches the juggler made
        Juggler.update(catches=update_catches).where(Juggler.name == jug_name).execute() # executes command to update the number of catches
        print('Success!')

    else:
        print('That record holder is not in the database.')


def delete_record():

    delete_holder = input('Which record holder would you like to delete? ')

    if Juggler.select().where(Juggler.name.contains(delete_holder)): # searches database to find a record that contains user input

        for juggler in Juggler.select().where(Juggler.name.contains(delete_holder)):
            jug_name = juggler.name

        # if record is found, then program asks user to confirm if they want to delete the juggler
        yes_or_no = input(f'Are you sure you want to delete {jug_name}? ')

        # if user enters 'yes' or 'y', then program searches database for the record and deletes it
        if yes_or_no.lower() in {'yes', 'y'}:
            Juggler.delete().where(Juggler.name == jug_name).execute()
            print('Success!')
        else:
            print('You either selected \'No\' or did not enter a valid input. Please try again.')

    else:
        print('That record holder is not in the database. Please try again')


if __name__ == '__main__':
    main()