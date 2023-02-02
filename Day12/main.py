
import random

print('Welcome to the Number Guesing Game!')
print("I'm thinking of a number between 1 and 100")

def game():
  computer_number =  random.randint(1, 100)
  
  difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
  print(computer_number)
  guesses = 0

  if difficulty == 'easy':
    guesses = 10
  elif difficulty == 'hard':
    guesses = 5

  game_is_over = False

  while guesses > 0:

    print(f'You have {guesses} attempts to guess the number')
    guess = int(input("Make a guess: "))
    if guess > computer_number:
      print('Your number is too high!')
      guesses -= 1
    elif guess < computer_number:
      print('Your number is too low.') 
      guesses -=1
    else:
      print(f'You Win! The number was {computer_number}')
      return

    if guesses == 0:
      print(f"You've run out of turns.  The number was {computer_number}")
      

game()