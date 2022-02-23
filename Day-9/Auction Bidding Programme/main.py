import os
def enter_bid(name,amount):
    global bids
    bids[name]=amount

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

loop_flag=True
bids={}
while loop_flag:
    print("Welcome to the secret auction program.\n")
    bidder_name=input("What is your name?: ")
    bid_amount=input("What's yout bid?: ")
    enter_bid(bidder_name,bid_amount)
    other_bidders=input("Are there other bidders? Type 'yes or 'no' ")
    while (other_bidders!="yes" and other_bidders!="no"):
        other_bidders=input("Unexpected Input please enter 'yes' or 'no'")
    if other_bidders=='yes':
        cls()
    else:
        cls()
        loop_flag=False
max_bid=0
max_bidder=None
for key in bids:
    if int(bids[key])>max_bid:
        max_bid=bids[key]
        max_bidder=key
print(f"The winner of the bid is {max_bidder} and the winning bid is {max_bid}")
