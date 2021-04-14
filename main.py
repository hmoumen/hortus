#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO 
import time
from datetime import datetime
import sys
import datetime
from hortus.tank import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


tank_min = 130
well_min = 250
watering_hour = "02:43 PM"

def main():
	now = datetime.datetime.now().strftime("%I:%M %p")
	if (now == watering_hour):
		stop_time = time.time() + 60
		relay1.on()
		counter = 0
		while(time.time() != stop_time):
			counter += 1 
			sys.stdout.write("\r" + "{}\t - Arrosage en cours...".format(datetime.datetime.now().strftime("%I:%M:%S %p")))
			sys.stdout.flush()
			time.sleep(1)
	else:
		sys.stdout.write("\r" + "\t{} - En attente...".format(datetime.datetime.now().strftime("%I:%M:%S %p")))
		sys.stdout.flush()
if __name__ == "__main__":
	tank1 = tank(200)
	relay1 = relay(22)
	relay2 = relay(23)
	relay3 = relay(24)
	relay4 = relay(25)

	relay1.test()
	relay2.test()
	#ultrasonic1 = ultrasonic(14, 15)
	
	#rain1 = rain(17)
	#rain2 = rain(27)
	
	while True :
		main()
GPIO.cleanup()