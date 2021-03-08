import threading
import queue
import serial
import time
import sys

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = '/dev/ttyUSB0'

debug = False
if len(sys.argv) > 1:
  if str(sys.argv[1]) == 'debug=true':
    print('Debug Enable')
    debug = True

class modbusRtuMaster(threading.Thread):
  def __init__(self, threadID, name, queue_http_send, queue_http_received):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.queue_http_send = queue_http_send
    self.queue_http_received = queue_http_received
  def run(self):
    #Connect to the slave
    try:
      master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=115200, bytesize=8, parity='N'))
      master.set_timeout(0.1)
      master.set_verbose(True)
    except modbus_tk.modbus.ModbusError as exc:
      logger.error("%s- Code=%d", exc, exc.get_exception_code())
    if debug:
      counterPoll = 0
      timeCurrent = time.time()
    while True:
      try:
        master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 100)
      except:
        if debug:
          print('Modbus - Slave no respond')
      if debug:
        counterPoll = counterPoll + 1
        
        if counterPoll >= 100:
          print("Modbus - Process: " + str(counterPoll/(time.time() - timeCurrent)))
          timeCurrent = time.time()
          counterPoll = 0
          self.queue_http_send.put('aaa')

class httpProcess(threading.Thread):
  def __init__(self, threadID, name, queue_http_request, queue_http_return):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.queue_http_request = queue_http_request
    self.queue_http_return = queue_http_return
  def run(self):
    while True:
      a = self.queue_http_request.get()
      print('HttpProcess: ' + str(a))


def main():
  threads = []
  queue_data_http_request = queue.Queue(1)
  queue_data_http_return = queue.Queue(1)

  thread = modbusRtuMaster(1, "Modbus Master", queue_data_http_request, queue_data_http_return)
  thread.start()
  threads.append(thread)
  thread = httpProcess(2, "Http Process", queue_data_http_request, queue_data_http_return)
  thread.start()
  threads.append(thread)

  for t in threads:
    t.join()
  print("Exit Program")

if __name__ == "__main__":
  main()
