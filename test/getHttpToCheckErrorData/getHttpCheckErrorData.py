import requests
import sys
import time

debug = False
if len(sys.argv) > 1:
  if str(sys.argv[1]) == 'debug=true':
    print('Debug Enable')
    debug = True

time.sleep(3)

data = ''
getInit = False
while not getInit:
  try:
    getInit = True
    data = requests.get('https://web.iotsystems-vn.com/api/communication/store/0171d76b-90ae-405c-bc6c-b98e653fe2ff/slots')
  except:
    pass
while True:
  if debug:
    print('New Request')
  dataNew = requests.get('https://web.iotsystems-vn.com/api/communication/store/0171d76b-90ae-405c-bc6c-b98e653fe2ff/slots')

  if dataNew.text != data.text:
    if debug:
      print('Data Error.......')
