#importing library
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#7-SEGMENT DISPLAY LED setup
GPIO.setup(26, GPIO.OUT) #BOTTOM LEFT
GPIO.setup(19, GPIO.OUT) #BOTTOM
GPIO.setup(13, GPIO.OUT) #BOTTOM RIGHT
GPIO.setup(6, GPIO.OUT) #MID
GPIO.setup(5, GPIO.OUT) #TOP LEFT
GPIO.setup(0, GPIO.OUT) #TOP
GPIO.setup(11, GPIO.OUT) #TOP RIGHT

#7-SEGMENT Setup phase
GPIO.output(26, False)
GPIO.output(19, False)
GPIO.output(13, False)
GPIO.output(6, False)
GPIO.output(5, False)
GPIO.output(0, False)
GPIO.output(11, False)

time.sleep(1)

#9
GPIO.output(13, True)
GPIO.output(6, True)
GPIO.output(5, True)
GPIO.output(0, True)
GPIO.output(11, True)
time.sleep(1)
#8
GPIO.output(26, True)
GPIO.output(19, True)
time.sleep(1)
#7
GPIO.output(6, False)
GPIO.output(5, False)
GPIO.output(26, False)
GPIO.output(19, False)
time.sleep(1)
#6
GPIO.output(6, True)
GPIO.output(5, True)
GPIO.output(26, True)
GPIO.output(19, True)
GPIO.output(0, True)
GPIO.output(11, False)
time.sleep(1)
#5
GPIO.output(26, False)
time.sleep(1)
#4
GPIO.output(19, False)
GPIO.output(0, False)
GPIO.output(11, True)
time.sleep(1)
#3
GPIO.output(5, False)
GPIO.output(19, True)
GPIO.output(0, True)
time.sleep(1)
#2
GPIO.output(26, True)
GPIO.output(13, False)
time.sleep(1)
#1
GPIO.output(13, True)
GPIO.output(19, False)
GPIO.output(6, False)
GPIO.output(0, False)
GPIO.output(26, False)
time.sleep(1)
#0
GPIO.output(5, True)
GPIO.output(0, True)
GPIO.output(11, True)
GPIO.output(26, True)
GPIO.output(19, True)
time.sleep(2)

GPIO.cleanup()