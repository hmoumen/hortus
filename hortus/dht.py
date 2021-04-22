#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import Adafruit_DHT

class dht:
    def __init__(self, gpio):
        self.gpio = gpio
        self.type = "dht"
    
    def humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(22, self.gpio)
        if humidity is not None:
            print('Humidity = {1:0.1f}%'.format(humidity))
    
    def temperature(self):
        humidity, temperature = Adafruit_DHT.read_retry(22, self.gpio)
        if humidity is not None and temperature is not None:
            print('Temperature = {0:0.1f}°C'.format(temperature)


