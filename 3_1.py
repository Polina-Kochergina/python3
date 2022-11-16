import time
print(time.localtime())

time = time.localtime()

if time[6] > 5:
    print("relax!!!")
else:
    finish = (34200+5700, 34200+2*5700+600, 34200+3*5700+600*2+40*60, 34200+4*5700+600*3+40*60)
    now_s = time[3]*3600 + time[4]*60 + time[5]
    
    if time[3]*3600 + time[4]*60 + time[5] < 34200:
        print("classes have not started yet")
    elif time[3]*3600 + time[4]*60 + time[5] > 61200:
        print("classes are over!")
    elif (time[3]*3600 + time[4]*60 + time[5] < 34200+5400+600) and (time[3]*3600 + time[4]*60 + time[5] > 34200+5400):
        print("Break time!")
    elif (time[3]*3600 + time[4]*60 + time[5] < 34200+2*5400+60*50) and (time[3]*3600 + time[4]*60 + time[5] > 34200+2*5400):
        print("Break time!")
    elif (time[3]*3600 + time[4]*60 + time[5] < 34200+3*5400+600) and (time[3]*3600 + time[4]*60 + time[5] > 34200+3*5400):
        print("Break time!")
    else:
        a = []
        for i in range(len(finish)):
            if finish[i]-now_s>0:
                a.append(finish[i]-now_s)

        print(f"Until the end of the lesson {int(min(a)/60)} minutes")

