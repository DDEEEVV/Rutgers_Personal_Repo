# Creates a variable with a string "Frankfurter"
title = "Frankfurter"
years = 23
hourly_wage = 65.40
expert_status = True

# Print the variables
print(title)
print(years)
print(hourly_wage)
print(expert_status)

# Prints the data type of each declared variable
print("The data type of variable title is:", type(title)) #str
print("The data type of variable years is:", type(years)) #int
print("The data type of variable hourly_wage is:", type(hourly_wage)) #str
print("The data type of variable expert_status is:", type(expert_status)) #bool

# Using variable names in calculations
total_miles = 257
gallons_gas = 7.2
miles_per_gallon = total_miles / gallons_gas
print(miles_per_gallon)

# Updating variables using assignment
miles = 48
kilometers = miles / 0.621371

# Substituting/formatting variable
message = f"The total kilometers driven was: {kilometers}"
print(message)

# Variable naming conventions
# Bad Example
mpg = 24
# Better Example
miles_per_gallon = 24
