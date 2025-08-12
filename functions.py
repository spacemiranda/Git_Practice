# Here are some functions that you can fill in to make them work.
# Replace the "raise NotImplementedError" line with the correct code!
   
import numpy as np
import astropy

def print_the_instructors_name():
    print('Dax')

def print_the_number_of_this_room():
    print('5382')

def split_this_string_at_each_space(input_string):
    return(input_string.split(' '))

def take_the_average_of_these_numbers(a, b):
    return(np.mean([a, b]))

def print_the_time_now_using_astropy():
    return('not yet')

def return_the_minimum_of_two_numbers(a, b):
    return(np.min([a, b]))

def return_the_std_of_two_numbers(a, b):
    return(np.std([a, b]))

def hello_world():
    print('hello world! <3')

def randomplanetgenerator(planetslist = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']):
    indx = np.random.randint(0, len(planetslist))
    print(f"Planet {indx}: {planetslist[indx]}")
    return(planetslist[indx])

def testall():
    print('Testing all functions in functions.py')
    print_the_instructors_name()
    print_the_number_of_this_room()
    split_this_string_at_each_space('split this on spaces')
    take_the_average_of_these_numbers(10, 20)
    #print_the_time_now_using_astropy()
    return_the_minimum_of_two_numbers(10, 20)
    return_the_std_of_two_numbers(10, 20)
    hello_world()
    randomplanetgenerator()
