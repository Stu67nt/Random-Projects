min = int(input('Enter min guess: '))
max = int(input('Enter max guess: '))
correct = False

while correct == False:
  dif = max-min
  mid = round(dif/2)
  guess = min+mid
  correct = input('Is ' + str(guess) + ' your number? [y/n]')
  if correct == 'y':
    correct = True
    break
  elif correct == 'n':
    h_or_l = input('Is the number higher or lower than my guess? [h/l]')
    if h_or_l == 'h':
      min = guess-1
      correct = False
    elif h_or_l == 'l':
      max = guess-1
      correct = False
    
  else:
    print("ur bad")
print('done')