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
GPIO.setmode(GPIO.BOARD)


tank_min = 130
well_min = 250
watering_duration = 5
watering_hour = "02:43 PM"

def chrono():
	stop_time = time.time() + watering_duration
	counter = 0
	while(time.time() != stop_time):
		counter += 1
		time.sleep(1)
	

def water(channel):
	if (relay1.status() == False):
		relay1.on()
		print("watering in progress ...")
		time.sleep(4)
		GPIO.add_event_detect(button1.gpio,GPIO.RISING,callback=water) 
		print("callback") 
	else:
		relay1.off()
		print("watering off")
		time.sleep(1)
		GPIO.add_event_detect(button1.gpio,GPIO.RISING,callback=water) 

def drain_tank(channel):
	if (relay2.status() == False):
		relay2.on()
		print("draining tank in progress ...")
	else:
		relay2.off()
		print("OFF")
		time.sleep(1)
		
def fill(channel):
    print("filling in progress ...")

def drain_well(channel):
    print("draining well in progress ...")

def main():
	#setup event on pin rising edge


	now = datetime.datetime.now().strftime("%I:%M %p")
	precip = weather()

	if (now == watering_hour and precip == True):
		relay1.on()	
	else:
		sys.stdout.write("\r" + "\t{} - en attente...".format(datetime.datetime.now().strftime("%I:%M:%S %p")))
		sys.stdout.flush()

if __name__ == "__main__":
	
	relay1 = relay(31) 		#init pump relay : tank > garden
	relay2 = relay(33) 		#init pump relay : tank > sewer
	relay3 = relay(35) 		#init pump relay : well > tank
	relay4 = relay(37) 		#init pump relay : well > egout

	button1 = button(29) 	#init push button : tank > garden
	button2 = button(22)	#init push button : tank > sewer 
	button3 = button(23)	#init push button : well > tank
	button4 = button(24)	#init push button : well > sewer
	
	GPIO.add_event_detect(button1.gpio,GPIO.RISING,callback=water) 
	GPIO.add_event_detect(button2.gpio,GPIO.RISING,callback=drain_tank) 
	GPIO.add_event_detect(button3.gpio,GPIO.RISING,callback=fill)
	GPIO.add_event_detect(button4.gpio,GPIO.RISING,callback=drain_well)
	
	while True :
		main()

GPIO.cleanup()