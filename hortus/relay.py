#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO 
import time
from datetime import datetime

class relay:

	def __init__(self, gpio):
		self.gpio = gpio
		print('\t*init : relay GPIO : {}'.format(self.gpio))
		GPIO.setup(self.gpio, GPIO.OUT)
		self.off()
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

	def water(self, type, level, whour, precip):
		#print("status: {} - level: {}".format(self.status(), level))
		now = datetime.now().strftime("%I:%M %p")
		
		if (self.status() == False and level > 10 and whour == now and precip == True):
			self.start = time.time()
			self.on()
			print("{} - automatic watering in progress".format(now))
			#return (now + " - automatic watering in progress")
	
		elif (self.status() == True and self.start is not None and (level < 10 or (time.time() - self.start) > 65 )):
			self.start = None
			self.off()
			print("insufficient water level : {} or time out {}:".format(level, (time.time() - self.start)))
			#return "insufficient water level : " + level + "or time out: " + (time.time() - self.start)

		elif (self.status() == False and level > 10 and type == "manual"):
			self.start = time.time()
			self.on()
			print("{} - manual watering in progress".format(now))
			#return now +" - manual watering in progress"
		elif (self.status() == True and type == "manual"):
			self.start = None
			self.off()
			print("{} - manual watering cut-off".format(now))
			#return now + " - manual watering cut-off"
		else:
			pass