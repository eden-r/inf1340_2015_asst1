#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# to do: make assumptions explicit
# for example, assumption that commission is paid on top of money spent on stock

# to do: add scenario to describe the test case.

#Constants
commission = 0.03
shares = 2000
sale_price = 900.00
sell_price = 942.75

money_spent = shares * sale_price
money_spent_plus_commission = money_spent + (money_spent * commission)
start_money = money_spent_plus_commission

# this is negative because the cash balance of Lakshmi is negative after purchasing stock
print(0 - money_spent_plus_commission)

money_earned = shares * sell_price
money_earned_minus_commission = money_earned - (money_earned * commission)
end_money = money_earned_minus_commission - start_money

# end money is the result of the first two transactions combined
print (end_money)


#placeholder
money = ""

print(money)
