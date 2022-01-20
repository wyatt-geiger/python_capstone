# this is an example of error handling with try and except functions

name_list = ['Teddy', 'Wyatt', 'Zeke', 'Eren']

try: # this try-except attempts to print the 7th element in the list, which does not exist, causing the except function to activate instead
    print(name_list[7])
except Exception as e: # specifying Exception as e and printing it allows us to see what the actual error is, useful for development
    print(e)
    print('It appears that element does not exist.') # this message is mostly for end users