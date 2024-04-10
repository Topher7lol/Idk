import time
import random

value = 1

while True:
  print(f"{value}.")
  value += 1

  if value == 1000000:
    print("Your food is done cooking!")
    option = input("Continue Counting/Cooking y/n: ")

    if option == 'yes' or 'Yes' or 'YES' or 'Y' or 'y':
      while True:
        print(f"{value}.")
        value += 1
    elif option == 'no' or 'No' or 'NO' or 'N' or 'n':
        print("Done!")
