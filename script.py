import datetime, time
now = datetime.datetime.now().strftime("%H:%M")
f = open("time.txt", "w")
f.write(now)
