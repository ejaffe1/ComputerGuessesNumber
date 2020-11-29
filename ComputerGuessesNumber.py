import random
import time
turns=0
print("Welcome! You will pick a number and I will try to guess your number.")
time.sleep(1)
playerNumber=int(input("Please enter a number from 1 to 100..."))

guess=random.randint(1,100)
print("My first guess is", guess)
time.sleep(2)

# Computer's Guess
def computerGuess():
  global guess
  if guess==playerNumber:
    print("Yes! I am correct!")

  elif guess>playerNumber:
    print("Hmm it appears I am too high...")
    print("I will guess again")
    newGuess=str(random.randint(1,guess))
    guess=[]
    guess.append(newGuess)
    guess="".join(guess)
    guess=int(guess)
    print("My next guess is", guess)

  elif guess<playerNumber:
    print("Hmm it appears I am too low...")
    print("I will guess again")
    newGuess=str(random.randint(guess,100))
    guess=[]
    guess.append(newGuess)
    guess="".join(guess)
    guess=int(guess)
    print("My next guess is", guess)

while True:
  computerGuess()
  turns=turns+1
  if guess==playerNumber:
    print("I guessed your number in", turns,"turns.")
    break


  
