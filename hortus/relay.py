#-*- coding: utf-8 -*-

class relay:

	def __init__(self, gpio):
		self.gpio = gpio
		print('\t*Init : relais GPIO : {}'.format(self.gpio))
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
