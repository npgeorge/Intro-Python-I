"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
 
Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
from datetime import date

def get_calendar():
  print('Number of arguments:', len(sys.argv), 'arguments.')
  print('Argument List:', str(sys.argv))

  # this grabs the arguments passed in after "python3" in the cmd line
  date_args = sys.argv

  # --Current Day--
  # use datetime to get current day
  today = date.today()
  # turn into string to slice it
  today = str(today)
  # slice and make integers to pass into formatmonth
  current_year = int(today[:4])
  current_month = int(today[5:7])

  # setting the calendar to begin on Sunday
  c = calendar.TextCalendar(calendar.SUNDAY)

  # if/else statement
  if len(date_args) == 1:
    user_cal = c.formatmonth(current_year,current_month)
    print(user_cal)
  elif len(date_args) == 2:
    # assume they passed in a month
    # this will grab the first argument passed in
    # translate from string to integer
    month_arg = int(date_args[1])
    # this places the first argument passed as a month
    user_cal = c.formatmonth(current_year, month_arg)
    print(user_cal)
  elif len(date_args) == 3:
    # this grabs the first two arguments, month and year
    # translates them from strings to integers
    month_arg = int(date_args[1])
    year_arg = int(date_args[2])
    # create calendar
    user_cal = c.formatmonth(year_arg,month_arg)
    print(user_cal)
  else:
    print("Please follow this syntax: `python3 14_cal.py [month] [year]`")

get_calendar()