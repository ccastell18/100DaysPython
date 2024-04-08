#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

def difficulty():
  mode = input("Would you like easy mode with 10 guesses or hard mode with 5 guesses? ")
  if mode == "hard":
    guesses = 5
  else:  
    guesses = 10


def play():

  guesses = 10
  game_over = False  
  
  difficulty()

  number = random.randint(1,101)

  def compare():
   if guess > number:
    print("Too high")
    print(f"{guesses} left")
    print(number)
   elif guess < number:
    print("Too Low!")
    print(f"{guesses} left")
    print(number)
   else:
    print("You are correct")

  while game_over == False:
    guess = int(input("Guess a number between 0 and 100? "))
    guesses -= 1
    compare()
    if guesses == 0 or guess == number:
      again = input("Do you want to guess again? y/n ")
      if again == "y":
        play()
      else:
        game_over = True
play()      


