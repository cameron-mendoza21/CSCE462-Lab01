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
     #button has been press, its on a 20 second cooldown starting now

        #Code for LED to blink blue 3 times, turn red, and other LED Turns Green

        GPIO.output(20, False)
        GPIO.output(8, True)
        time.sleep(0.5)
        GPIO.output(8, False)
        time.sleep(0.5)
        GPIO.output(8, True)
        time.sleep(0.5)
        GPIO.output(8, False)
        time.sleep(0.5)
        GPIO.output(8, True)
        time.sleep(0.5)
        GPIO.output(8, False)
        time.sleep(0.5)
        GPIO.output(21, True)
        GPIO.output(12, False)
        GPIO.output(1, True)  
        
           
        #countdown
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

        #start blinking blue
        GPIO.output(1, False)
        GPIO.output(7, True)
        time.sleep(0.5)
        GPIO.output(7, False)
        time.sleep(0.5)


        #3
        GPIO.output(5, False)
        GPIO.output(19, True)
        GPIO.output(0, True)

        GPIO.output(7, True)
        time.sleep(0.5)
        GPIO.output(7, False)
        time.sleep(0.5)
        #2
        GPIO.output(26, True)
        GPIO.output(13, False)

        GPIO.output(7, True)
        time.sleep(0.5)
        GPIO.output(7, False)
        time.sleep(0.5)
        #1
        GPIO.output(13, True)
        GPIO.output(19, False)
        GPIO.output(6, False)
        GPIO.output(0, False)
        GPIO.output(26, False)

        GPIO.output(7, True)
        time.sleep(0.5)
        GPIO.output(7, False)
        time.sleep(0.5)
        #0
        GPIO.output(5, True)
        GPIO.output(0, True)
        GPIO.output(11, True)
        GPIO.output(26, True)
        GPIO.output(19, True)


        #Car light is now Green!
        GPIO.output(21,False)   
        GPIO.output(20,True)

        GPIO.output(1,False)
        GPIO.output(12,True)
        time.sleep(1)

        GPIO.output(26, False)
        GPIO.output(19, False)
        GPIO.output(13, False)
        GPIO.output(6, False)
        GPIO.output(5, False)
        GPIO.output(0, False)
        GPIO.output(11, False)

        #sleep the code for 11 seconds before button can be used again
        time.sleep(11)


GPIO.add_event_detect(9, GPIO.BOTH, handler)


while True:
    time.sleep(1e6)




    #clean up
    #GPIO.cleanup()