# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
price =0
#Write your code below this line 👇
if size =="S":
    price=15
elif size =="M":
    price=20
elif size =="L":
    price=25

if add_pepperoni =="Y" and size =="S":
    price +=2
elif add_pepperoni =="Y" and size =="M" and size=="L":
    price +=3

if extra_cheese =="Y":
    price +=1
print (f"You should pay {price}")