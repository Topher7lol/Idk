import time
import random

value = 1
hi = True
printing = True
while_cooking = True  # Initialize while_cooking variable

while hi and printing and while_cooking:
    print(f"{value}.")
    value += 1
    if value == 1000000:
        hi = False
        while_cooking = False
        printing = False
        break  # Exit the loop instead of using return

if not while_cooking and not printing and not hi:
    print("Done!")

# Here, you should use an if statement, not a while loop
if value == 1000000 and not hi and not printing and not while_cooking:
    print(f"Your food is done cooking! ({value})")
    while_cooking = False
    option = input("Continue Counting/Cooking y/n: ").lower()  # Convert input to lowercase

    if option in ['yes', 'y']:
        while True:
            print(f"{value}.")
            value += 1
            if value == 1000000:
                break  # Exit the loop when value reaches 1000000

    elif option in ['no', 'n']:
        print("Done!")
