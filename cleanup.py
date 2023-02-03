#importing library
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#RBG LED 1 setup Car Light
GPIO.setup(21, GPIO.OUT) #RED
GPIO.setup(20, GPIO.OUT) #GREEN
GPIO.setup(8, GPIO.OUT) #BLUE

#RGB LED 2 setup People Light
GPIO.setup(12, GPIO.OUT) #RED
GPIO.setup(1, GPIO.OUT) #GREEN
GPIO.setup(7, GPIO.OUT) #BLUE

#7-SEGMENT DISPLAY LED setup
GPIO.setup(26, GPIO.OUT) #BOTTOM LEFT
GPIO.setup(19, GPIO.OUT) #BOTTOM
GPIO.setup(13, GPIO.OUT) #BOTTOM RIGHT
GPIO.setup(6, GPIO.OUT) #MID
GPIO.setup(5, GPIO.OUT) #TOP LEFT
GPIO.setup(0, GPIO.OUT) #TOP
GPIO.setup(11, GPIO.OUT) #TOP RIGHT

#BUTTON setup
GPIO.setup(9, GPIO.IN) #Button Input

#clean-up
GPIO.cleanup()