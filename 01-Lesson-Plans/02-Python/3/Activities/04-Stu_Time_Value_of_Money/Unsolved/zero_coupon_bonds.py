# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value

from dis import dis


def calculate_present_value(future_value, discount_rate, compounding_periods, years):


    """""
    Calculates the present value of money given the future_value, interest_rate, compounding_period, and number of years.
    Args:
        future_value (float): The future value
        discount_rate (float): The interest rate
        compounding_periods (int): The compounding period
        time_to_maturity (int): THe number of years
    Returns:
        The present value of money.
    """
    pv = future_value / (1 + (discount_rate / compounding_periods )) ** (compounding_periods * years)
    return pv 

# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1

price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables

fair_market_price = calculate_present_value(future_value, discount_rate, compounding_periods, years)

# @TODO: Determine if the bond is worth it

if fair_market_price > price:
    discount = fair_market_price - price
    print(f"The discount rate is {discount}")
elif fair_market_price < price:
    premium = price - fair_market_price
    print(f"The premium is {round(premium,2)}")
else: 
    print(f"The bond price {price} is trading at its fair value({fair_market_price})")

"""
The bond it traded at Premium it is $79.08 more than the Fair Market Value ~ Not Worth Buying 
"""