from random import random
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import random

factory = PiGPIOFactory(host='192.168.52.164')
servoHand = Servo(18, pin_factory=factory)
servoMouth = Servo(17, pin_factory=factory)

def hand():
    servoHand.value = -1
    sleep(0.75)
    servoHand.value = 1
    sleep(0.75)
    servoHand.value = -1
    sleep(0.75)
    servoHand.value = 1

def mouth(seconds):
    for i in range(seconds):
        servoMouth.value = random.randint(0,1)
        sleep(0.2)
        servoMouth.value = random.randint(-1,0)
        sleep(0.2)
        servoMouth.value = random.randint(-1,1)
        sleep(0.2)
        servoMouth.value = random.randint(-1,0)
        sleep(0.2)
