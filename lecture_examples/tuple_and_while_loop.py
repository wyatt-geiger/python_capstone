# t = input('Enter a string: ')

# string_list = t.split()

# new_list = [1, 2, 3, 4, 'pizza']

# print(string_list)

# print(new_list)

# if int in string_list:
#     print('Error')
# else:
#     print('Success')

animals = ('What is 10 + 5? ', '15')

answer = input(animals[0])

while answer != animals[1]:
    print('That is incorrect. Try again.')
    answer = input(animals[0])

print('That is correct!')