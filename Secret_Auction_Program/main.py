import os
from art import logo

bidders_dict = {}

print(logo)
print("Welcome to the secret auction program.")

is_true = True

def find_highest_bidder(bid_record):
    w_bid = 0
    for bidder_name in bid_record:
        if bid_record[bidder_name] > w_bid:
            w_name = bidder_name
            w_bid = bid_record[bidder_name]

    print(f"The winner is {w_name} with a bid of ${w_bid}")

while is_true:
    bidder_name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders_dict[bidder_name] = bid

    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "no":
        is_true = False
        find_highest_bidder(bidders_dict)
    else:
        _ = os.system('cls')

# Frank Alexander Eraso Adarme, 2024.