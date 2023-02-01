import random
from art import logo
from os import system


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) ==2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1) 
  
  return sum(cards)

def compare(your_score, computer_score):
    if your_score == 0:
      print('You win!')
    elif your_score > computer_score and your_score != 0 and computer_score != 0:
      print("You win!") 
    elif computer_score > 21:
      print("You win!")
    else:
      print("Computer wins!")
 
def play_game():
  print(logo)
  your_hand = []
  computer_hand = []
  is_game_over = False

  for _ in range(2):
    your_hand.append(deal_card())
    computer_hand.append(deal_card())
  while is_game_over == False:
    your_score = calculate_score(your_hand)
    computer_score = calculate_score(computer_hand)

    print(f"  Your cards: {your_hand}, current score: {your_score}")
    print(f"  Computer's first card: {computer_hand[0]}")

    if your_score == 0 or computer_score == 0 or your_score > 21:
      play = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        your_hand.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_hand.append(deal_card())
    computer_score = calculate_score(computer_hand)
  
  print(f" Your hand: {your_hand} and Computer hand{computer_hand}")
  compare(your_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'. " ) == "y":
  play_game()
  cls = lambda: system('cls')