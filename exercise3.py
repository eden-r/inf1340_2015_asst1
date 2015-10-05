#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs: y, n

    Expected Outputs: further questions, answers

    Errors: input other than y, n

    """

    question_one = raw_input("Is the car silent when you turn the key?")

    question_two = raw_input("Are the battery terminals corroded?") # if Y to question 1
    print("Clean terminals and try starting again.") # if Y to question 2
    print("Replace cables and try again.") #if N to question 2

    question_three = raw_input("Does the car make a clicking noise?") # if N to question 1

    print("Replace the battery.") # if Y to question 3

    question_four = raw_input("Does the car crank up but fail to start?") # if N to quesiton 3

    print("Check spark plug connection.") #if Y to question 4

    question_five = raw_input("Does the engine start and then die?") # if N to question 4

    question_six = raw_input("Does your car have fuel injection?") # if Y to question 5

    print("Your car is working.") # if N to question 5

    print("Check to ensure the choke is opening and closing.") #if Y to question 6

    print("Get it in for service.") # if N to question 6

    print("Error.") # if something other than y or N is entered





    print("The battery cables may be damaged. Replace cables and try again.")



diagnose_car()