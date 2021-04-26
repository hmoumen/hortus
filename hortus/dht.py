#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import Adafruit_DHT

class dht:
    def __init__(self, gpio):
        self.gpio = gpio
        self.type = "dht"
    
    def humidity(self):
        humidity = Adafruit_DHT.read_retry(22, self.gpio)[0]
        if humidity is not None:
            return round(humidity)
        else:
            return 0
    
    def temperature(self):
        temperature = round(Adafruit_DHT.read_retry(22, self.gpio)[1], 1)
        if temperature is not None:
            return round(temperature)
        else:
            return 0