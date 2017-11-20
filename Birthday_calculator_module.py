# Import
import time
from datetime import date, datetime
import calendar
from dateutil.relativedelta import relativedelta
import os, time

#Function
def dotprint():
    print ' '

def dotprint2():
    dotprint()
    dotprint()

def add_years(d, years):
    new_year = d.year + years
    try:
        return d.replace(year=new_year)
    except ValueError:
        if (d.month == 2 and d.day == 29 and # leap day
            isleap(d.year) and not isleap(new_year)):
            return d.replace(year=new_year, day=28)
        raise

def wait():
    time.sleep(1)

time.strftime('%X %x %Z')
os.environ['TZ'] = 'US/Pacific'
time.tzset()
time.strftime('%X %x %Z')

# MAIN
print ('######################################################################')
print ('###                   This is a Date Calculator                    ###')
print ('###                 Created for Byte Lab Hackathon                 ###')
print ('######################################################################')

time.sleep(2)

dotprint2()
dotprint2()

print ('This is a program that can calculate what day of the week your birthday will be 1-99 years into the future ')

time.sleep(2)
dotprint2()

my_date = date.today()
calendar.day_name[my_date.weekday()]

print "Current date {}, {}".format(calendar.day_name[my_date.weekday()], my_date.strftime('%m/%d/%Y'))
time.sleep(0.8)

birthday = raw_input ('What is your birthday(m/d/yyyy)?')
dotprint()

g = raw_input ('How many years in advance would you like to look at?(1-99)')
dotprint()

birthday_date = datetime.strptime(birthday, '%m/%d/%Y').date()
print "Your birthday was {}, {}".format(calendar.day_name[birthday_date.weekday()], birthday_date.strftime ('%m/%d/%Y'))
dotprint()
wait()

difference_in_years = relativedelta(my_date, birthday_date).years
new_bday = date(birthday_date.year+difference_in_years, birthday_date.month, birthday_date.day)

print 'Your most recent birthday was {}, {}'.format(calendar.day_name[new_bday.weekday()],new_bday.strftime ('%m/%d/%Y'))
dotprint()
wait()

print 'The day your birthday will be on for the next {} years is:'.format(g)

for x in range(1, int(float(g)) + 1):
    time.sleep(0.1)
    new_byear = date(new_bday.year + x, new_bday.month, new_bday.day)
    print "{:>2}. {}, {}" .format (x, new_byear.strftime('%Y/%d/%m'), calendar.day_name[new_byear.weekday()])

leap_year_count = 0

for v in range(1, int(difference_in_years)):
    try:
      t = date(new_bday.year + v, 2, 29)
      leap_year_count += 1 
    except:
      pass


time.sleep(5)
dotprint()
if raw_input("Would you like to see some other information we know about you know? yes? or no?").lower() == 'yes':
  dotprint()
  print 'Your age is: {} years old'.format (difference_in_years)
  dotprint()
  wait()
  d0 = date(birthday_date.year, birthday_date.month, birthday_date.day)
  d1 = date(my_date.year, my_date.month, my_date.day)
  delta = d1 - d0
  print 'You have been alive for: {} days'.format(delta.days)
  dotprint()
  wait()
  
  average_month_in_days = 365 / 12.0
    
  print 'You have been alive for about: {} months'.format(int (delta.days / average_month_in_days))
  wait()
  
  dotprint()
  print 'You have seen: {} leap years'.format(leap_year_count)
  wait()
  print 'This is some of the information we could show you. I hope you found this program useful.'
else:
  print 'There is nothing else this prgram can provide for you. I hope you found this program useful.'


