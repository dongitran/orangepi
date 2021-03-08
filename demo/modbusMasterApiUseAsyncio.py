#!/usr/bin/env python
from pymodbus.compat import IS_PYTHON3, PYTHON_VERSION
if IS_PYTHON3 and PYTHON_VERSION >= (3, 4):
    import logging
    import asyncio
    from pymodbus.client.asynchronous.serial import (
        AsyncModbusSerialClient as ModbusClient)
    from pymodbus.client.asynchronous import schedulers
else:
    import sys
    sys.stderr("This example needs to be run only on python 3.4 and above")
    sys.exit(1)

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

UNIT = 0x01


async def start_async_test(client):
    try:
        log.debug("Write to a holding register and read back")
        #rq = await client.write_register(1, 10, unit=UNIT)
        rr = await client.read_holding_registers(1, 1, unit=UNIT)
        assert(rq.function_code < 0x80)     # test that we are not an error
        assert(rr.registers[0] == 10)       # test the expected value

        
        arguments = {
            'read_address':    1,
            'read_count':      8,
            'write_address':   1,
            'write_registers': [20]*8,
        }
        log.debug("Read write registers simulataneously")
        rq = await client.readwrite_registers(unit=UNIT, **arguments)
        rr = await client.read_holding_registers(1, 8, unit=UNIT)
        assert(rq.function_code < 0x80)     # test that we are not an error
        assert(rq.registers == [20]*8)      # test the expected value
        assert(rr.registers == [20]*8)      # test the expected value
    except Exception as e:
        log.exception(e)
        client.transport.close()
    await asyncio.sleep(1)


if __name__ == '__main__':
    loop, client = ModbusClient(schedulers.ASYNC_IO, port='/dev/ttyUSB0',
                                baudrate=115200, method="rtu")
    loop.run_until_complete(start_async_test(client.protocol))
    loop.close()
