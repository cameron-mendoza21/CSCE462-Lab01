#importing library
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#RBG LED 2 setup
GPIO.setup(21, GPIO.OUT) #RED
GPIO.setup(20, GPIO.OUT) #GREEN
GPIO.setup(16, GPIO.OUT) #BLUE

#RGB LED 1 setup
GPIO.setup(12, GPIO.OUT) #RED
GPIO.setup(1, GPIO.OUT) #GREEN
GPIO.setup(7, GPIO.OUT) #BLUE

#LED Setup phase
GPIO.output(21, False)
GPIO.output(20, True)
GPIO.output(16, False)

GPIO.output(12, True)
GPIO.output(1, False)
GPIO.output(7, False)

time.sleep(2)

#Code for LED to blink blue 3 times, turn red, and other LED Turns Green
GPIO.output(20, False)
GPIO.output(16, True)
time.sleep(0.5)
GPIO.output(16, False)
time.sleep(0.5)
GPIO.output(16, True)
time.sleep(0.5)
GPIO.output(16, False)
time.sleep(0.5)
GPIO.output(16, True)
time.sleep(0.5)
GPIO.output(16, False)
time.sleep(0.5)
GPIO.output(16, False)
GPIO.output(21, True)

GPIO.output(12, True)
GPIO.output(1, False)

GPIO.output(12, False)
GPIO.output(1, True)

time.sleep(3)

GPIO.cleanup()