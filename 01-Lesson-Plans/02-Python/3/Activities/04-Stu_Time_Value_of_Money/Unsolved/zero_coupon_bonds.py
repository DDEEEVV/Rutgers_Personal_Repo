# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value

def calculated_present_value(future_value, discount_rate, compounding_periods, years):
    present_value = future_value / ((1 + (discount_rate / compounding_periods)) ** (compounding_periods * years))
    present_value_formatted = present_value



# Initialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables
calculated_present_value = calculated_present_value(future_value, discount_rate, compounding_periods, years)

# @TODO: Determine if the bond is worth it

print(f"The Present Value of {price} at a discount rate of {discount_rate} componded {compounding_periods} time(s) every year over{years} years is ${calculated_present_value}")