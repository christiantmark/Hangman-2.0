def hidden(guessedLetters,sentence):
  for c in sentence:
    if c not in guessedLetters:
      if c != " ":
        sentence = sentence.replace(c,"_")
  return sentence

def main():
  sentence = input("Write a sentence: ")
  sentence = sentence.strip()
  guessedLetters = []
  print("\n\n\n\n\n\n\n\n\n\n\n\n")
  counter = 0
  while counter<6:
    print(hidden(guessedLetters,sentence))
    if sentence == hidden(guessedLetters,sentence):
      print("Congratulations you have won!")
      exit()
    print("You have " + str(6-counter) + " lives left.")
    print(guessedLetters)
    guess = input("Guess a letter: ")
    guessedLetters.append(guess)
    if guess in sentence:
      print("Correct!")
    else:
      print("Incorrect.")
      counter+=1
    print("==========================================")
  print("You have lost :(")



main()