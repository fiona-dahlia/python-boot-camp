from art import logo

keep_going = 'yes'
bids = {}
print(logo)
while keep_going == 'yes':
    name = input("What it your name: ")
    bid_amount = int(input("How much do you bid: "))
    bids[name] = bid_amount
    # print(f"The person with the highest bid is {}")
    keep_going = input("Are there any more bidders: ").lower()

print(bids)

highest_bid = 0
highest_bidder = ""
for bid_user in bids:
    auction_amount = bids[bid_user]
    print(f"name: {bid_user}, value: {auction_amount}")
    if highest_bid < auction_amount:
        highest_bid = auction_amount
        highest_bidder = bid_user

print(f"highest amount: {highest_bid} highest bidder: {highest_bidder}")

