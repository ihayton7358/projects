import RPi.GPIO as GPIO, time

pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

count = 0
current_state = 0
previous_state = 0

while True:
    current_state = GPIO.input(pin)

    if previous_state == GPIO.HIGH and current_state == GPIO.LOW:
        count += 1
        print (count)

    previous_state = current_state
    time.sleep(0.01)
    
    
    
