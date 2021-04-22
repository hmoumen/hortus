#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO 
import time
class relay:

	def __init__(self, gpio):
		self.gpio = gpio
		print('\t*init : relay GPIO : {}'.format(self.gpio))
		GPIO.setup(self.gpio, GPIO.OUT)
		self.type = "relay"

	def on(self, launch_time):
		GPIO.output(self.gpio, GPIO.HIGH)
		self.launch_time = launch_time

	def off(self):
		GPIO.output(self.gpio, GPIO.LOW)

	def status(self):
		return GPIO.input(self.gpio)

	def test(self):
		self.on()
		time.sleep(0.5)
		self.off()
		time.sleep(0.5)

	def water(self, type, level, start):
		duration = time.time() - start
		if (self.status() == False and level > 10 and duration < 300):
			relay1.on(now)
			print("watering in progress ...") 
		elif (self.status() == False and level < 10 and duration < 300):
			relay1.off()
			print("insufficient water level")
		else:
			relay1.off()
			print("insufficient water level")