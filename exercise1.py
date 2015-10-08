#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# The Scenario
# Lakshmi buys 2000 shares at $900.00 per share (2000 * $900.00 = $1800000)
# Lakshmi pays the stockbroker 3% commission of the buy price (0.03 * $1800000 = $54000)
# Lakshmi spent a total of $1800000 + $54000 = $1854000
# Lakshmi sells 2000 shares at $942.75 per share (2000 * $942.75 = $1885500)
# Lakshmi pays the stockbroker 3% commission of the sell price (0.03 * $1885500 = $56565)
# Lakshmi earned a total of $1885500 - $56565 = $1828935
# Lakshmi's balance is earned - spent ($1828935 - $1854000 = -$25065); Lakshmi lost money

# Program Input: None
# Program Output Description: Lakshmi's Balance after paying the stockbroker each time.
# Intended Program Output:
#   -1854000
#   -25065
# Actual Program Output:
#   -1854000.0
#   -25065.0

# Constants
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
