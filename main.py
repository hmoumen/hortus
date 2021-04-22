#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO 
import time
from datetime import datetime
import sys
import datetime
from hortus.relay import *
from hortus.button import *
from hortus.weather import *
from hortus.dht import *
from hortus.lcd import lcd

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


tank_min = 130
well_min = 250
watering_duration = 5
watering_hour = "12:36 PM"

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
	#setup event on pin rising edge
	lcd(dht1.humidity(), dht1.temperature, precip)
	now = datetime.datetime.now().strftime("%I:%M %p")
	if (now == watering_hour and precip == True):
		relay1.on()	
	else:
		sys.stdout.write("\r" + "\t{} - en attente...".format(datetime.datetime.now().strftime("%I:%M:%S %p")))
		sys.stdout.flush()

if __name__ == "__main__":
	
	relay1 = relay(6) 		#init pump relay : tank > garden
	relay2 = relay(13) 		#init pump relay : tank > sewer
	relay3 = relay(19) 		#init pump relay : well > tank
	relay4 = relay(26) 		#init pump relay : well > egout

	button1 = button(1) 	#init push button : tank > garden
	button2 = button(7)	#init push button : tank > sewer 
	button3 = button(8)	#init push button : well > tank
	button4 = button(25)	#init push button : well > sewer
	
	dht1 = dht(23)

	GPIO.add_event_detect(button1.gpio,GPIO.RISING,callback=water, bouncetime=200) 
	GPIO.add_event_detect(button2.gpio,GPIO.RISING,callback=drain_tank, bouncetime=200) 
	GPIO.add_event_detect(button3.gpio,GPIO.RISING,callback=fill, bouncetime=200)
	GPIO.add_event_detect(button4.gpio,GPIO.RISING,callback=drain_well, bouncetime=200)
	precip = weather()

	while True :
		main()

GPIO.cleanup()