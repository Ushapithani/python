def leap_years_in_range(start, end):
    leap_years = []
    for year in range(start, end + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years.append(year)
    return leap_years


start = int(input("Enter the starting year: "))
end = int(input("Enter the ending year: "))

result = leap_years_in_range(start, end)

if result:
    print(f"Leap years between {start} and {end}: {result}")
else:
    print(f"No leap years found in the given range.")


