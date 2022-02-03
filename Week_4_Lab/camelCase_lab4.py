def camel_case(sentence):

    string_list = sentence.split() # splits the user string into individual elements in a list

    new_list = [] # initializes an empty list

    ignore_list = ['!', '@', '.', '(', ')', '*'] # TODO: update this

    for e in string_list:
        if e not in ignore_list: # TODO: update this
            new_list.append((e.title())) # for every element in the list, capitalize only the first letter

    first_word = new_list[0].lower() 
    new_list[0] = first_word
    # these two statements look at the first element in the list and convert it to lowercase

    camel_sentence = "".join(new_list) # this joins all the elements in the list into a single string

    return camel_sentence # returns the value to be printed out in the main function


def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)


if __name__ == '__main__':
    main()