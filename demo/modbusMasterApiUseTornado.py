import functools

from tornado.ioloop import IOLoop
from pymodbus.client.asynchronous import schedulers

# ---------------------------------------------------------------------------#
# choose the requested modbus protocol
# ---------------------------------------------------------------------------#

from pymodbus.client.asynchronous.serial import AsyncModbusSerialClient

# ---------------------------------------------------------------------------#
# configure the client logging
# ---------------------------------------------------------------------------#
import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# ---------------------------------------------------------------------------#
# helper method to test deferred callbacks
# ---------------------------------------------------------------------------#


def dassert(future, callback):

    def _assertor(value):
        # by pass assertion, an error here stops the write callbacks
        assert value  

    def on_done(f):
        exc = f.exception()
        if exc:
            log.debug(exc)
            return _assertor(False)

        return _assertor(callback(f.result()))

    future.add_done_callback(on_done)


def _print(value):
    if hasattr(value, "bits"):
        t = value.bits
    elif hasattr(value, "registers"):
        t = value.registers
    else:
        log.error(value)
        return
    log.info("Printing : -- {}".format(t))
    return t

UNIT = 0x01


def beginAsynchronousTest(client, protocol):
    rq = client.write_coil(1, True, unit=UNIT)
    rr = client.read_coils(1, 1, unit=UNIT)
    dassert(rq, lambda r: r.function_code < 0x80)     # test for no error
    dassert(rr, _print)          # test the expected value

    rq = client.write_coils(1, [False]*8, unit=UNIT)
    rr = client.read_coils(1, 8, unit=UNIT)
    dassert(rq, lambda r: r.function_code < 0x80)     # test for no error
    dassert(rr, _print)         # test the expected value

    rq = client.write_coils(1, [False]*8, unit=UNIT)
    rr = client.read_discrete_inputs(1, 8, unit=UNIT)
    dassert(rq, lambda r: r.function_code < 0x80)     # test for no error
    dassert(rr, _print)         # test the expected value

    rq = client.write_register(1, 10, unit=UNIT)
    rr = client.read_holding_registers(1, 1, unit=UNIT)
    dassert(rq, lambda r: r.function_code < 0x80)     # test for no error
    dassert(rr, _print)       # test the expected value

    rq = client.write_registers(1, [10]*8, unit=UNIT)
    rr = client.read_input_registers(1, 8, unit=UNIT)
    dassert(rq, lambda r: r.function_code < 0x80)     # test for no error
    dassert(rr, _print)      # test the expected value

    arguments = {
        'read_address':    1,
        'read_count':      8,
        'write_address':   1,
        'write_registers': [20]*8,
    }
    rq = client.readwrite_registers(**arguments, unit=UNIT)
    rr = client.read_input_registers(1,8, unit=UNIT)
    dassert(rq, lambda r: r.registers == [20]*8)      # test the expected value
    dassert(rr, _print)      # test the expected value

    # -----------------------------------------------------------------------#
    # close the client at some time later
    # -----------------------------------------------------------------------#
    IOLoop.current().add_timeout(IOLoop.current().time() + 1, client.close)
    IOLoop.current().add_timeout(IOLoop.current().time() + 2, protocol.stop)

def err(*args, **kwargs):
    log.error("Err", args, kwargs)


def callback(protocol, future):
    log.debug("Client connected")
    exp = future.exception()
    if exp:
        return err(exp)

    client = future.result()
    return beginAsynchronousTest(client, protocol)


if __name__ == "__main__":

    # Rtu
    protocol, future = AsyncModbusSerialClient(schedulers.IO_LOOP,
                                               method="rtu",
                                               port="/dev/ttyUSB0",
                                               baudrate=115200,
                                               timeout=2)
    future.add_done_callback(functools.partial(callback, protocol))
