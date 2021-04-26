#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO 
import time

class ultrasonic:

	def __init__(self, gpio_trigger, gpio_echo):
		self.gpio_trigger = gpio_trigger
		self.gpio_echo = gpio_echo
		print('\t*Init : capteur ultrason GPIO : ')
		print('\t\t **Trigger GPIO \t: {}'.format(self.gpio_trigger))
		print('\t\t **Echo GPIO \t: {}'.format(self.gpio_echo))
		GPIO.setup(self.gpio_trigger,GPIO.OUT)
		GPIO.setup(self.gpio_echo,GPIO.IN)

	def get_depth(self):
		GPIO.output(self.gpio_trigger, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(self.gpio_trigger, GPIO.HIGH) # set TRIGGER to HIGH
		time.sleep(0.00001) # wait 10 microseconds
		GPIO.output(self.gpio_trigger, GPIO.LOW) # set TRIGGER to LOW
		start = time.time()
		while GPIO.input(self.gpio_echo)==0:
			start = time.time()
		# Assign the actual time to stop variable until the ECHO goes back from HIGH to LOW
		while GPIO.input(self.gpio_echo)==1:
			stop = time.time()
		# Calculate the time it took the wave to travel there and back
		measuredTime = stop - start
		# Calculate the travel distance by multiplying the measured time by speed of sound
		distanceBothWays = measuredTime * 33112 # cm/s in 20 degrees Celsius
		# Divide the distance by 2 to get the actual distance from sensor to obstacle
		depth = distanceBothWays / 2
		return depth

	def get_avgdepth(self):
		i = 0
		depth_sum = 0
		depth = 0
		GPIO.output(self.gpio_trigger, GPIO.LOW)
		time.sleep(0.5)
		while (i < 10):
			GPIO.output(self.gpio_trigger, GPIO.HIGH) # set TRIGGER to HIGH
			time.sleep(0.00001) # wait 10 microseconds
			GPIO.output(self.gpio_trigger, GPIO.LOW) # set TRIGGER to LOW
			start = time.time()
			while GPIO.input(self.gpio_echo)==0:
				start = time.time()
			# Assign the actual time to stop variable until the ECHO goes back from HIGH to LOW
			while GPIO.input(self.gpio_echo)==1:
				stop = time.time()
			# Calculate the time it took the wave to travel there and back
			distanceBothWays = measuredTime * 33112 # cm/s in 20 degrees Celsius
			# Divide the distance by 2 to get the actual distance from sensor to obstacle
			depth = distanceBothWays / 2
			if (depth != 0):5
				depth_sum = depth_sum + depth
				i+=1

		average_depth = (depth_sum / i)
		return depth

	def get_percdepth(self):
		return ((self.get_avgdepth() / 150) * 100)
		#depth_per = 100 - ((self.get_avgdepth() / 150) * 100)
		#if (depth_per > 20):
			#print("Reservoir d'eau rempli à {} %".format(depth_per))
		#	return True
		#else:
		#	return False