import time, math, RPi.GPIO as GPIO
pin = 17
count = 0

def spin():
    global count
    count+=1
    print(count)

def calcspeed():
    radius = 9
    time = 5
    CmS = ((math.pi*radius)*count)/time
    KmS = (CmS/100000)*3600
    return KmH

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.PUD_UP)
GPIO.add_event_detect_(pin, GPIO.FALLING, callback = spin, bouncetime = 300)

while True:
    count = 0
    time.sleep(5)
    windspeed = calcspeed()
    print (windspeed)
