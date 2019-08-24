import random
def main():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)
  rnd = random.randomint(0, last)
  print(quotes[rnd])

  if 
   __name__== "__main__":
  main()
