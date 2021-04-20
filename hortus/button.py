#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO 

class button:

    def __init__(self, gpio):
        self.gpio = gpio
        #set pin to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(self.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #print('\t*init : Push button GPIO : {}'.format(self.gpio))
        self.type = "push button"

    def status(self):
        #return button state
        return GPIO.input(self.gpio)