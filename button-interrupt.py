#importing library
import time
import RPi.GPIO as GPIO
from blink import blink
from countdown import countdown

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

#LED Setup phase
GPIO.output(21, False)
GPIO.output(20, True)
GPIO.output(8, False)

GPIO.output(12, True)
GPIO.output(1, False)
GPIO.output(7, False)

GPIO.output(26, False)
GPIO.output(19, False)
GPIO.output(13, False)
GPIO.output(6, False)
GPIO.output(5, False)
GPIO.output(0, False)
GPIO.output(11, False)

#By DEFAULT: Traffic Light 2 should stay GREEN, Traffic Light 1 should stay RED

#System requirements: 
#a. When the button has not been pressed, traffic light 2 stay green 
#b. When the button is pressed, traffic light 2 turns to blue blink 3 times then turns 
#red. 
#c. When Traffic light 2 turns red, traffic light 1 becomes green and the countdown 
#panel begins to count down from 9 to 0, in seconds. (In the real world it would be 
#longer) 
#d. When countdown reaches 4, the traffic light 1 flashes with blue light until time 0. 
#e. When countdown reaches 0, the traffic light 1 becomes red, traffic light 2 
#becomes green. 
#f. When the button is pressed once there will be a 20 seconds cooldown to be able 
#to make another valid press. 

#event handler
def handler(self):
    GPIO.remove_event_detect(9) #to prevent queued events to happen
    #button has been press, its on a 20 second cooldown starting now
    blink()
    countdown()
    #sleep the code for 11 seconds before button can be used again
    time.sleep(11)
    GPIO.add_event_detect(9, GPIO.FALLING, handler) #re-enabling the interrupts


GPIO.add_event_detect(9, GPIO.FALLING, handler)


while True:
    time.sleep(1e6)

#clean up
#GPIO.cleanup()