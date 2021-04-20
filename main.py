#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO 
import time
from datetime import datetime
import sys
import datetime
from hortus.relay import *
from hortus.button import *
from hortus.weather import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


tank_min = 130
well_min = 250
watering_hour = "02:43 PM"

def water(channel):
    print("watering in progress ...")

def drain_tank(channel):
    print("draining tank in progress ...")

def fill(channel):
    print("filling in progress ...")

def drain_well(channel):
    print("draining well in progress ...")

def main():
	#setup event on pin rising edge
	GPIO.add_event_detect(button1.gpio,GPIO.RISING,callback=water) 
	GPIO.add_event_detect(button2.gpio,GPIO.RISING,callback=drain_tank) 
	GPIO.add_event_detect(button3.gpio,GPIO.RISING,callback=fill)
	GPIO.add_event_detect(button4.gpio,GPIO.RISING,callback=drain_well)

	now = datetime.datetime.now().strftime("%I:%M %p")
	weather()

	if (now == watering_hour):
		stop_time = time.time() + 60
		relay1.on()
		counter = 0
		while(time.time() != stop_time):
			counter += 1 
			sys.stdout.write("\r" + "{}\t - arrosage en cours...".format(datetime.datetime.now().strftime("%I:%M:%S %p")))
			sys.stdout.flush()
			time.sleep(1)
	else:
		sys.stdout.write("\r" + "\t{} - en attente...".format(datetime.datetime.now().strftime("%I:%M:%S %p")))
		sys.stdout.flush()

if __name__ == "__main__":
	
	relay1 = relay(22) 		#init pump relay : tank > garden
	relay2 = relay(23) 		#init pump relay : tank > sewer
	relay3 = relay(24) 		#init pump relay : well > tank
	relay4 = relay(25) 		#init pump relay : well > egout

	button1 = button(13)  	#init push button : tank > garden
	button2 = button(15)	#init push button : tank > sewer 
	button3 = button(16)	#init push button : well > tank
	button4 = button(18)	#init push button : well > sewer
	
	while True :
		main()

GPIO.cleanup()