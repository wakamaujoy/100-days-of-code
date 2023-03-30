def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "True"
            else:
                return "False"
        else:
            return "True"
    else:
        return "False"


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    status = is_leap(year)
    month_index = month - 1

    if status == "False":
        return month_days[month_index]
    elif status == "True" and month_index == 1:
        return 29
    elif status == "True":
        return month_days[month_index]

    # if status =="True": and month_index ==1:


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)











