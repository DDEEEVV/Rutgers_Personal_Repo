# Declare a variable `welcome_name` as an input with a string of "Welcome to the sandwich shop, what do I call you? ".


welcome_name = input("Welcome to the sandwich shop, what do I call you?") 
print(f"Hello, {welcome_name}")

question_sandwich = input("Are you here for a sandwich? (Y/N)")
if question_sandwich == "Y":
    food_prompt = input("What kind of sandwich would you like?")
    print(f"Please wait 10 min for your {food_prompt}")

elif question_sandwich == "N":
    print("If you don't want a sandwich what are you here for?! Go nxt door for Weed, and come later for a sandwich OKAY!")
else:
    print("You did not write Y or N!")