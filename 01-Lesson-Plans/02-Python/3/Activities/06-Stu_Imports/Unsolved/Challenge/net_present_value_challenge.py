# -*- coding: utf-8 -*-
"""Student Activity: Financial Analysis using NPV.

This script will choose the optimal project scenario to
undertake based on max NPV values.
"""

# @TODO: Import the NumPy Financial (numpy_financial) library
import numpy_financial
import numpy_financial as npf

# Discount Rate
discount_rate = .1
interest_rate = discount_rate
# Initial Investment, Cash Flow 1, Cash Flow 2, Cash Flow 3, Cash Flow 4
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

# @TODO: Initialize dictionary to hold NPV return values
npv_dict = {}

# @TODO: Calculate the NPV for each scenario
NPV_Conservative = npf.npv(interest_rate,cash_flows_conservative)
print(f"\nThe NPV_Conservative is: {round(NPV_Conservative,2)}\n")

NPV_Neutral = npf.npv (interest_rate,cash_flows_neutral)
print(F"The NVP_Neutral is: {round(NPV_Neutral,2)}\n")

NPV_Aggressive = npf.npv(interest_rate, cash_flows_aggressive)
print(f"Then NPV_Aggressive is: {round(NPV_Aggressive,2)}\n")

# @TODO: Initialize variables



# @TODO: Iterate over npv_dict to find the max key-value pair










# @TODO: Print out the optimal project scenario with the highest NPV value
