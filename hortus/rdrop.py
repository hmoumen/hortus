#-*- coding: utf-8 -*-

class rain:
	def __init__(self, gpio):
		self.gpio = gpio
		print('Initialisation du capteur de pluie/arrosage GPIO : {}'.format(self.gpio))
		time.sleep(0.5)
		GPIO.setup(self.gpio, GPIO.IN)
	
	def status(self):
		status = GPIO.input(self.gpio)
		return status	
	
	def check_rain(self):
		if (self.status() == 1):
			return True
		else:
			return False