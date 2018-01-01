# Command line calendar
from time import sleep, strftime
user = raw_input('Welcome to your own personal calendar. \nPlease enter your first name: ')

calendar = {}

def welcome():
  print 'Welcome ' + user + '.'
  print 'The Calendar is now opening up.'
  sleep(1)
  print 'Today\'s date is: ' + strftime('%A %B %d, %Y')
  print 'The current time is: ' + strftime('%H:%M:%S')
  sleep(1)
  print 'What would you like to do?'

def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input('A to Add \nU to Update \nV to View \nD to Delete \nX to Exit: ')
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print 'The calendar is empty.'
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input('What date? ')
      update = raw_input('Enter date (MM/DD/YYYY): ')
      calendar[date] = update
      print 'The update was a success!'
      print calendar
    elif user_choice == 'A':
      event = raw_input('Enter event: ')
      date = raw_input('Enter date (MM/DD/YYYY): ')
      if (len(date) > 10 or int(date[6:]) < int(strftime('%Y'))):
        print 'The date you entered is invalid. Please enter a date in the future, in the format \'MM/DD/YYYY\''
        try_again = raw_input('Would you like to try again? Y for Yes, N for No ')
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        elif try_again == 'N':
          break
      else:
        calendar[date] = event
        print 'The even has been successfully added!'
        print calendar
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        'The calendar is empty.'
      else:
        event = raw_input('What event? ')
        for i in calendar.keys():
          if event == calendar[i]:
            del calendar[i]
            print 'The event has been removed successfully.'
            print calendar
          else:
            print 'Your even does not match a calendar entries.'
    elif user_choice == 'X':
      break
  
start_calendar()