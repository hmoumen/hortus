#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

class dht:
    def __init__(self, gpio):
        self.gpio = gpio
        self.type = "dht"
        self.tempo = 0
        self.flag = False

    def data(self):
        if self.flag is False:
            self.data[0], self.data[1] = round(Adafruit_DHT.read_retry(22, self.gpio))
            self.tempo = time.time()
            self.flag = True
            return self.data
        elif ((self.flag is True) and ((time.time() - self.tempo) > 3600)):
            self.flag = False
        else:
            return self.data
    
    def temperature(self):
        temperature = round(Adafruit_DHT.read_retry(22, self.gpio)[1], 1)
        if temperature is not None:
            return round(temperature)
        else:
            return 0