#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# The Scenario
# The user is prompted by the program with a question regarding the number of sides your shape has
# The user enters a number between 3 and 10.
# The program outputs a textual description of the shape with the number of sides specified by the user
#   or "Error" if the number is not between 3 and 10.

# Intended Program Prompt: How many sides does your shape have? (Please enter a number)
# Actual Program Prompt: How many sides does your shape have? (Please enter a number)
# Run1
# Sample Program Input: 7
# Sample Program Output Description: The name of the shape with the number of sides specified by the user.
# Sample Intended Program Output: heptagon
# Sample Actual Program Output: heptagon
# Run2
# Sample Program Input: 11
# Sample Program Output Description: The name of the shape with the number of sides specified by the user.
# Sample Intended Program Output: Error
# Sample Actual Program Output: Error.


triangle = "3"
square = "4"
pentagon = "5"
hexagon = "6"
heptagon = "7"
octagon = "8"
nonagon = "9"
decagon = "10"

def name_that_shape():
    shape = str(raw_input("How many sides does your shape have? (Please enter a number)")) # ask for the number of sides
    if shape == triangle: #match the number of sides to the shape
        print("triangle") #print the name of the shape
    elif shape == square:
        print("square")
    elif shape == pentagon:
        print("pentagon")
    elif shape == hexagon:
        print("hexagon")
    elif shape == heptagon:
        print("heptagon")
    elif shape == octagon:
        print("octagon")
    elif shape == nonagon:
        print("nonagon")
    elif shape == decagon:
        print("decagon")
    else:
        print("Error.")


    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: 3, 4, 5, 6, 7, 8, 9, 10

    Expected Outputs: name of shape according to number entered

    Errors: entered something other than 3, 4, 5, 6, 7, 8, 9, 10

    """

name_that_shape()