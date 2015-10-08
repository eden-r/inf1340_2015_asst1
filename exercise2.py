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

# Assumption: input must be valid (i.e. one of 3, 4, 5, 6, 7, 8, 9, or 10).

# Test Cases:
# Intended Program Prompt: How many sides does your shape have? (Please enter a number)
# Actual Program Prompt: How many sides does your shape have? (Please enter a number)

# Run1
# Sample Program Input: 3
# Sample Program Output Description: The name of the shape with the number of sides specified by the user.
# Sample Intended Program Output: triangle
# Sample Actual Program Output: triangle
# Run2
# Sample Program Input: 4
# Sample Intended Program Output: square
# Sample Actual Program Output: square
# Run3
# Sample Program Input: 5
# Sample Intended Program Output: pentagon
# Sample Actual Program Output: pentagon
# Run4
# Sample Program Input: 6
# Sample Intended Program Output: hexagon
# Sample Actual Program Output: hexagon
# Run5
# Sample Program Input: 7
# Sample Intended Program Output: heptagon
# Sample Actual Program Output: heptagon
# Run6
# Sample Program Input: 8
# Sample Intended Program Output: octagon
# Sample Actual Program Output: octagon
# Run7
# Sample Program Input: 9
# Sample Intended Program Output: nonagon
# Sample Actual Program Output: nonagon
# Run8
# Sample Program Input: 10
# Sample Intended Program Output: decagon
# Sample Actual Program Output: decagon


triangle = "3"
square = "4"
pentagon = "5"
hexagon = "6"
heptagon = "7"
octagon = "8"
nonagon = "9"
decagon = "10"

def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: 3, 4, 5, 6, 7, 8, 9, 10

    Expected Outputs: name of shape according to number entered

    Errors: entered something other than 3, 4, 5, 6, 7, 8, 9, 10

    """

    shape_edges = str(raw_input("How many sides does your shape have? (Please enter a number)")) # ask for the number of sides
    shape_text = "" #Initialize variable
    if shape_edges == triangle: #match the number of sides to the shape
        shape_text = "triangle" #store the name of the shape
    elif shape_edges == square:
        shape_text = "quadrilateral"
    elif shape_edges == pentagon:
        shape_text = "pentagon"
    elif shape_edges == hexagon:
        shape_text = "hexagon"
    elif shape_edges == heptagon:
        shape_text = "heptagon"
    elif shape_edges == octagon:
        shape_text = "octagon"
    elif shape_edges == nonagon:
        shape_text = "nonagon"
    elif shape_edges == decagon:
        shape_text = "decagon"
    else:
        shape_text = "Error"
    print(shape_text)



