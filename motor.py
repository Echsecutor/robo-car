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
        self.pmw = GPIO.PWM(en_pin, PMW_FREQUENCY)
        print("New Motor using pins " + str(self.pins))

    def forward(self):
        GPIO.output(self.pins[0], GPIO.HIGH)
        GPIO.output(self.pins[1], GPIO.LOW)

    def backward(self):
        GPIO.output(self.pins[0], GPIO.LOW)
        GPIO.output(self.pins[1], GPIO.HIGH)

motors = [
    Motor(3, 2, 4),
    Motor(14, 15, 18)
]
GPIO.cleanup()
