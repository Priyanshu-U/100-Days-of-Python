def prime_checker(number):
    flag=True
    for i in range(2,number):
        if number%i==0:
            flag=False

    if flag==True:
            print(f"{number} is a prime")
    else:
            print(f"{number} is not a prime")
    


n = int(input("Check this number: "))
prime_checker(number=n)

