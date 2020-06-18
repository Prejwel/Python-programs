# %A -> to display the full name of Day

import datetime

y = int(input("Enter the year"))
m = int(input("Enter the month"))
d = int(input("enter the date"))
dtm = datetime.date(y,m,d)
print(dtm.strftime("%A %B %d"))

gvr=datetime.date(1956,1,31)
print(dtm.year)
print(dtm.month)
print(dtm.day)


