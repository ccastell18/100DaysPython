from art import logo, vs
from game_data import data
import random

print(logo)
card = {}
card1 = {}
card2 = {}

def get_card(data, card):
  card_data = data[random.randint(0, len(data)-1)]
  card = {
    'name': card_data['name'],
    'description': card_data["description"], 
    'follower_count':card_data['follower_count'],
    'country':card_data["country"]
  } 
  return card

def format(card):
  name = card['name']
  description = card["description"]
  country = card["country"]
  print(f"Name:{name}\n Description:{description}\n Country: {country}")


def board(card1, card2):
  print(format(card1))
  print(vs)
  print(format(card2))

def play_game():
  game_over = False
  card1 = get_card(data, card)
  card2 = get_card(data, card)
  score = 0
  while not game_over:
    board(card1, card2)
    result = '' 
    if card1["follower_count"] < card2["follower_count"]:
      result = "higher"
    else:
      result = "lower"

    guess = input("Is the follower count for the second user higher or lower than the first user?")

    if guess == result:
      print("you are correct!")
      score += 1
      card1 = card2
      card2 = get_card(data, card)
    else:
      print(f"You are wrong! End score is {score}")
      game_over = True

play_game()