import os

print("Welcome to the silent auction, place your bid silently....")
bidding_details = {}

end = False
while not end:
    name = input("What is your name: ")
    bid_amount = int(input("What's your bid? $"))
    bidding_details[name] = bid_amount
    question = input("Are there are any other bidders? Type 'yes' or 'no': ").lower()

    if question == 'no':
        print("\nBidding is closed and the item is sold")
        end = True
    
    elif question == 'yes':
        os.system('cls')
        
    else:
        print("\nInvalid response, please try again.")

highest_bid = 0     
bidder_name = ''    
for name, amount in bidding_details.items():
    if amount > highest_bid:
        highest_bid = amount
        bidder_name = name
        
print(f"\nThe winner is {bidder_name} with a bid of ${highest_bid}.")