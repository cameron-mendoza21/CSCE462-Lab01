#importing library
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#BUTTON setup
GPIO.setup(9, GPIO.IN) #Button Input

#RBG LED 2 setup [Car Light]
GPIO.setup(21, GPIO.OUT) #RED
GPIO.setup(20, GPIO.OUT) #GREEN
GPIO.setup(16, GPIO.OUT) #BLUE

#RGB LED 1 setup [People Light]
GPIO.setup(12, GPIO.OUT) #RED
GPIO.setup(1, GPIO.OUT) #GREEN
GPIO.setup(7, GPIO.OUT) #BLUE

#LED Setup phase
GPIO.output(21, True)
GPIO.output(20, False)
GPIO.output(16, False)

#GPIO.output(12, True)
#GPIO.output(1, False)
#GPIO.output(7, False)

time.sleep(1)

while True:
    if not GPIO.input(9):
        GPIO.output(21,False)
    else:
        GPIO.output(21,True)
    time.sleep(0.1)