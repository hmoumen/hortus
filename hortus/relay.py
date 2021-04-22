#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO 
import time
class relay:

	def __init__(self, gpio):
		self.gpio = gpio
		print('\t*init : relay GPIO : {}'.format(self.gpio))
		GPIO.setup(self.gpio, GPIO.OUT)
		self.type = "relay"

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

	def water(self, type, level, start):
		duration = time.time() - start
		if (self.status() == False and level > 10 and duration < 300):
			self.on()
			print("\twatering in progress ...")
			print('\t*level \t: {}'.format(level))
			print('\t*duration \t: {}'.format(duration))
		elif (self.status() == False and level < 10 or duration > 300):
			self.off()
			print("insufficient water level")
		else:
			pass