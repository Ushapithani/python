def leap_year(year):
    leap=False
    if (year%400 and year!=0) or (year%400==0):
        leap=True
    else:
        leap=False
year=int(input())
print(year)