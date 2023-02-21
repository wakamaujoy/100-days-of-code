# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
match = lower_case_name1 + lower_case_name2
t= match.count("t")
r= match.count("r")
u= match.count("u")
e= match.count("e")
l= match.count("l")
o= match.count("o")
v= match.count("v")
e= match.count("e")
first_value =int(t+r+u+e)
last_value = int(l+o+v+e)
print(f"Your love score is {first_value}{last_value}")
