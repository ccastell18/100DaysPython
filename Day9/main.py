from art import logo
from os import system

print(logo)
is_bidding = True

def find_highest(bidding_record):
  highest_bid = 0
  highest_bidder = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of {highest_bid}")

while is_bidding == True:
  bids = {}
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))

  bids["name"] = bid

  keep_bidding = input("Does anyone else want to bid? y/n ").lower()

  if keep_bidding == 'y':
    system('cls')
  else:
    is_bidding = False
    find_highest(bids)