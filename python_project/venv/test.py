import datetime

current_date = datetime.date.today()
name = raw_input("What's your name?")

print "Today is" , current_date.strftime('%d-%m-%Y')
print "Hello,", name

