#Import

import time
from datetime import date, datetime
import calendar
from dateutil.relativedelta import relativedelta
import os, time


#Function and Class

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
    time.sleep(0.1)

def waithalf():
    time.sleep(0.5)

def wait1():
    time.sleep(1)

def wait2():
    time.sleep(2)

def dotprint1():
    time.sleep(0.1)
    print ' '
    time.sleep(0.1)

def dotprint2():
    print ' '
    time.sleep(0.2)
    print ' '

def convert_timezone():
  time.strftime('%X %x %Z')
  os.environ['TZ'] = 'US/Pacific'
  time.tzset()
  time.strftime('%X %x %Z')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#Main

convert_timezone()
my_date = date.today()
calendar.day_name[my_date.weekday()]

print '               ***********************************'
print '               ***                             ***'
print color.BOLD + '               ***          LEVIATHAN          ***' + color.END
print '               ***                             ***'
print '               ***********************************'
wait2()
dotprint1()

print 'Leviathan: {}, {}, {}'.format(calendar.day_name[my_date.weekday()], my_date.strftime('%m/%d/%Y'), time.strftime("%I:%M:%S"))
waithalf()
print '           1 program loaded'

wait2()
dotprint2()

print 'Leviathan: Welcome to this Master Program created by Rafael Cenzano'
wait2()
dotprint2()

print 'Leviathan: Before we start there are a few things we need to know about you'
wait2()
dotprint2()

birthday = raw_input ('Leviathan: What is your birthday(m/d/yyyy)?')
birthday_date = datetime.strptime(birthday, '%m/%d/%Y').date()
difference_in_years = relativedelta(my_date, birthday_date).years
new_bday = date(birthday_date.year+difference_in_years, birthday_date.month, birthday_date.day)
d0 = date(birthday_date.year, birthday_date.month, birthday_date.day)
d1 = date(my_date.year, my_date.month, my_date.day)
delta = d1 - d0
def birth_day_calculator():
  print ('######################################################################')
  print ('###                   This is a Date Calculator                    ###')
  print ('###                 Created for Byte Lab Hackathon                 ###')
  print ('######################################################################')
  wait2()
  dotprint2()
  
  print 'Leviathan: This is a program that can calculate what day of the week your birthday will be 1-99 years into the future '
  wait1()
  dotprint2()
    
  g = raw_input ('Leviathan: How many years in advance would you like to look at?(1-99)')
  dotprint2()
    
  print 'Leviathan: Your birthday was {}, {}'.format(calendar.day_name[birthday_date.weekday()], birthday_date.strftime ('%m/%d/%Y'))
  dotprint2()
  wait1()
    
  print 'Leviathan: Your most recent birthday was {}, {}'.format(calendar.day_name[new_bday.weekday()],new_bday.strftime ('%m/%d/%Y'))
  dotprint2()
  waithalf()
    
  print 'Leviathan: The day your birthday will be on for the next {} years is:'.format(g)
  waithalf()
    
  for x in range(1, int(float(g)) + 1):
    wait()
    new_byear = date(new_bday.year + x, new_bday.month, new_bday.day)
    print "{:>2}. {}, {}" .format (x, new_byear.strftime('%Y/%d/%m'), calendar.day_name[new_byear.weekday()])
  wait2()
  dotprint2()
  
  leap_year_count = 0

  for v in range(1, int(difference_in_years)):
    try:
      t = date(new_bday.year + v, 2, 29)
      leap_year_count += 1 
    except:
      pass

  
  if raw_input('Leviathan: Would you like to see some other information we know about you know? yes? or no?').lower() == 'yes':
    dotprint1()
      
    print 'Leviathan: Your age is: {} years old'.format (difference_in_years)
    dotprint1()
    wait1()
      
    print 'Leviathan: You have been alive for: {} days'.format(delta.days)
    dotprint1()
    wait1()
    
    average_month_in_days = 365 / 12.0
    
    print 'You have been alive for about: {} months'.format(int (delta.days / average_month_in_days))
    dotprint1()
    wait1()
    
    print 'You have seen: {} leap years'.format(leap_year_count)
    dotprint1()
    wait1()
    
    if raw_input('Leviathan: That is all the Birth-Day-Calculator can provide would you like to try a different program? yes? or no?').lower() == 'yes':
          print 'insert new programs here'
          
    else:
      print 'Leviathan: Rerun program to use master program again'
      
  else:
      dotprint1()
      if raw_input('Leviathan: That is all the Birth-Day-Calculator can provide would you like to try a different program? yes? or no?').lower() == 'yes':
        dotprint2()
        print 'insert new programs here'
      
      else:
        dotprint2()
        print 'Leviathan: Rerun program to use master program again'
dotprint2()

waithalf()
if raw_input('Leviathan: Would you like to run Birth-Day-Calculator? yes? or no?').lower() == 'yes':
    
    dotprint1()
    print 'Leviathan: Loading Birth-Day-Calculator'
    count = 1
    while (count < 101):
        print 'Loading: {}%' .format (count)
        time.sleep(0.03)
        count = count + 1
  
    dotprint2()
    
    birth_day_calculator()
  
else:
  dotprint2()
  print 'insert new programs here'
