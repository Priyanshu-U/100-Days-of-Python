print("Welcome to Python Pizza Deliveries")
size= input("What size pizza do you want? S,M,L \n")
peperoni=input("Do you want perperoni? Y,N \n")
cheese=input("Do you want extra cheese? Y,N \n")

bill=0
if size=='S':
    bill+=15
elif size=='M':
    bill+=20
elif size=='L':
    bill+=25
    
if peperoni=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3
if cheese=='Y':
    bill+=1
print(f"Your bill is {bill}")
            
