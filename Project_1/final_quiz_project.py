""" TODO: 
    Docstring
    Comments
    Add a conditional message if the user got 100%
    Look into soft-coding 'score out of 3' so 3 can be any number
    Change any variable named 'test'
    Review original code in quiz_project.py to identify any missing parts
    Review project requirements for any missing parts"""

class Topic:
    def __init__(self, theme):
        self.theme = theme.capitalize()
        self.question_list = {}

    def select_topic(self):

        print(f'-----\nYour selected quiz topic is: {self.theme}\n-----')
        
        if self.theme == 'Art':
            self.question_list['Who painted the Mona Lisa? '] = 'Leonardo Da Vinci'
            self.question_list['What precious stone is used to make the artist\'s pigment ultramarine? '] = 'Lapiz lazuli'
            self.question_list['Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city? '] = 'Chicago'
        elif self.theme == 'Space':
            self.question_list['Which planet is closest to the sun? '] = 'Mercury'
            self.question_list['Which planet spins in the opposite direction to all the others in the solar system? '] = 'Venus'
            self.question_list['How many moons does Mars have? '] = '2'
        elif self.theme == 'Pokemon':
            self.question_list['What is the first Pokemon on the Pokedex?'] = 'Bulbasaur'
            self.question_list['Who is the final Elite 4 member in Pokemon Red?'] = 'Lance'
            self.question_list['Who is the leader of Team Rocket?'] = 'Giovanni'

    def __str__(self):

        score = 0

        max_score = len(self.question_list) # this is the max score. requires further testing

        for question, answer in self.question_list.items():
            
            print(question)
            reply = input('Enter your answer: ')

            if reply != answer:
                print(f'Sorry, the answer is {answer}.\n-----')
            else:
                print('Correct!\n-----')
                score += 1

        return f'End of quiz!\nYour total score on {self.theme} questions is {score} out of {max_score}.'

def main():

    topic_list = ['Art', 'Space', 'Pokemon']

    format_list = ', '.join(topic_list)
        
    print(f'Which topic would you like to pick? Available topics: {format_list}')
    topic = input(f'Enter your topic choice: ')

    while topic.capitalize() not in topic_list:
        print('That is not a valid topic.')
        topic = input(f'Enter your topic choice: ')

    topic_result = Topic(topic.lower())

    topic_result.select_topic()

    print(topic_result)

main()