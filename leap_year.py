leapYear = int(input(" Enter the year to be checked for leap year"))

if leapYear%4==0 and (leapYear%100 !=0 or leapYear%400==0):
    print(leapYear, "is a Leap Year")
else:
    print(leapYear,"is not a Leap Year")