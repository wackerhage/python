from replit import clear

from art import logo

print(logo)
print("Welcome to the Blind Auction!\n")

bids = {}
game = True

def finding_highest_bid(bidding_record):
  # biddings_record = bids{} = {"dom": 30, "mod": 10}
  reference_value = 0
  winner = ""
  for key in bidding_record:
    bid_amount = bids[key]
    if bid_amount > reference_value:
      reference_value = bid_amount
      winner = key
  print(f"The winner is {winner}, with the amount of ${reference_value}.")

while game is True:
  name = input("What's your name?\n")
  price = int(input("How much is the bid?\n"))
  bids[name] = price
  any_more_bidders = input("Any more bidder? (yes or no)\n")
  if any_more_bidders == "no":
    clear()
    game = False
    finding_highest_bid(bids)
  elif any_more_bidders == "yes":
    clear()
  



