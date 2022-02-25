import os
def add(n1,n2):
    return (n1+n2)
def sub(n1,n2):
    return (n1-n2)
def multiply(n1,n2):
    return(n1*n2)
def division(n1,n2):
    return(n1/n2)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":division
}

while_flag=True
n1=float(input("Enter Number 1: "))

while(while_flag):
    for operation_symbol in operations:
        print(operation_symbol)
    operation=input("Select the desired operation: ")
    n2=float(input("Enter Number 2: "))
    results=operations[operation](n1,n2)
    print(f"Results to your operations are {results}")
    continue_flag=input("Would you like to continue?(y/n): ")
    if continue_flag=='y':
        reset_flag=input("Carry Value or Reser? (c/r): ")
        if continue_flag=='y' and reset_flag=='c':
            n1=results
        elif continue_flag=='y' and reset_flag=='r':
            cls()
            n1=float(input("Enter Number 1: "))
    else:
        while_flag=False
        print(f"Results to your operations are {results}")
   
