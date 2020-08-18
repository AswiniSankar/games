import random
print("enter your choice from",end=' ')
print("stone,paper,siccors")
human=input()
c=['stone','paper','siccors']
com=(random.choice(c))
if human==com:
 print("this match is tie...",end=' ')
 print("computer throws ",com)
elif(human=='stone'):
 if com=='paper':
   print("you lost!! paper rolls the stone",end=' ')
   print("computer throws ",com)
 else:
   print("you win!! stone break the siccors",end=' ')
   print("computer throws ",com)
elif (human=='paper'):
  if com=='siccors':
     print("you lost!! siccors cuts the paper",end=' ')
     print("computer throws ",com)
  else:
    print("you win!! paper rolls the stone",end=' ')
    print("computer throws ",com)
elif (human=='siccors'):
 if com=='stone':
     print("you lost!! stone break the siccors",end=' ')
     print("computer throws ",com)
 else:
    print("you win!! siccors cuts the paper",end=' ')
    print("computer throws ",com)
else:
   print("check the spelling")
