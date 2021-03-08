import OPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)

while True:
	gpio.output(12, 1)
	time.sleep(0.1)
	gpio.output(12, 0)
	time.sleep(0.1)

