"""
Conditionally Yours

Pseudocode:
1- Initialize variables current_price, original_price ec


"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price
import re


original_price = 450

# Create integer variable for current_price
current_price = 320

# Create float for threshold_to_buy
threshold_to_buy = -10

# Create float for threshold_to_sell
threshold_to_sell = +23

# Create float for portfolio balance


# Create float for balance check


# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price
change_in_price = original_price - current_price

# Calculate percent increase
percentage_change = (current_price - original_price ) / original_price * 100

# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(f"Netflix's current stock price was ${current_price}")

# Print percent increase
print(f"Netflix's percentage change in price is: {round(percentage_change, 2)}%")

# Determine if stock should be bought or sold
if percentage_change >= threshold_to_sell:
    recommendation = "SELL"
elif percentage_change <= threshold_to_buy:
    recommendation = "BUY"
elif percentage_change > threshold_to_sell and percentage_change < threshold_to_buy:
    recommendation = "HOLD"
else:
    print("ERROR, Need the human grain to control the machine!!!")


# Print recommendation
print("Recommendation: " + recommendation)
print()
print("But wait a minute... lets check your excess equity first.")


# Challenge

# Declare balance variable as a float
portfolio_balance = 5000

# Declare balance_check variable
balance_check = portfolio_balance * 5

# Compare balance to recommendation, checking whether or not balance is 5 times more than current_price
print(f"You currently have ${portfolio_balance} in excess equity available in your portfolio.")

# IF-ELSE Logic to determine recommendation based off of balance check
if recommendation == "BUY" and balance_check > current_price:
    print("Final recommendation is as I said before " + recommendation)
elif recommendation == "BUY" and balance_check < current_price:
    print("Final recommendation is to buy but you don't have enough $ in you account")
else:
    print("Final recommendation:" + recommendation)