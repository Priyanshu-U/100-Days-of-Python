
import random# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
lengtha=len(names);
payer=random.randint(0,lengtha-1)
print(f"{names[payer]} will play the bill")
#Write your code below this line 👇



