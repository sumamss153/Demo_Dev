import pandas
import os
import time

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File not Found!!!")
    time.sleep(10)
