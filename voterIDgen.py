from random import randint
from voterID import voternum

num = 1
codegen = int(input("How may codes do you wish to generate? "))

while num <= codegen:
  codenum = randint(10000,99999)
  print(codenum)
  with open("voterID.py","w") as f:
    voternum.append(str(codenum))
    f.write("voternum ="+str(voternum))
  num += 1