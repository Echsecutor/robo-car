#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers

GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)

PMW_FREQUENCY = 1000


class Motor:
    def __init__(self, input_pin1, input_pin2, en_pin):
        self.pins = (input_pin1, input_pin2, en_pin)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        self.pmw = GPIO.PWM(en_pin, PMW_FREQUENCY)
        self.pmw.start(50)
        print("New Motor using pins " + str(self.pins))

    def forward(self):
        GPIO.output(self.pins[0], GPIO.HIGH)
        GPIO.output(self.pins[1], GPIO.LOW)

    def backward(self):
        GPIO.output(self.pins[0], GPIO.LOW)
        GPIO.output(self.pins[1], GPIO.HIGH)
    
    def stop(self):
        GPIO.output(self.pins[0], GPIO.LOW)
        GPIO.output(self.pins[1], GPIO.LOW)

    def set_speed(self, speed):
        if speed < 0 or speed > 100:
            print("Speed needs to be in percent.")
        self.pmw.ChangeDutyCycle(speed)


motors = [
    Motor(3, 2, 4),
    Motor(14, 15, 18)
]

def main(args):

    print("Motor test")

    print("forward")
    for motor in motors:
        motor.forward()

    for speed in range(100,-1,-5):
        for motor in motors:
            print("speed " + str(speed))
            motor.set_speed(speed)
        time.sleep(0.5)

    time.sleep(1)
    print("stop")
    for motor in motors:
        motor.stop()
    time.sleep(1)

    print("backward")
    for motor in motors:
        motor.backward()

    for speed in range(100,-1,-5):
        for motor in motors:
            print("speed " + str(speed))
            motor.set_speed(speed)
        time.sleep(0.5)

    print("finished")

    GPIO.cleanup()


if __name__ == "__main__":
    main(sys.argv[1:])
