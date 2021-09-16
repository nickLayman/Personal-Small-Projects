import random
A=1
while A==1:
  while True:
    try:
      x=int(raw_input("Lower bound?\n"))
    except ValueError:
      print("Must be an integer")
      continue
    else:
      break
  while True:
    try:
      y=int(raw_input("upper bound?\n"))
    except ValueError:
      print("Must be an integer")
      continue
    else:
      break
  N=random.randint(x, y)
  while True:
    try:
      G=int(raw_input("Guess\n"))
    except ValueError:
      print"Must be an integer"
      continue
    else:
      break
  while G!=N:
    if G>N:
      print "Too High"
      while True:
        try:
          G=int(raw_input("Guess\n"))
        except ValueError:
          print"Must be an integer"
          continue
        else:
          break
    if G<N:
      print"Too Low"
      while True:
        try:
          G=int(raw_input("Guess\n"))
        except ValueError:
          print"Must be an integer"
          continue
        else:
          break
  if G==N:
    print"Yes! Congratulations!"
  while True:
    try:
      A=int(raw_input("Want to play again?\n 1:Yes\n 2:No\n"))
    except ValueError:
      print("Must be '1' or '2'")
      continue
    else:
      if A==2:
        print"Ok, Bye-Bye now!"
      break