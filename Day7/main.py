import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += '_'
print(display)

end_of_game = False

while not end_of_game:
  guess  = input("Choose a letter? ").lower()
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(f"{' '.join(display)}")

  if "-" not in display:
    end_of_game = True
    print("you win!!")