#Step 1 
from art import logo, stages
from words import word_list as wl
import random

word_list = wl 
end_of_game = False
lives = 6
display = []
chosen_word = random.choice(word_list)

for char in chosen_word:
  display.append("_")
print(display)

print(logo)
while not end_of_game:
  
  guess = input("Guess a letter? ").lower()

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    
    if letter == guess:
      display[position] = letter

  print(display)

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game == True
      print("you lose")



  if "_" not in display:
    end_of_game == True

  print(stages[lives])
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#for letter in [*chosen_word]:
 # if guess == letter:
  #  print(letter)
  #else:


  
