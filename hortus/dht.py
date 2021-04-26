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
        self.humidity = None
        self.temperature = None

    def get_data(self):
        if self.flag is False:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(22, self.gpio)
            self.tempo = time.time()
            self.flag = True
            return (round(self.humidity), round(self.temperature))
        elif ((self.flag is True) and ((time.time() - self.tempo) > 3600)):
            self.flag = False
        else:
            return self.data
    
    def temperature(self):
        temperature = round(Adafruit_DHT.read_retry(22, self.gpio)[1], 1)
        if temperature is not None:
            return (round(self.humidity), round(self.temperature))
        else:
            return 0