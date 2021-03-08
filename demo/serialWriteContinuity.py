import serial
import time 

s = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
s.isOpen()

while 1:
    s.write(b'headsfasdfasdfasdfasdfasdfsafasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfllo\r\n')
    time.sleep(1)

