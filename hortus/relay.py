#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO 
import time
class relay:

	def __init__(self, gpio):
		self.gpio = gpio
		print('\t*init : relay GPIO : {}'.format(self.gpio))
		GPIO.setup(self.gpio, GPIO.OUT)
		self.type = "relay"
		self.start = None

	def on(self):
		GPIO.output(self.gpio, GPIO.HIGH)

	def off(self):
		GPIO.output(self.gpio, GPIO.LOW)

	def status(self):
		return GPIO.input(self.gpio)

	def test(self):
		self.on()
		time.sleep(0.5)
		self.off()
		time.sleep(0.5)

	def water(self, type, level):
		if (self.status() == False and level > 65):
			self.start = time.time()
			self.on()
			print("watering in progress")
		elif (self.status() == True and self.start is not None and (level < 10 or (time.time() - self.start) > 10 )):
			self.off()
			print("insufficient water level or time out")
		else:
			pass