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

class Car:
    front_left: Motor
    front_right:Motor
    back_left: Motor
    back_right:Motor
    
    def __init__(self, front_left : Motor, front_right:Motor, back_left: Motor, back_right:Motor):
        self.front_left= front_left
        self.front_right=front_right
        self.back_left=back_left
        self.back_right=back_right

    def motors(self) -> list[Motor]:
        return [self.front_left, self.front_right, self.back_left, self.back_right]

    def forward(self):
        for motor in self.motors():
            motor.forward()

    def backward(self):
        for motor in self.motors():
            motor.backward()
    
    def stop(self):
        for motor in self.motors():
            motor.stop()

    def set_speed(self, speed):
        for motor in self.motors():
            motor.set_speed(speed)

    def turn_left(self):
        self.front_right.forward()
        self.front_left.backward()
        self.back_right.forward()
        self.back_left.backward()
        
    def turn_left(self):
        self.front_right.backward()
        self.front_left.forward()
        self.back_right.backward()
        self.back_left.forward()

        

car = Car(
    Motor(3, 2, 4),
    Motor(14, 15, 18),
    Motor(9,11,10),
    Motor(27, 17, 22)
    )

def main(args):

    print("CAR TEST")

    print("forward")
    car.forward()

    for speed in range(100,50,-10):
        print("speed " + str(speed))
        car.set_speed(speed)
        time.sleep(0.5)

    print("stop")
    car.stop()
    time.sleep(1)

    print("backward")
    car.backward()

    for speed in range(100,50,-10):
        print("speed " + str(speed))
        car.set_speed(speed)
        time.sleep(0.5)

    print("stop")
    car.stop()
    time.sleep(1)


    print("finished")

    GPIO.cleanup()


if __name__ == "__main__":
    main(sys.argv[1:])
