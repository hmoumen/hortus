#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO 
import time
from datetime import datetime
import sys

from hortus.relay import *
from hortus.button import *
from hortus.weather import *
from hortus.dht import *
from hortus.lcd import lcd
from hortus.ultrasonic import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


tank_min = 130
well_min = 250
watering_duration = 5
whour = "04:08 PM"

def water(channel):
	if (relay1.status() == False):
		relay1.on()
		print("watering in progress ...") 
	else:
		relay1.off()
		print("watering off")

def drain_tank(channel):
	if (relay2.status() == False):
		relay2.on()
		print("draining tank in progress ...")
	else:
		relay2.off()
		print("draining off")
		
def fill(channel):
    print("filling in progress ...")

def drain_well(channel):
    print("draining well in progress ...")

def main():
	#lcd(dht1.humidity(), dht1.temperature(), hc1.get_avgdepth())
	relay1.water("auto",hc1.get_percdepth(),whour,precip)
	print("en attente")
	#sys.stdout.write("\r" + "\t{} - en attente...".format(datetime.now().strftime("%I:%M:%S %p")))
	#sys.stdout.flush()

if __name__ == "__main__":
	
	relay1 = relay(6) 		#init pump relay : tank > garden
	relay2 = relay(13) 		#init pump relay : tank > sewer
	relay3 = relay(19) 		#init pump relay : well > tank
	relay4 = relay(26) 		#init pump relay : well > egout

	button1 = button(1) 	#init push button : tank > garden
	button2 = button(7)		#init push button : tank > sewer 
	button3 = button(8)		#init push button : well > tank
	button4 = button(25)	#init push button : well > sewer
	
	dht1 = dht(23)

	hc1 = ultrasonic(14,15)

	GPIO.add_event_detect(button1.gpio,GPIO.RISING,callback=relay1.water("manual",hc1.get_percdepth(), 0, 0), bouncetime=200) 
	GPIO.add_event_detect(button2.gpio,GPIO.RISING,callback=drain_tank, bouncetime=200) 
	GPIO.add_event_detect(button3.gpio,GPIO.RISING,callback=fill, bouncetime=200)
	GPIO.add_event_detect(button4.gpio,GPIO.RISING,callback=drain_well, bouncetime=200)
	
	precip = weather()

	try:
		while True :
			main()
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit("Hortus closed, bye !")