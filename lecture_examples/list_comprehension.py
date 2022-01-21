# List comprehension examples

# list of classes for a student

class_list = ['ITEC 1100', 'ITEC 1150', 'ENGL 1340', 'MATH 1100']

# make a list of only ITEC classes

only_itec = [ c for c in class_list if c.startswith('ITEC') ]
# you can perform an operation on the first c, e.g. 'c.lower() for c'
print(only_itec)

print('-----')

# records temperatures everyday, record -1 if invalid temperature

high_temps = [-1, 56, 78, -1, 65, 86, -1]

# make a list of only the valid temperatures

valid_temps = [ temp for temp in high_temps if temp != -1 ] # removes all values that are -1
print(valid_temps)

# convert to celsius

temp_celsius = [ round((temp_f - 32) * 5 / 9, 2) for temp_f in valid_temps ] # round function is used to round to 2 decimals
print(temp_celsius)

# find the average temp

average = sum(temp_celsius)/len(temp_celsius)
print(f'The average temperature is: {average:.2f} C') # string formatting; .2f means round to two decimals

print('-----')

print('Video Exercises:')

num_list = [2,4,6]
num_list_plus_one = [ num + 1 for num in num_list ]
print(num_list_plus_one)

zero_list = [0,3,4,0,22,1]
non_zero = [ no_zero for no_zero in zero_list if no_zero != 0 ]
print(non_zero)

single_list = [0,10,4,0,32]
double_list = [ non_zero * 2 for non_zero in single_list if non_zero != 0 ]
print(double_list)