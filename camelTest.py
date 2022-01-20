question = ('What is 10 + 5? ', '15')
# This is a tuple, which acts similarly to a list.
# The difference is, a tuple cannot be modified, whereas a list can.

answer = input(question[0])
# The first element in the tuple is called upon, which is the question.
# This asks the user for an input and stores the answer in a variable

while answer != question[1]:
    print('That is incorrect. Try again.')
    answer = input(question[0])
# while the answer is not the second element in the tuple (15), the while loop will say
# incorrect and ask the question again

print('That is correct!')
# If the while loop check is passed, this message will show