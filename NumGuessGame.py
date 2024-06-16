from random import randint
import os

guess = ""
level = 1
MaxLvls = 100
max = 10
TotalGuess = 0
AvgGuess = 0

while level < MaxLvls:
  print("Level "+str(level))
  
# Adds a random amount between 1 and 40 to the maximum possible guess.
  max = max + randint(1,40)
  ans = randint(1,max)
  
  guess = input("Guess a number between 1 and "+str(max)+": ")
  
# Prompts user to guess a possible number within the limit
  while guess.isdigit() == False:
    guess = input("Guess a number between 1 and "+str(max)+": ")
  guess = int(guess)
  
# Checks if prompt is correct
  while guess != ans:
    
# Checks if prompt is within the limits
    if guess>=1 and guess<max:  
      
# Checks if prompt is bigger or smaller than answer.
      if guess < ans:
        print('Higher')
        print('')
        guess = input("Guess a number between 1 and "+str(max)+": ")
# Check to see if input is valid
        while guess.isdigit() == False:
          guess = input("Guess a number between 1 and "+str(max)+": ")
        guess = int(guess)
        TotalGuess = TotalGuess+1
      
      elif guess > ans:
        print('Lower')
        print('')
        guess = input("Guess a number between 1 and "+str(max)+": ")
# Check to see if input is valid
        while guess.isdigit() == False:
          guess = input("Guess a number between 1 and "+str(max)+": ")
        guess = int(guess)
        TotalGuess = TotalGuess+1
# If input is not within boundries this code is executed which prompts user that their input is invalid and allows them to re enter their guess.
    else:
      print('Your number is not between 1 and '+str(max)+'! ')
      print('')
      guess = int(input("Guess a number between 1 and "+str(max)+": "))

# Output when player completes the level.
  print("You guessed the number.")
  TotalGuess = TotalGuess+1
  print('Total Guesses: '+str(TotalGuess))
  AvgGuess = TotalGuess/level
  print('Average Guesses: '+str(round(AvgGuess,2)))
  input('Press enter to go to next level.')

# Clears console for new level
  clear = lambda: os.system('clear')
  clear()

  level = level+1

# Abosluley amazing win message.
print('Congratulations u won.')