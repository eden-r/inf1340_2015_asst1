#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


triangle = 3
square = 4
pentagon = 5
hexagon = 6
heptagon = 7
octagon = 8
nonagon = 9
decagon = 10

def name_that_shape():
    shape = raw_input("How many sides does your shape have?")



    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: 3, 4, 5, 6, 7, 8, 9, 10

    Expected Outputs: name of shape according to number entered

    Errors: entered something other than 3, 4, 5, 6, 7, 8, 9, 10

    """

    print("Error")

# ask for number of sides
# match number of sides to name of shape
# print name of shape

name_that_shape()