""" This set of functions should return the appropriate data type"""


def return_number_3():
    """ This function should return an integer with the value of 3"""

    return_value = 3
    return return_value


def return_string_vcu():
    """ This function should return a string with the lowercase value of vcu"""

    return_value = 'vcu'
    return return_value


def return_lowercased_string(input_string):
    """You have a variable called input_string that is of type string.
    Return it but the lowercase version of it."""

    string = "INPUT_STRING"
    print(string.lower())


def return_without_starting_ending_whitespace(input_string):
    """You have a variable called input_string that is of type string.
    Return it but with the surrounding (left and right) whitespace stripped."""

    string = "      INPUT_STRING        "
    print(string)
    string.strip()
    print(string.strip())
    
    
def return_addition(first_number, second_number):
    """ Return the two numbers added together. """

    num1 = input( 'Enter first number: ')
    num2 = input( 'Enter second number: ')

    sum = float(num1) + float(num2)

    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

   
   
    
