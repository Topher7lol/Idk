import time
import random

value = 1

hi = True
printing = True

while hi == True and printing == True:
  print(f"{value}.")
  value += 1
  while_cooking = True
  if value == 1000000:
    hi = False
    while_cooking = False
    printing = False
  
if value == 1000000 and hi == False and printing == False:
  print(f"Your food is done cooking! ({value})")
  while_cooking = False
  option = input("Continue Counting/Cooking y/n: ")

  if option == 'yes' or 'Yes' or 'YES' or 'Y' or 'y':
      while True:
        print(f"{value}.")
        value += 1
elif option == 'no' or 'No' or 'NO' or 'N' or 'n' and while_cooking == False:
  print("Done!")
  hi = False
  
