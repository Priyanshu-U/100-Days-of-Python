# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
name11=name1.lower()
name21=name2.lower()
score1=0
score2=0
score1+=name11.count("t")
score1+=name11.count("r")
score1+=name11.count("u")
score1+=name11.count("e")
score2+=name21.count("l")
score2+=name21.count("o")
score2+=name21.count("v")
score2+=name21.count("e")

final_score=score1*10+score2
if final_score<10 or final_score>90 :
    print("you go together like coke and mentos")
elif final_score>=40 and final_score<=50:
    print("you're okay together")
else:
    print(f"your score is {final_score}")
#Write your code below this line 👇


