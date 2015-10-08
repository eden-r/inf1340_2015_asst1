#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# The Scenario  (Test)
# the user is prompted to answer questions about their car troubles to diagnose the problem
# the user inputs "Y" or "N"
# the user gets either another question prompt or a statement in response
# Assumption: input must be valid (i.e. one of "Y", or "N").


# Intended Program Prompt: Is your car silent when you turn the key?
# Actual Program Prompt: Is your car silent when you turn the key?
# Run1 (YY)
# Sample Program Input: Y
# Sample Program Output Description: another question prompt / a statement
# Sample Intended Program Output: Are the battery terminals corroded?
# Sample Actual Program Output: Are the battery terminals corroded?
# Sample Program Input: Y
# Sample Intended Program Output: Clean terminals and try starting again.
# Sample Actual Program Output: Clean terminals and try starting again.
# Run2 (YN)
# Sample Program Input: Y
# Sample Intended Program Output: Are the battery terminals corroded?
# Sample Actual Program Output: Are the battery terminals corroded?
# Sample Program Input: N
# Sample Intended Program Output: Replace cables and try again.
# Sample Actual Program Output: Replace cables and try again.
# Run3 (NY)
# Sample Program Input: N
# Sample Intended Program Output: Does the car make a clicking noise?
# Sample Actual Program Output: Does the car make a clicking noise?
# Sample Program Input: Y
# Sample Intended Program Output: Replace the battery
# Sample Actual Program Output: Replace the battery.
# Run4 (NNY)
# Sample Program Input: N
# Sample Intended Program Output: Does the car make a clicking noise?
# Sample Actual Program Output: Does the car make a clicking noise?
# Sample Program Input: N
# Sample Intended Program Output: Does the car crank up but fail to start?
# Sample Actual Program Output: Does the car crank up but fail to start?
# Sample Program Input: Y
# Sample Intended Program Output: Check spark plug connection.
# Sample Actual Program Output: Check spark plug connection.
# Run5 (NNNYY)
# Sample Program Input: N
# Sample Intended Program Output: Does the car make a clicking noise?
# Sample Actual Program Output: Does the car make a clicking noise?
# Sample Program Input: N
# Sample Intended Program Output: Does the car crank up but fail to start?
# Sample Actual Program Output: Does the car crank up but fail to start?
# Sample Program Input: N
# Sample Intended Program Output: Does the engine start and then die?
# Sample Actual Program Output: Does the engine start and then die?
# Sample Program Input: Y
# Sample Intended Program Output: Does your car have fuel injection?
# Sample Actual Program Output: Does your car have fuel injection?
# Sample Program Input: Y
# Sample Intended Program Output: Get it in for service.
# Sample Actual Program Output: Get it in for service.
# Run6 (NNNYN)
# Sample Program Input: N
# Sample Intended Program Output: Does the car make a clicking noise?
# Sample Actual Program Output: Does the car make a clicking noise?
# Sample Program Input: N
# Sample Intended Program Output: Does the car crank up but fail to start?
# Sample Actual Program Output: Does the car crank up but fail to start?
# Sample Program Input: N
# Sample Intended Program Output: Does the engine start and then die?
# Sample Actual Program Output: Does the engine start and then die?
# Sample Program Input: Y
# Sample Intended Program Output: Does your car have fuel injection?
# Sample Actual Program Output: Does your car have fuel injection?
# Sample Program Input: N
# Sample Intended Program Output: Check to ensure the choke is opening and closing.
# Sample Actual Program Output: Check to ensure the choke is opening and closing.
# Run7 (NNNN)
# Sample Program Input: N
# Sample Intended Program Output: Does the car make a clicking noise?
# Sample Actual Program Output: Does the car make a clicking noise?
# Sample Program Input: N
# Sample Intended Program Output: Does the car crank up but fail to start?
# Sample Actual Program Output: Does the car crank up but fail to start?
# Sample Program Input: N
# Sample Intended Program Output: Does the engine start and then die?
# Sample Actual Program Output: Does the engine start and then die?
# Sample Program Input: N
# Sample Intended Program Output: Engine is not getting enough fuel. Clean fuel pump.
# Sample Actual Program Output: Engine is not getting enough fuel. Clean fuel pump.



def diagnose_car():
    question_one = raw_input("Is the car silent when you turn the key?")
    yes_selection = "Y"
    if question_one == yes_selection:
        question_two = raw_input("Are the battery terminals corroded?") # if Y to question 1
        if question_two == yes_selection:
            print("Clean terminals and try starting again.") # if Y to question 2
        elif question_two == "N":
            print("Replace cables and try again.") #if N to question 2
        else:
            print("Error.")
    elif question_one == "N":
        question_three = raw_input("Does the car make a clicking noise?") # if N to question 1
        if question_three == yes_selection:
            print("Replace the battery.") # if Y to question 3
        elif question_three == "N":
            question_four = raw_input("Does the car crank up but fail to start?") # if N to quesiton 3
            if question_four == yes_selection:
                print("Check spark plug connections.") #if Y to question 4
            elif question_four == "N":
                question_five = raw_input("Does the engine start and then die?") # if N to question 4
                if question_five == yes_selection:
                    question_six = raw_input("Does your car have fuel injection?") # if Y to question 5
                    if question_six == yes_selection:
                        print("Check to ensure the choke is opening and closing.") #if Y to question 6
                    elif question_one == "N":
                        print("Get it in for service.") # if N to question 6
                    else:
                        print("Check to ensure the choke is opening and closing.") # if N to question 6
                else:
                    print("Error.")
            else:
                print("Error.")
        else:
            print("Error.")
    else:
        print("Error.")
