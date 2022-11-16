import os
import time
import datetime
path1 = os.getcwd()

def scan(path):
    while True: 
        dir1 = os.listdir(path)
        d1 = set(dir1)
        time.sleep(1)
        dir2 = os.listdir(path)
        d2 = set(dir2)
        if d1^d2 != set():
            if d2.difference(d1) != set():
                print(datetime.datetime.today(), d2.difference(d1), "was created")
            elif d1.difference(d2) != set():
                print(datetime.datetime.today(), d1.difference(d2), "was removed")



scan(path1)