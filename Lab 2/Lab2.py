#Seconds to Days, Hours, minutes and seconds
#By Chris Grant
#Lab 2

time = int(input("Enter the number of seconds to convert: "))

day = 60*60*24
hour = 60*60
minute = 60

days = time // day
time -= days*day

hours = time // hour
time -= hours *hour

minutes = time // minute
time -= minutes * minute;

print("{0:} days, {1:} hours, {2:} minutes, and {3:} seconds ".format(days,hours,minutes,time))