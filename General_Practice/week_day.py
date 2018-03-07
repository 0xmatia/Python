from calendar import weekday

date = input("Enter a date: ")

day = int(date[:2])
month = int(date[3:5])
year = int(date[6:10])

in_week = weekday(year, month, day)

if in_week == 0:
    print("Monday")
elif in_week == 1:
    print("Tuesday")
elif in_week == 2:
    print("Wednesday")
elif in_week == 3:
    print("Thursday")
elif in_week == 4:
    print("Friday")
elif in_week == 5:
    print("Saturday")
elif in_week == 6:
    print("Sunday")
