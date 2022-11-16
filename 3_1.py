import datetime as dt


def timetable(now):
    if dt.datetime.today().weekday() > 3:
        print("relax!!!")
    else:
        finish = (dt.timedelta(hours=11, minutes=5), dt.timedelta(hours=12, minutes=50),
         dt.timedelta(hours=15, minutes=15), dt.timedelta(hours=17, minutes=0))
        n = dt.timedelta(hours = now.hour, minutes = now.minute)
        
        if now <= dt.time(9,30):
            print("classes have not started yet")
        elif now > dt.time(17,00):
            print("classes are over!")
        elif (now > dt.time(11,5)) and (now < dt.time(11,15)):
            print("Break time!")
        elif (now > dt.time(12,50)) and (now < dt.time(13,40)):
            print("Break time!")
        elif (now > dt.time(15,15)) and (now < dt.time(15,25)):
            print("Break time!")
        elif (now > dt.time(17,0)) and (now < dt.time(17,10)):
            print("Break time!")
        else:
            a = []
            for i in range(len(finish)):
                if finish[i].seconds - n.seconds > 0:
                    a.append(finish[i] - n)
            print(f"Until the end of the lesson {min(a)} minutes")


timetable(dt.datetime.now().time())