words = open("words.txt").read()
letterslist = [{},{},{},{},{}]
for word in words.split("\n"):
  for letternum,letters in enumerate(word):
    letterdict = letterslist[letternum]
    if letters not in letterdict:
      letterdict[letters] = 1
    else:
      letterdict[letters] += 1
def sortd(dict1):
  return sorted(dict1.items(), key=lambda x: x[1], reverse=True)
inputr = "bbbbb"
guesses = 1
wordvalue = {}
def search(letterslist1):
  for word in words.split("\n"):
      value = 0
      for letternum,letter in enumerate(word):
        value += letterslist1[letternum][letter]
      wordvalue[word] = value
  return sortd(wordvalue)[0][0]
cword = search(letterslist)
while inputr != "ggggg":
  print(cword)
  inputr = input("result: ")
  guesses += 1
  for snum, score in enumerate(inputr):
    if score == "g":
      for letter in letterslist[snum]:
        if letter != letterslist[snum][cword[snum]]:
          letterslist[snum][cword[snum]] = 0
        else:
          letterslist[snum][cword[snum]] += 200
    if score == "b":
      for letterb in letterslist:
        letterb[cword[snum]] = 0
    if score == "y":
      letterslist[snum][cword[snum]] = 0
  cword = search(letterslist)
  print(letterslist)
      
      
      
          
          
    