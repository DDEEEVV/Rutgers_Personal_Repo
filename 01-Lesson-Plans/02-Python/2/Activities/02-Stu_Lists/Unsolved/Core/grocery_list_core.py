# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries

from os import remove


groceries = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]
print(f"list of groceries: {groceries}")

# @TODO: Find the first two items on the list
print(f"the first two items on the list are: {groceries[0:2]}")

# @TODO: Find the last five items on the list
print(f"the last five items on the list: {groceries[2:7]}")

# @TODO: Find every other item on the list, starting from the second item

print(f"all the other items after second one are : {groceries[2:]}")

# @TODO: Add an element to the end of the list
groceries.append("Wine")
print(groceries)

# @TODO: Changes a specified element within the list at the given index

groceries[7] = "Beer"
print(groceries)

# @TODO: Calculate how many items you have in the list
print(len(groceries))

# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name
print(groceries.index("Eggs"))

# @TODO: Remove an element from the list based on the given element name
groceries.remove("Beer")
print(groceries)

# @TODO: Remove an element from the list based on the given index
sugar_index = groceries.index("Sugar")
groceries.pop(sugar_index)
print(groceries)

# @TODO: Remove the last element of the list
groceries.pop(-1)
print(groceries)

print("You continue on your journey purchasing groceries...")
