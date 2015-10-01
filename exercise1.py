#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


commission = 0.03
purchase_price = 942.75

shares = 2000
sale_price = 900.00
# calculate money spent 2000 shares * $900.00 per share
money_spent = shares * sale_price
# calculate commission as 3% of money spent
money_spent_plus_commission = money_spent * commission
# store money spent
start_money = money_spent_plus_commission
# print money
print(0 - money_spent_plus_commission)
# calculate money earned as 2000 shares * $942.75 per share
# calculate commission as 3% of money earned
# subtract commission from money earned
# print money
# compare money earned to money spent to determine whether Lakshmi made a profit or loss

#placeholder
money = 0

print(money)
