import time, math, RPi.GPIO as GPIO
pin = 17
pin_bucket = 27
count = 0
count_bucket = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

def spin():
    global count
    count+=1
    print(count)

def calcspeed():
    radius = 9
    time = 5
    CmS = ((math.pi*radius)*count)/time
    KmS = (CmS/100000)*3600
    return KmS


while True:
    count = 0
    time.sleep(5)
    windspeed = calcspeed()
    print (windspeed)
####


def bucket_tipped(channel):
    global count_bucket
    count_bucket+= 1
    print (count_bucket * 0.2794)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin-bucket, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin_bucket, GPIO.FALLING, callback=bucket_tipped, bouncetime = 300)

input = ("Press enter to exit...")




