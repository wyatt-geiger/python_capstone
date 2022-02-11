"""This is a quiz program that lists out a sequence of topics for the user to choose from. Once the user selects their preferred
topic, the program goes through a dictionary of questions and tallies the score if the answer was correct. The results of the quiz
are printed out at the end."""

art_questions = {
    'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
    'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli'
}

space_questions = {
    'Which planet is closest to the sun?': 'Mercury',
    'Which planet spins in the opposite direction to all the others in the solar system? ': 'Venus'
    }   


class Topic: # topic class which contains initialization method, select_topic method, and string method
    def __init__(self, theme, questions): # initialization method - consider passing in the topic's questions 
        self.theme = theme.capitalize() 
        # theme variable which stores the topic. capitalize method is used for displaying the theme back to the user
        # and also to compare to the subjects in the if statements within select_topic
        self.question_dictionary = questions  # if it's not a list, avoid list as part of the variable name.  
        # Or this could be called something like questions_and_answers ? 
        # initializes an empty dictionary, which will store the questions and answers

    def select_topic(self): # select_topic method, which stores each subject and appends questions and answers to the empty dictionary

        print(f'-----\nYour selected quiz topic is: {self.theme}\n-----') # message showing user's selection
                

        # how would you manage a quiz with hundreds of questions? Consider providng the 
        # Topic with the questions when you create a Topic object.
        # this if block looks at the capitalized topic the user entered, and compares it to a string literal
        # if the two match, lines of code are fired to add questions and answers to the empty dictionary
        # This if block would have to be manually updated if the programmer wanted to add more subjects and/or questions

        # in general, a dictionary initializer would be less code than individual lines,
        #     self.question_list = { 'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
        #        'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli'
        #        .... etc 
        #       }

    def ask_questions(self): # __str__ should be used to print a string representation of an object, often for debugging. 
        #  use a regular method for this task 

        score = 0 # initializes a score variable to 0

        max_score = len(self.question_dictionary) # initializes a max_score variable which looks at the length of the dictionary

        for question, answer in self.question_dictionary.items(): # for loop which iterates over the dictionary
            
            print(question) # prints the key, or the question
            reply = input('Enter your answer: ') # stores the user input to the question in a variable

            if reply.lower() != answer.lower(): 
            # lowercases the user input reply and the dictionary value of the key so that any case may be entered by the user
                print(f'Sorry, the answer is {answer}.\n-----') # if the reply and answer don't match, this line is printed
            else:
                print('Correct!\n-----')
                score += 1
                # if the reply and answer do match, this line is printed and 1 is added to the score variable

        final_message = f'End of quiz!\nYour total score on {self.theme} questions is {score} out of {max_score}.'
        # stores a formatted string into a variable which contains feedback on the quiz results, including the score received

        if score/max_score == 1:
            return f'{final_message}\nYou got all the answers correct!'
        else:
            return final_message
        # if the score divided by the max score equals 1 (100%), then an additional message is displayed alongside the final_message variable
        # otherwise, only the final_message variable is printed

def main(): # main function

    question_bank = { 
        'Art': Topic('Art', art_questions),
        'Space': Topic('Space', space_questions) }

    topic_list = question_bank.keys()
    # initializes a list of topics. This list serves 2 purposes:
    # First, it is displayed to the user in a formatted list
    # Second, validation is used to determine if the user inputted a valid topic from this list
    # This list would have to be manually updated by the programmer if they wanted to add more topics

    format_list = ', '.join(topic_list)
    # the formatted list, to be displayed as the list of topic options for the user to pick from

    print('Welcome to the Quiz Program! Select a topic, answer questions about that topic, and see what your score is!')
    # greeting
    print(f'Which topic would you like to pick? Available topics: {format_list}')
    # user's topic choices using the formatted list
    
    topic = input(f'Enter your topic choice: ').capitalize() # program asks for user's topic choice

    while topic.capitalize() not in topic_list:
        print('That is not a valid topic.')
        topic = input(f'Enter your topic choice: ').capitalize()
    # this while loop uses the capitalize method to alter the user input so that it would match a topic in the list, essentially ignoring letter case
    # while loop continues to ask the question until a valid topic is entered

    # topic_result = Topic(topic.lower())
    quiz_topic = question_bank[topic]
    # this line lowercases the user input to be placed in the Topic class, which is then placed into the topic_result variable
    
    # topic_result.select_topic()
    # this line uses topic_result to call upon the select_topic() method, which checks the user input and matches it with a topic inside the method
    topic_result = quiz_topic.ask_questions()

    print(topic_result)
    # prints the string method inside the Topic class inside the topic_result variable

main()