from art import logo,vs
from game_data import data
import random
import os

print(logo)

# format data
def format_data(account):
  account_name = account['name']
  account_description = account['description']  
  account_country = account['country']
  return(f"{account_name}, a {account_description}, from {account_country}, follower count {account['follower_count']}")
# account_name = account_a['name']
# account_description = account_a['description'] 
# account_country = account_a['country']
# print(f"{account_name}, a {account_description}, from {account_country}")
# Check answer
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess== 'b'

score = 0

game_should_continue = True 
account_b = random.choice(data)

while game_should_continue:
  #random data
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  # guess
  guess = input("Who has more followers? Type 'A' or 'B'  ").lower()

  # compare
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  os.system('clear')
  print(logo)
  # Feedback
  if is_correct:
    score += 1
    print('You are correct!')
  else:
    print(f"Sorry, that is wrong. Your final score is {score}")
    game_should_continue = False


