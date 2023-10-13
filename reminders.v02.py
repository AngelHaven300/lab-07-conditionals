import datetime
now = datetime.datetime.now()
print(now.now)


if now > 0 and now < 5:
    print("Its early. You should be sleeping!")
elif now > 6 and now < 7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif now > 8 and now < 9:
    print("Time to go to work.")
elif now > 10 and now < 12:
    print("You should be working!")
elif now > 12 and now < 13:
    print("Take your lunch break!")
elif now > 13 and now < 17:
    print("Do you feel that afternoon lull?")
elif now > 17 and now < 19:
    print("Time to hit the gym…")
elif now > 19 and now < 21:
    print("Gotta eat that dinner.")
elif now > 21 and now < 23:
    print("Get that SLEEP. And rePEAT!")
else:
    print("You didnt say an acceptable value! (0-23)")