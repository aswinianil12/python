day=int(input("Enter the day(1-31):"))
month=int(input("Enter the month(1-12):"))
year=int(input("Enter the year(e.g.,2024):"))
print(f"Entered date: {day:02d}-{month1:02d}-{year}")
if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print(f"the year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")