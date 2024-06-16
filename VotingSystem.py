from voterID import voternum

voterID = voternum

while True:
  voterIDdetection = input("Enter Voter ID or type checkvotes to see vote count: ")
  if voterIDdetection in voterID:
    with open("voterID.py", "w") as f:
        if voterIDdetection in voterID:
            voterID.remove(voterIDdetection)
            voterID = voternum
            f.write("voternum ="+str(voterID))
  elif voterIDdetection == "checkvotes":
    f = open("a_votes.txt", "r")
    print("A votes: "+str(len(f.readlines())))
    f.close()
    f = open("b_votes.txt", "r")
    print("B votes: "+str(len(f.readlines())))
    f.close()
    break
    
  else:
    print("Be gone.")
    break
    
  vote = input("Who do you want to vote? A or B? ")

  vote = vote.lower()

  if vote == "a":
    f = open("a_votes.txt", "a")
    f.write("+1\n")
    f.close()

  elif vote == "b":
    f = open("b_votes.txt", "a")
    f.write("+1\n")
    f.close()
