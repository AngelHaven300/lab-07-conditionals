hour = input("What trime is it right now? (in military time)")
if hour > 0 and hour < 5:
    print("Its early. You should be sleeping!")
elif hour > 6 and hour < 7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
elif hour > 8 and hour < 9:
    print("Time to go to work.")
elif hour > 10 and hour < 12:
    print("You should be working!")
elif hour > 12 and hour < 13:
    print("Take your lunch break!")
elif hour > 13 and hour < 17:
    print("Do you feel that afternoon lull?")
elif hour > 17 and hour < 19:
    print("Time to hit the gym…")
elif hour > 19 and hour < 21:
    print("Gotta eat that dinner.")
elif hour > 21 and hour < 23:
    print("Get that SLEEP. And rePEAT!")
else:
    print("You didnt say an acceptable value! (0-23)")