import os,time
while True:
  print("High ScoreTable")
  print()
  initials = input("input your initials >").upper()
  score = input("input your score >")
  print()
  f= open("highScore", "a+")
  f.write(f"{initials} {score}\n")
  #print("finißhed adding data")
  f.close()
  print("Finished entering data")
  finish = input("Add more data? yes/no ?")
  
  if finish == "no":
    break
  else: 
    continue
  #print("Finished entering data!")
  
  time.sleep(2)
  os.system("clear")
  
  






























































































































#import os, time

#while True:
  #print("High score table")
  #print()
  #initials = input("INITIALS >").upper()
  #score = input("SCORE >")
  #print()
  #f = open("topscore", "a+")
  #f.write(f"{initials} {score}\n")
  #f.close()
  #finish = input("Add more data? yes/no ?")
  #if finish == "no":
      #break
  #else:
      #continue
    #exit
  #print("Finished entering data!")

  #print("Added scores")
  #time.sleep(2)
  #os.system("clear")
