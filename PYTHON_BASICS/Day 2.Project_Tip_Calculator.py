print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10,12 or 15 "))
no_of_people = int(input("How many people should split the bill?"))
# if percentage_tip ==12:
#     tip_to_give = 1.12 * total_bill
# elif percentage_tip ==10:
#     tip_to_give = 1.10 *total_bill
# elif percentage_tip ==15:
#     tip_to_give = 1.15 *total_bill
# bill_per_person =round(tip_to_give/no_of_people)
# print(f"Each person should pay:{bill_per_person}")

bill_with_tip = (percentage_tip/100) *total_bill
overall_bill = bill_with_tip + total_bill
bill_per_person =total_bill/no_of_people
print(f"Each person should pay:{bill_per_person}")