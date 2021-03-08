import OPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT)

while True:
	gpio.output(16, 1)
	time.sleep(0.2)
	gpio.output(16, 0)
	time.sleep(0.2)
