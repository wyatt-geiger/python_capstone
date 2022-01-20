"""This program creates a class that handles sample data from the main function and format the data into a string,
which is then returned to the main function for output."""

from dataclasses import dataclass # imports dataclass

@dataclass
class Student: # creates a Student class, which handles the sample data in the main function
    name: str
    school_id: str
    gpa: float
    # defines the variables used and their data type

    def __str__(self): # returns the final formatted string to main to be printed
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

def main(): # main function

    alex = Student('Alex', 'abcdef', 3.7) # calls upon the Student class and inputs sample data
    print(alex.name) # calls upon specific variables within Student class to be printed
    print(alex.school_id)
    print(alex.gpa)
    print(alex) # prints the final formatted string from Student class

    sam = Student('Sam', 'qwerty', 3.245) # more sample data placed into Student class
    print(sam) # prints the final formatted string from Student class

main()

# Final Thoughts: The most obvious advantage of the dataclass version vs. the traditional version is
# readability and simplicity by not having to type out the __init__ method. Another advantage is that with dataclass,
# it is more straightforward and easier to define the data types for the variables. This allows you to specify
# the data type you want, which is useful if you want to make sure the variable is always a float as opposed to an integer, for example.