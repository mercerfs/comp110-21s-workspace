"""A vaccination calculator."""

__author__ = "730409119"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
today: datetime = datetime.today()
today.strftime("%B %d, %Y")
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
tomorrow.strftime("%B %d, %Y")
fortnight: timedelta = timedelta(7 + 7)
future: datetime = today + fortnight

population: int= int(input("Population:"))
doses_administered: int=int(input("Doses Administered:"))
doses_per_day: int=int(input("Doses Per Day:"))
target_percent_vaccinated: int=int(input("Target Percent Vaccinated:"))

target_people_vaccinated: int= population*(.01*target_percent_vaccinated)
total_doses_needed: int= (target_people_vaccinated*2)-(doses_administered)
days: int= total_doses_needed/ doses_per_day

population*(.01*target_percent_vaccinated) == target_people_vaccinated
(target_people_vaccinated*2)-(doses_administered) == total_doses_needed
total_doses_needed/ doses_per_day== days

round(days,0)
round(target_people_vaccinated)

end: today + (one_day*days)
date_achieved: str=end.strftime("%B %d, %Y")

print("We will reach " + str(target_percent_vaccinated) + "% vaccination in " + str(days) +" days which falls on " + str(date_achieved) 
+ ".")