"""This is a quiz program that lists out a sequence of topics for the user to choose from. Once the user selects their preferred
topic, the program goes through a dictionary of questions and tallies the score if the answer was correct. The results of the quiz
are printed out at the end."""

class Topic: # topic class which contains initialization method, select_topic method, and string method
    def __init__(self, theme): # initialization method
        self.theme = theme.capitalize() 
        # theme variable which stores the topic. capitalize method is used for displaying the theme back to the user
        # and also to compare to the subjects in the if statements within select_topic
        self.question_list = {}
        # initializes an empty dictionary, which will store the questions and answers

    def select_topic(self): # select_topic method, which stores each subject and appends questions and answers to the empty dictionary

        print(f'-----\nYour selected quiz topic is: {self.theme}\n-----') # message showing user's selection
        
        if self.theme == 'Art':
            self.question_list['Who painted the Mona Lisa? '] = 'Leonardo Da Vinci'
            self.question_list['What precious stone is used to make the artist\'s pigment ultramarine? '] = 'Lapiz lazuli'
            self.question_list['Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city? '] = 'Chicago'
            self.question_list['Which kid\'s TV characters are named after Renaissance artists? '] = 'Teenage Mutant Ninja Turtles'
            self.question_list['The graphite in an artist\'s pencil is made of what chemical element? '] = 'Carbon'
        elif self.theme == 'Space':
            self.question_list['Which planet is closest to the sun? '] = 'Mercury'
            self.question_list['Which planet spins in the opposite direction to all the others in the solar system? '] = 'Venus'
            self.question_list['How many moons does Mars have? '] = '2'
            self.question_list['What was the first human-made object to leave the solar system? '] = 'Voyager 1'
            self.question_list['When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what? '] = 'Meteor'
        elif self.theme == 'Sports':
            self.question_list['Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?'] = 'Simone Biles'
            self.question_list['Which country has won the soccer world cup the most times?'] = 'Brazil'
            self.question_list['What does MLB stand for?'] = 'Major League Baseball'
        
        # this if block looks at the capitalized topic the user entered, and compares it to a string literal
        # if the two match, lines of code are fired to add questions and answers to the empty dictionary
        # This if block would have to be manually updated if the programmer wanted to add more subjects and/or questions

    def __str__(self): # string method to be printed out to the user

        score = 0 # initializes a score variable to 0

        max_score = len(self.question_list) # initializes a max_score variable which looks at the length of the dictionary

        for question, answer in self.question_list.items(): # for loop which iterates over the dictionary
            
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

    topic_list = ['Art', 'Space', 'Sports'] 
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
    
    topic = input(f'Enter your topic choice: ') # program asks for user's topic choice

    while topic.capitalize() not in topic_list:
        print('That is not a valid topic.')
        topic = input(f'Enter your topic choice: ')
    # this while loop uses the capitalize method to alter the user input so that it would match a topic in the list, essentially ignoring letter case
    # while loop continues to ask the question until a valid topic is entered

    topic_result = Topic(topic.lower())
    # this line lowercases the user input to be placed in the Topic class, which is then placed into the topic_result variable

    topic_result.select_topic()
    # this line uses topic_result to call upon the select_topic() method, which checks the user input and matches it with a topic inside the method

    print(topic_result)
    # prints the string method inside the Topic class inside the topic_result variable

main()