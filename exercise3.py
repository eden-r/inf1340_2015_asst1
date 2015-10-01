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
    # ask "Is the car silent when you turn the key?"
    question_one = "Is the car silent when you turn the key?"
    # if the answer to "Is the car silent when you turn the key?" is yes, ask " Are the batter terminals corroded?"
    question_two = "Are the battery terminals corroded?" # if Y to question 1
        # if the answer to " Are the batter terminals corroded?" is yes, print "Clean terminals and try starting again."
    print("Clean terminals and try starting again.") # if Y to question 2
        # if the answer to " Are the batter terminals corroded?" is no, print "Replace cables and try again."
    print("Replace cables and try again.") #if N to question 2
    # if the answer to "Is the car silent when you turn the key?" is no, ask "Does the car make a clicking noise?"
    question_three = "Does the car make a clicking noise?" # if N to question 1
        # if the answer to "Does the car make a clicking noise?" is yes, print "Replace the battery."
    print("Replace the battery.") # if Y to question 3
        # if the answer to "Does the car make a clicking noise?" is no, ask "DOes the car crank up by fail to start?"
    question_four = "Does the car crank up but fail to start?" # if N to quesiton 3
            # if the answer to "DOes the car crank up by fail to start?" is yes, print "Check spark plug connection."
    print("Check spark plug connection.") #if Y to question 4
            # if the answer to "DOes the car crank up by fail to start?" is no, ask "Does the engine start and then die?"
    question_five = "Does the engine start and then die?" # if N to question 4
                # if the answer to "Does the engine start and then die?" is yes, ask "Does your car have fuel injection?"
    question_six = "Does your car have fuel injection?" # if Y to question 5
                # no instructions for what to say if the answer to "Does the engine start and then die?" is no
    print("Your car is working.") # if N to question 5
                    # if the answer to "Does your car have fuel injection?" is yes, print "Check to ensure the choke is opening and closing."
    print("Check to ensure the choke is opening and closing.") #if Y to question 6
                    # if the answer to "Does your car have fuel injection?" is no, print "Get it in for service"
    print("Get it in for service.") # if N to question 6
    # if the answer to any of these questions is not y or n, print "Error"
    print("Error.") # if something other than y or N is entered





    print("The battery cables may be damaged. Replace cables and try again.")



diagnose_car()