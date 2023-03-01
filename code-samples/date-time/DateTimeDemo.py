from datetime import datetime
from datetime import date
from datetime import time

currentDate = datetime.now()
print(currentDate)

testDate = date(2023, 3, 1)
print(testDate)

today = date.today()
print("Today's date", today)
print("Extracted year ", today.year)
print("Extracted month ", today.month)
print("Extracted day ", today.day)

print("Time from current date ", currentDate.time())
t = currentDate.time()

print("Hour ", t.hour)
print("Minutes ", t.minute)
print("Seconds ", t.second)

#  The method to control the format of datetime is strftime()
formattedDate = currentDate.strftime("%d/%m/%Y %H:%M:%S")
print("Formatted date is ", formattedDate)

customDateTime = datetime(year=2023, month=1, day=1, hour=00, minute=00, second=00)
print("1st Jan 2023 datetime format ", customDateTime)

timeDifference = currentDate - customDateTime
print("Time difference is ", timeDifference)


