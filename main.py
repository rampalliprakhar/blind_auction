from art import logo
import time
import random
import os

print(logo)

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Determine the highest bid
def highest_bid(auction_dictionary):
    if not auction_dictionary:
        print("No valid bids received.")
        return

    winner = ""
    max_bid = 0
    for bidder in auction_dictionary:
        bid_amount = auction_dictionary[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}.")
    
    random_prize()

# Display leaderboard
def show_leaderboard(auction_dictionary):
    sorted_bidders = sorted(auction_dictionary.items(), key=lambda x: x[1], reverse=True)
    print("\n--- Leaderboard ---")
    for i, (bidder, bid) in enumerate(sorted_bidders, start=1):
        print(f"{i}. {bidder}: ${bid}")
    print("-------------------\n")

# Random prize for a lucky participant
def random_prize():
    prizes = ["Free Vacation", "Gift Card", "Concert Tickets", "VIP Experience"]
    prize = random.choice(prizes)
    print(f"Congratulations! You won a {prize} for participating!")

# Countdown timer
def bid_with_time_limit():
    print("You have 10 seconds to place your bid!")
    start_time = time.time()
    bid = None

    while time.time() - start_time < 10:
        if bid is None:
            bid = input("Enter your bid: $")
            if bid.isdigit():
                return int(bid)

    print("Time's up!")
    return 0

# Main auction loop with leaderboard and random prizes
# For storing name and bid
collection = {}
should_add = True

while should_add:
    name = input("What is your name?: ")
    bid = bid_with_time_limit()
    if bid > 0:
        collection[name] = bid
        print(f"{name} placed a bid of ${bid}")
    else:
        print(f"{name}, no bid placed due to timeout!")
    
    show_leaderboard(collection)

    new_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if new_bidders == "no":
        should_add = False
        highest_bid(collection)
    elif new_bidders == "yes":
        clear_screen()
    else:
        print("Invalid input! Please type 'yes' or 'no'.")
