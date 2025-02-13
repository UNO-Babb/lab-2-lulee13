#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  

  #TODO:
  #Ask user for hours
  hoursAhead = input("Input hours ahead: ")

  #Ask user for minutes
  minutesAhead = input("Input minutes ahead: ")

  #Calculate the time after the user-supplied time has passed.
  
  futureMinutes = (int(currentMinute) + int(minutesAhead)) % 60
  futureHour = (int(currentHour) + int(hoursAhead) + (int(currentMinute + int(minutesAhead)) // 60)) % 24

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  if futureHour > 9 and futureMinutes > 9:      #I chose to make myself miserable and add a leading zero to the hours too. 
    print(str(futureHour) + ":" + str(futureMinutes) + " GMT")
  if futureHour < 10 and futureMinutes > 9:
    print("0" + str(futureHour) + ":" + str(futureMinutes) + " GMT")
  if futureHour > 9 and futureMinutes < 10:
    print(str(futureHour) + ":0" + str(futureMinutes) + " GMT")
  if futureHour < 10 and futureMinutes < 10:
    print("0" + str(futureHour) + ":0" + str(futureMinutes) + " GMT")


if __name__ == '__main__':
  main()
