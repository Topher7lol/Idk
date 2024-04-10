import time
import random

value = 1

hi = True

while hi == True:
  print(f"{value}.")
  value += 1
  if value == 1000000:
    hi = False
  
if value == 1000000 and hi == False:
  print(f"Your food is done cooking! ({value})")
  option = input("Continue Counting/Cooking y/n: ")

  if option == 'yes' or 'Yes' or 'YES' or 'Y' or 'y':
      while True:
        print(f"{value}.")
        value += 1
elif option == 'no' or 'No' or 'NO' or 'N' or 'n':
  print("Done!")
