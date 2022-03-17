# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries

Groceries = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]

print(Groceries) #The original list of Groceries

# @TODO: Find the first two items on the list

print(Groceries[0:2])


# @TODO: Find the last five items on the list

print(Groceries[2:7])


# @TODO: Find every other item on the list, starting from the second item

print(Groceries[1::2])


# @TODO: Add an element to the end of the list

Groceries.append("Vodka")

print(Groceries) #we will see that in the list of groceries has been added Vodka


# @TODO: Changes a specified element within the list at the given index

index = Groceries.index("Vodka")
Groceries[index] = "White_Wine"
print(Groceries) # we will see tha in the list we are not buying Vodka for tonight but White Wine

#or it can be written in one line of code as: Groceries[Groceries.index("Vodka")] = White_Wine

# @TODO: Calculate how many items you have in the list

print(len(Groceries))

# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name

print(Groceries[2]) #the third item on the list is eggs (0,1,2) we start from 0 that's why nr2 corresponds the 3rd item

# @TODO: Remove an element from the list based on the given element name

Groceries.remove("Eggs")
print(Groceries)  #it will show the list without Eggs

# @TODO: Remove an element from the list based on the given index

del Groceries[1] 
print(Groceries)  #it will show the list without Butter (the second on the list)

# @TODO: Remove the last element of the list

del Groceries[-1] #no alcohol for tonight it is the month of Ramadan

print("You continue on your journey purchasing groceries...")
