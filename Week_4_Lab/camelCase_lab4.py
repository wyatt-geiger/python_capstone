"""This program asks the user to input a sentence which the program will then camelcase. It uses a variety of checks
to ensure that improper inputs are not permitted."""

def camel_case(sentence):

    string_list = sentence.split() # splits the user string into individual elements in a list

    new_list = [] # initializes an empty list

    for e in string_list:
        if e.isalpha(): # check if each individual element is alphabetical. if it is, append element to the new list
            new_list.append((e.title())) # for every element in the list, capitalize only the first letter
            first_word = new_list[0].lower() # look at the first element in the list and convert it to lowercase
            new_list[0] = first_word # use the original first element as the first element in the new list

    camel_sentence = "".join(new_list) # this joins all the elements in the list into a single string

    return camel_sentence # returns the value to be printed out in the main function


def main(): # main function

    sentence = input('Enter your sentence: ') # user input

    while sentence == '' or sentence.isalpha() is False: # if the input is blank or no alphabetical, the program asks user to try again
        print('You have not entered anything or you entered an invalid input.')
        sentence = input('Enter your sentence: ')

    camelcased = camel_case(sentence) # camelcases the user input
    print(f'Your sentence in camelcase: {camelcased}') # print message with camelcased sentence


if __name__ == '__main__':
    main()