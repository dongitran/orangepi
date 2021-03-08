from pymodbus.server.sync import StartTcpServer as StartServer
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from pymodbus.datastore.remote import RemoteSlaveContext
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# --------------------------------------------------------------------------- # 
# configure the service logging
# --------------------------------------------------------------------------- # 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_serial_forwarder():
    client = ModbusClient(method='rtu', port='ttyUSB0')

    store = RemoteSlaveContext(client)
    context = ModbusServerContext(slaves=store, single=True)
    StartServer(context, address=("localhost", 5020))


if __name__ == "__main__":
    run_serial_forwarder()
