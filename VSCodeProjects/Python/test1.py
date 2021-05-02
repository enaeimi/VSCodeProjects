
# coding: utf-8
import pyodbc

conn    = pyodbc.connect('Driver={SQL SERVER};SERVER=LT-SOD00006364;DATABASE=AdventureWorks2017;TRUSTED_CONNECTION=yes;')
cursor  = conn.cursor()
cursor.execute('USE [AdventureWorks2017]; Selecte * from person.person')
for row in cursor:
    print(row)

    

from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time] + " time. ")
        break
else:
    print('Unknown, AFK or sleeping!')


