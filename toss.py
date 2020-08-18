import random
print("enter your choice heads/tails")
human=input()
li=['heads','tails']
com=(random.choice(li))
if human==com:
  print("computer throws ",com," you match...congradulations!!")
else:
  if com=='tails' and  human=='heads':
    print("computer throws ",com," you lost...better luck next time!!")
  elif com=='heads' and  human=='tails':
    print("computer throws ",com," you lost...better luck next time!!")
  else:
    print("check the spelling!!")
