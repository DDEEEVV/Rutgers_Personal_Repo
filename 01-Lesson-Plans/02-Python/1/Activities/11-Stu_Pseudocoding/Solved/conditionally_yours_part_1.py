"""
Conditionally Yours

Pseudocode:
1. Initialize variables original_price, current_price, increase, percent_increase, recommendation, threshold_to_buy, and threshold_to_sell
2. Compoute increase
3. Compute percent_increase
4. IF percent_increase is greater than or equal to threshold_to_sell
        THEN Set recommendation to "sell"
    ELSE IF percent_increase is less than or equal to threshold_to_buy
        THEN set recommendation to "buy"
    ELSE IF percent_increase is less than threshold_to_sell and greater than threshold_to_buy
        THEN set recommendation to "hold"
    ELSE
        THEN print("Not enough data to make a decision. Need human input")
5. Print("Recommendation: " + recommendation)
"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price and current_price:
from time import perf_counter


original_price = 400
current_price = 325

# Creating threshold to buy and sell:
threshold_to_buy = -10
threshold_to_sell = +20

# Creating strings for recommendations:
recommendation = "Buy"

# Calculating the difference between current and original price:

change_in_price = current_price - original_price
print(f"Price of Netflix increased or decrease by: $ {change_in_price}")

# Calculating percentage increase:

percentage_increase = (current_price - original_price) / original_price * 100
print(f"The percentage change of Netflix is: {percentage_increase}%")


# Determine to buy or sell based on the change:
if percentage_increase >= threshold_to_sell:
    recommendation = "Sell"
elif percentage_increase <= threshold_to_buy:
    recommendation = "Buy"
elif percentage_increase < threshold_to_sell and percentage_increase > threshold_to_buy:
    recommendation = "hold"
else:
    print("not enough data, help needed")

print("My recommendation based on the market change is to " + recommendation)
print()
print("Let's check if you have $ on your account")


# another