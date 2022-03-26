# Define a function `calculate` that takes in two numbers and adds, subtracts, multiplies, or divides the two numbers.

from unittest import result


def calculate(num_1, num_2):
    # Create a variable `result` and set it to 0.
    result = 0

    # Prompt the user "What do you want to do: Add, Subtract, Multiply or Divide?" and assign the answer to a variable `choice`.
    choice = input("What do you want to do: Add, Subtract, Multiply or Divide?")

    # Create an if-else statement to perform the proper calculation with the two parameters based on the user's `choice`.

    if choice == ("Add"):
        result = num_1 + num_2
    if choice == ("Substract"):
        result = num_1 - num_2
    if choice == ("Multiply"):
        result = num_1 * num_2
    if choice == ("Divide"):
        result = num_1 / num_2
    else:
        print("You really don't like Math!!!")
    # Return the calculated `result` variable.
    return result

# Call the `calculate` function and print the results.
print(calculate(10, 3))

