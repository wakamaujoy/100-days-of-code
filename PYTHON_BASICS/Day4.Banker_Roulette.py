import random

name_string =input("Give everybody's name sepatared by a comma ")
print(name_string)
names = name_string.split(",")
print(names)
# length_of_names = len(names)
# print(length_of_names)
# random_choice =random.randint(0,length_of_names-1)
# print(random_choice)
# payer = names[random_choice]
# print(f"{payer} will pay the bill")

random_name = random.choice(names)
print(f"{random_name} pays")