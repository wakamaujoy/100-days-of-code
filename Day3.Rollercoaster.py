print("Welcome to the rollercoaster ride!!!")
height = int(input("Enter your height in cm  "))
if height >= 120:
    print("You can enjoy the ride")
    age = int(input("How old are you?"))
    if age <12:
        price =5
        print("Child tickets are $5")
    elif age <18:
        price =7
        print("Youth tickets are $7")
    else:
        price =12
        print("Adult tickets are $12")
    photo = input("Would you like a photo taken?  Y or N")
    if photo == "Y":
        price +=3
    print(f"You should pay ${price}")
else:
    print("Sorry you have to grow a bit taller before you can ride")