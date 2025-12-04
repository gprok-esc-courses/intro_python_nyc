# Simulation of temperature sensor 
# who writes measurements into a file
# measeurements assumed 0 to 40 degrees
# if less than 10 indicate LOW, more than 30 HIGH, else OK

import random 
from datetime import datetime
from time import sleep


for i in range(10):
    temperature = random.random()
    t = temperature * 40
    dt = datetime.now()
    status = "OK"
    if t < 10:
        status = "LOW"
    elif t > 30:
        status = "HIGH"
    line = f"{t},{dt},{status}\n"
    file = open("temperature.csv", "a")
    file.write(line)
    file.close()
    sleep(5)
    
