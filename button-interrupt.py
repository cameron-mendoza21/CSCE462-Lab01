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
GPIO.output(21, False)
GPIO.output(20, True)
GPIO.output(16, False)

GPIO.output(12, True)
GPIO.output(1, False)
GPIO.output(7, False)

time.sleep(2)

def handle_input_button(channel):
    # Part b
    for i in range(3):
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(16, GPIO.LOW)
        time.sleep(0.1)
    GPIO.output(21, GPIO.HIGH)

    time.sleep(20)


GPIO.add_event_detect(9, GPIO.FALLING, callback=handle_input_button, bouncetime=300)

def main():
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.1)

try:
    while True:
        main()
except KeyboardInterrupt:
    GPIO.cleanup()