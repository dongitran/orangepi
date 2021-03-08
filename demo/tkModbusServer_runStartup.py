import sys

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import time 

PORT = '/dev/ttyUSB0'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

    #Create the server
    server = modbus_rtu.RtuServer(serial.Serial(port=PORT, baudrate=115200))

    try:
        logger.info("running...")
        logger.info("enter 'quit' for closing the server")

        server.start()

        slave_1 = server.add_slave(2)
        slave_1.add_block('0', cst.HOLDING_REGISTERS, 0, 100)
        while True:
            time.sleep(1)

    finally:
        server.stop()

if __name__ == "__main__":
    main()
