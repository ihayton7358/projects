
import time, math, RPi.GPIO as GPIO

pin = 17
count = 0

pin_2 = 27
count_2 = 0

####wind speed
###orange wires

def spin(channel):
    global count
    count+=1
    print(count)

def calcspeed():
    radius = 9
    time = 5
    CmS = ((math.pi*radius)*count)/time
    KmH = (CmS/100000)*3600
    return KmH

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback = spin, bouncetime = 300)

while True:
    count = 0
    time.sleep(5) #pauses for 5 seconds
    windspeed = calcspeed() #windspeed is equal to what calcspeed returned 
    print (windspeed)   #prints the windspeed

####### annemometer (rain count)
#####blue wires

def bucket_tipped(channel):
    global count_2
    count_2 += 1
    print (count_2 * 0.2794 + "millilitres of rain")

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_2, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin_2, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

input = ("Press enter to exit...")
