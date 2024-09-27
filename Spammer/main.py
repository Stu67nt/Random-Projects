from keyboard import *
import time

spam_input = input("Enter spammed text: ")

time.sleep(5)

while is_pressed('#') == False:
  write(spam_input)
  press('enter')
  time.sleep(0.3)
print("stopped")
