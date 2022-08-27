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
  try:
    getInit = True
    dataNew = requests.get('https://web.iotsystems-vn.com/api/communication/store/0171d76b-90ae-405c-bc6c-b98e653fe2ff/slots')

    if dataNew.text != data.text:
      if debug:
        print('Data Error.......')
        sys.exit()
  except:
    pass


[2021-07-28 01:51:46.882363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.913314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.944361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.975374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.006346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.037326][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.068285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.099289][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.130263][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.161304][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.192479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.223482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.254509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.285455][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.316482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.347406][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.378409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.409567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.440544][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.471540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.502571][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.533531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.564582][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.595527][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.626500][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.657522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.688538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.719640][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.750628][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.781602][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.812603][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.874460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.905519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.936519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.967590][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.998542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.029465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.060443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.091447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.122744][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.153745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.184767][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.215790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.246852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.277830][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.339663][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.370689][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.401652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.432676][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.463693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.494675][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.525641][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.556685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.587774][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.618778][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.650037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.681190][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.712160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.743174][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.774246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.805285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.836546][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.867540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.898541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.929574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.960700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.991698][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.022646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.053744][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.084833][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.115797][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.146757][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.177698][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.208702][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.239650][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.270704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.302053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.333051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.363955][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.394909][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.425828][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.456846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.487819][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.518878][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.549865][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.580890][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.611816][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.642919][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.673850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.704814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.735748][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.766820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.797808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.828915][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.859872][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.890877][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.921807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.983539][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.014614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.045661][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.076841][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.107800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.138852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.169855][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.200883][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.231818][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.262850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.293857][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.324879][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.355881][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.386875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.448631][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.479563][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.510532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.541438][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.572455][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.603956][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.634940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.665935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.697020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.728043][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.759039][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.790042][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.820996][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.852127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.883152][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.914080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.945097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.976113][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.007145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.038099][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.069137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.100190][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.131176][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.162127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.193131][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.224195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.255168][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.286228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.317185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.348224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.379259][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.410325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.441303][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.472399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.503382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.534395][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.565440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.596405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.658239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.689206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.720157][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.751115][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.782127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.813092][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.844082][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.875134][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.906103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.937203][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.968167][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.999179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.030213][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.061223][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.123032][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.154021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.185054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.216163][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.247265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.278330][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.309331][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.340371][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.371470][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.402513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.433535][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.464637][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.495668][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.526601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.588385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.619409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.650467][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.681407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.712363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.743413][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.774380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.805333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.836370][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.867327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.898332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.929353][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.960345][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.991475][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.022452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.053477][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.084540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.115493][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.146450][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.177461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.208456][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.239423][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.270371][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.301391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.332536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.363530][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.394555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.425616][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.456669][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.487653][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.518782][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.549795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.580826][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.611798][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.642808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.673839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.704906][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.735907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.797672][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.828688][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.859718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.890754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.921779][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.952790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.983799][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.014845][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.045969][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.077012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.108268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.139438][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.170380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.201397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.232385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.263460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.294401][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.325361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.356398][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.387409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.418346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.449314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.480318][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.511332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.542276][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.573421][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.604381][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.635346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.666254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.697210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.728248][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.759166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.790164][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.820949][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -337.600006 to -337.399994]
[2021-07-28 01:51:54.820997][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -337.600006 to -337.399994|5]
[2021-07-28 01:51:54.821116][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.852109][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.883120][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.914089][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.945038][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.976053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.007080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.038106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.069080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.100170][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.131209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.162140][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.193186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.224156][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.255162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.286165][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.317191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.348238][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.379257][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.441054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.472023][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.503031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.533975][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.564965][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.595893][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.626910][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.657884][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.688937][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.719972][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.751013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.782034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.813073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.844093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.905859][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.936902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.968118][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.999244][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.030300][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.061261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.092169][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.123214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.154350][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.185389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.216396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.247693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.278754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.309983][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.340943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.372167][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.403162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.434372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.465364][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.496542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.527471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.558494][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.589409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.620335][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.651285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.682402][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.713388][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.744302][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.775226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.806178][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.837095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.868137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.899052][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.930022][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.961016][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.991997][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.022915][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.053859][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.084800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.115769][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.146722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.177722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.208754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.239818][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.270853][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.301773][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.332754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.363761][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.394708][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.425685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.456627][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.487674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.518590][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.549646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.580649][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.611686][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.642619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.673603][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.704565][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.735655][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.766591][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.797776][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.829145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.860062][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.890949][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.921888][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.952878][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.983790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.014673][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.046027][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.077057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.108091][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.139162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.170168][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.201205][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.232148][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.263229][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.294277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.325230][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.356211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.387241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.418287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.449275][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.480224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.511227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.542290][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.573304][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.604258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.635347][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.666295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.697228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.759326][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.790391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.821354][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.852339][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.883297][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.914328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.945321][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.976346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.007292][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.038293][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.069291][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.100315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.131320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.162302][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.224223][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.255186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.286103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.317131][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.348125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.379094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.410029][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.441053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.472453][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.503460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.534551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.565507][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.596518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.627564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.658505][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.689475][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.720601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.751566][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.782515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.813463][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.844505][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.875455][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.906389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.937478][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.968473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.999507][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.030451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.061416][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.092400][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.123346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.154358][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.185434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.216420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.247427][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.278468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.309471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.340500][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.371513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.402461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.433480][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.464500][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.495447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.526433][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.557421][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.588438][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.619392][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.650386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.681410][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.712492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.743503][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.774528][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.805559][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.836532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.898410][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.929426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.960485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.991498][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.022448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.053393][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.084389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.115435][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.146385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.177396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.208452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.239432][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.270341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.301267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.332261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.363315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.394313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.425387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.456424][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.487622][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.518646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.549556][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.580545][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.611542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.642512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.673525][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.704542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.735513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.766411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.797382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.828626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.859655][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.890645][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.921576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.952620][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.983635][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.014627][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.076389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.107428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.138356][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.169361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.200360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.231367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.262373][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.293345][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.324328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.355306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.386273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.417274][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.448260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.510154][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.541106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.572143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.603145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.634080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.665056][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.696051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.727013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.758400][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.789400][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.820419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.851353][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.882259][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.913245][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.944175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.006057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.037084][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.068042][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.098980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.129936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.160924][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.191850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.222910][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.253900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.284920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.315913][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.346925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.377931][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.408893][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.439838][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.470854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.501853][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.532957][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.563993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.594963][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.625925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.656839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.687820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.719088][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.749998][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.780995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.812097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.843146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.874085][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.905021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.936169][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.967188][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.998203][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.029206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.060236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.091261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.122231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.184262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.215287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.246239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.277231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.308231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.339231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.370226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.401136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.432313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.463288][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.494240][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.525177][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.556097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.587092][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.618064][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.649435][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.680485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.711467][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.742386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.773399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.804426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.835443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.897216][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.928227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.959211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.990195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.021188][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.052226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.083165][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.114307][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.145284][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.176236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.207223][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.238206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.269181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.300080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.361900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.392925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.423919][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.454924][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.485879][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.516880][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.547917][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.579162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.610203][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.641315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.672314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.703393][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.734270][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.765412][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.827387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.858320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.889533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.920562][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.951621][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.982565][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.013555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.044588][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.075850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.106815][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.137758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.168808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.199824][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.230836][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.292572][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.323488][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.354394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.385414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.416469][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.447470][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.478426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.509439][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.540416][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.571519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.602485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.633453][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.664366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.695382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.726333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.757430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.788378][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.819333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.850254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.881161][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.912055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.942970][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.973905][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.004946][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.035901][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.066922][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.097875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.128891][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.159822][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.190819][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.221801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.252795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.283725][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.314652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.345683][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.376866][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.407762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.469522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.500488][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.531443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.562524][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.593506][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.624611][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.655651][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.686646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.717613][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.748709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.779682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.810714][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.841645][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.872612][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.903551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.934519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.965448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.996484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.027434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.058392][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.089332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.120376][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.151447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.182391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.213331][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.244332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.275368][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.306330][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.337246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.368295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.399204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.430228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.461160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.492119][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.523048][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.554073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.585009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.616145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.647153][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.678327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.709268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.740458][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.771394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.802579][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.833523][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.864656][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.895644][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.926574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.957523][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.988616][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.019547][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.050449][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.081611][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.112626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.143536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.174536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.205528][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.236527][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.267424][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.298325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.329321][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.360255][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.391212][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.422315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.453231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.480857][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.500000 to -336.700012]
[2021-07-28 01:52:09.480910][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.500000 to -336.700012|6]
[2021-07-28 01:52:09.484120][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.515020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.546083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.577021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.608100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.639060][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.670093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.701044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.731968][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.762971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.793888][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.824846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.855885][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.886857][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.917824][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.948740][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.010686][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.041753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.072675][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.103710][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.134697][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.165682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.196635][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.227670][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.258606][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.289635][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.320570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.351574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.382562][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.413484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.475393][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.506322][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.537532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.568520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.599684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.630638][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.662102][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.693083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.724046][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.754985][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.785951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.816929][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.848015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.878943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.910007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.940917][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.971852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.002783][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.033814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.064788][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.095780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.126700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.157801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.188750][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.219837][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.250780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.281734][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.312682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.343703][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.374678][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.405722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.436738][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.467759][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.498705][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.529630][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.560554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.622425][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.653430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.684388][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.715556][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.746543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.777504][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.808464][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.839529][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.870436][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.901403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.932377][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.963445][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.994368][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.025368][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.056330][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.087294][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.118253][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.149245][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.180211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.211144][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.242051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.273007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.304029][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.335049][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.366009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.397012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.427967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.458975][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.489990][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.521210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.552174][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.583363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.614319][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.645496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.676464][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.707479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.738410][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.769608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.800543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.831507][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.862403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.893382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.924337][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.955214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.986132][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.017212][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.048143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.079171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.110096][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.141010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.171901][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.233633][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.264762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.295684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.326582][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.357496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.388657][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.419598][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.450638][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.481587][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.512602][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.543719][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.574664][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.605589][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.636518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.667432][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.698419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.729370][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.760354][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.791266][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.822403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.853366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.884333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.915296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.946227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.977183][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.008233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.039145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.070260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.101180][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.132085][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.163014][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.194005][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.225034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.256020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.286934][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.317973][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.348916][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.379945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.410902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.441913][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.472865][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.503797][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.534737][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.565745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.596755][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.628026][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.658922][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.689898][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.720873][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.751814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.782711][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.844350][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.875268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.906233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.937207][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.968210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.999204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.030092][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.061083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.092219][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.123299][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.154260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.185372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.216326][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.247210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.278104][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.309242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.340199][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.371171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.402090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.433044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.463955][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.494847][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.525835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.556857][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.587769][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.618735][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.649719][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.681209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.712215][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.743162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.774076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.805017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.835928][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.866849][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.897724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.928674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.959613][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.990601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.021541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.052541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.083459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.114358][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.145285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.176316][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.207237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.238215][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.269108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.300103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.330981][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.361871][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.392802][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.423698][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.454584][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.485715][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.516605][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.547536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.578418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.609419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.640325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.671327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.702280][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.733262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.764184][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.795119][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.826027][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.856978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.887897][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.919112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.950035][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.980982][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.011895][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.042931][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.073826][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.104807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.135729][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.166773][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.197718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.228737][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.259659][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.290672][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.321616][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.352682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.383690][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.414666][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.445653][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.476618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.507602][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.538793][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.569736][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.631471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.662736][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.693798][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.725046][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.756095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.787240][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.818107][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.849093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.880024][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.911054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.941998][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.973053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.003954][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.034867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.096566][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.127520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.158555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.189479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.220628][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.251570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.282734][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.313753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.345038][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.376020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.407234][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.438272][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.469293][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.500242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.531323][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.562334][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.593459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.624594][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.655540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.686480][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.717384][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.748301][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.779255][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.810285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.841285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.872256][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.903275][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.934200][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.965127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.996064][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.027254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.058239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.089217][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.120190][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.151164][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.182098][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.213111][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.244068][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.275100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.306049][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.337196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.368136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.399265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.430201][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.461151][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.492090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.523319][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.554270][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.585451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.616399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.647425][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.678332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.709258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.740251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.771265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.802210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.833171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.864224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.895231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.926191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.957143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.988135][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.019186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.050089][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.081099][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.112013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.143006][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.173960][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.235724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.266718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.297681][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.328632][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.359533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.390511][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.421418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.452399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.483333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.514316][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.545355][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.576271][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.607176][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.638196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.700407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.731322][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.762314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.793212][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.824145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.855072][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.886094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.917125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.948106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.979041][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.010056][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.041009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.071908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.102842][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.133812][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.164754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.195758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.226676][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.257646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.288576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.319548][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.350836][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.381754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.412699][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.443797][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.474752][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.505768][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.536689][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.567671][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.598762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.629707][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.660637][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.691552][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.722433][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.753333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.815397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.846328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.877288][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.908236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.939201][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.970231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.001157][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.032058][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.063037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.093952][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.124850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.155867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.186855][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.217784][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.279557][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.310697][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.341701][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.372651][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.403566][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.434583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.465560][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.496875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.527811][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.558795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.589757][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.620834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.651779][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.682684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.713608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.744632][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.775576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.806603][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.837543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.868554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.899484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.930412][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.961446][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.992673][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.023718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.054791][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.085722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.116740][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.147754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.178745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.209766][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.240843][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.271762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.302772][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.333763][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.364730][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.395678][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.457778][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.488726][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.519650][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.550701][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.581620][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.612626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.643604][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.674611][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.705538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.736583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.767513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.798428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.829378][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.860405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.891320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.922416][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.953383][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.984414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.015360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.046422][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.077404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.108380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.139312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.170337][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.201324][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.232333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.263286][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.294268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.325233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.356179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.387353][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.418348][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.449294][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.480255][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.511178][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.542182][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.573078][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.634800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.665702][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.696601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.727573][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.758471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.789412][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.820361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.851325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.882341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.913465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.944436][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.975532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.006475][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.068341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.099496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.130525][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.161531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.192482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.223465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.254431][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.285454][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.316476][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.347541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.378577][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.409585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.440543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.471494][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.502471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.533490][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.564460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.595499][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.626431][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.657443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.688397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.719463][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.750420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.781307][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.812234][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.843295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.874237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.905274][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.936214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.967272][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.998252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.029297][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.060248][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.091384][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.122335][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.153468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.184495][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.246462][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.277613][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.308519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.339527][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.370460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.401551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.432488][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.463542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.494554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.525598][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.556567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.587727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.618691][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.649735][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.680688][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.711840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.742978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.773969][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.804935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.835951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.866907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.897928][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.928909][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.960195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.991114][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.022094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.053050][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.084031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.114967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.145915][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.176908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.207864][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.238888][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.269945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.300947][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.331867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.362789][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.424552][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.455567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.486487][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.517543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.548491][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.579575][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.610526][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.641588][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.672582][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.703554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.734491][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.765684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.796657][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.827652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.889428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.920374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.951383][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.982378][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.013420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.044380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.075343][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.106277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.137367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.168348][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.199405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.230364][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.261366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.292414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.354181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.385394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.416386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.447420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.478372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.509365][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.540305][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.571241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.602173][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.633175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.664138][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.695150][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.726149][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.757145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.788086][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.819267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.850242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.881237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.912172][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.943103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.974017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.004928][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.035910][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.066957][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.097911][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.128932][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.159907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.190902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.221836][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.252804][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.283727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.314766][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.345840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.376867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.407804][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.438816][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.469763][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.500756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.531735][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.562657][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.593595][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.624555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.655491][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.686450][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.717395][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.748705][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.779637][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.810586][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.841490][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.872570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.903524][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.965347][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.996374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.027286][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.058231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.089225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.120195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.151138][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.182105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.213031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.244146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.275144][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.306161][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.337152][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.368199][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.399198][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.430244][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.461148][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.492115][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.523062][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.554134][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.585146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.616050][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.677825][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.708815][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.740196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.771150][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.802236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.833155][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.864179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.895191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.926273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.957198][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.988279][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.019213][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.050309][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.081251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.142946][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.174137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.205086][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.236282][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.267181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.298230][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.329175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.360287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.391252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.422263][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.453225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.484225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.515231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.546273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.577209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.608235][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.639160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.670173][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.701131][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.732198][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.763102][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.794035][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.825209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.856375][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.887241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.918216][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.949132][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.980256][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.011225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.042224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.073154][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.104136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.135061][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.166058][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.197021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.228026][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.289722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.320708][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.351704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.382674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.413687][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.444619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.475649][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.506692][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.537809][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.568784][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.599803][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.630747][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.661768][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.692706][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.723614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.754573][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.785618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.816580][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.847531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.878452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.909460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.940396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.971385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.002375][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.033471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.064394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.095408][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.126381][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.157401][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.188355][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.219374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.250311][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.281348][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.312313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.343296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.374265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.405158][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.466995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.498008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.529112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.560185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.591166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.622109][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.653065][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.684008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.715048][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.745970][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.776935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.807846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.838821][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.869733][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.900685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.931935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.962845][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.993737][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.024629][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.055550][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.086614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.117572][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.148617][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.179539][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.210522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.241448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.272521][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.303458][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.334484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.365406][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.396583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.427518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.458542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.489476][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.520521][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.551474][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.582509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.613562][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.644535][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.675501][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.706471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.737426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.768581][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.799502][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.830619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.861575][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.892509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.923541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.954623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.985554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.016589][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.047541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.109272][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.140298][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.171228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.202267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.233189][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.264155][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.295082][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.326034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.356993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.387984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.418874][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.449839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.480747][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.542426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.573414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.604346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.635386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.666386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.697379][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.728564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.759486][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.790532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.821487][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.852496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.883538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.914510][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.945459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.976407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.007360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.038315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.069296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.100233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.131151][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.162093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.193076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.224220][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.255202][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.286151][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.317066][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.347949][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.378934][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.409870][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.440817][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.471727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.502775][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.533709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.564704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.595601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.626520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.688493][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.719485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.750403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.781440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.812411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.843386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.874273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.905265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.936247][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.967123][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.998030][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.028972][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.059881][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.090825][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.121896][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.152962][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.183978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.214882][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.245925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.276842][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.307813][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.338723][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.369709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.400615][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.431585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.462612][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.493585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.524513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.555417][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.586364][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.617277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.648174][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.679078][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.709999][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.740984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.771980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.803068][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.834052][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.865026][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.895951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.926912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.957821][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.988731][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.019664][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.050724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.081660][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.112785][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.143710][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.174835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.205777][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.236680][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.267642][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.298669][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.329579][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.360608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.391541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.422526][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.453459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.484512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.515794][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.546719][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.577600][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.608583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.639503][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.670429][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.732301][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.793997][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.825051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.856191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.887125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.918055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.949015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.980048][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.010978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.042058][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.073009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.104090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.135012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.166024][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.196979][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.228007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.258935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.289938][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.320914][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.351973][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.382885][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.413848][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.444801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.475810][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.506716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.537685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.568706][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.599830][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.630715][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.661741][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.692677][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.723654][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.754658][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.785674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.816623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.847533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.878515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.909639][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.940618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.971579][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.002478][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.033411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.064380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.095346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.126492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.157474][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.188419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.219389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.250336][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.281292][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.312201][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.343228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.374139][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.405139][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.436103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.467087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.498097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.529046][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.559984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.590891][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.621796][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.652746][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.683704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.714813][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.745753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.776792][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.807803][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.838876][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.869860][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.900914][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.931894][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.962897][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.993833][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.024787][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.055745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.086739][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.117685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.148705][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.179615][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.210546][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.241468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.272473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.303429][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.334385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.365312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.396260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.427166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.458144][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.489147][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.520170][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.551105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.582068][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.612993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.644012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.674995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.705929][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.736882][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.767831][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.798793][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.829869][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.860820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.891882][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.922785][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.953766][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.984848][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.015834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.046756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.077854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.108858][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.139862][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.201540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.232467][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.263465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.266369][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:42.266426][MultiLaser][error] ERROR: No connection to laser range finder or connection lost!
[2021-07-28 01:52:42.266482][MultiLaser][error] ERROR: data connection error: 125
[2021-07-28 01:52:42.267706][MultiLaser][error] ERROR: Laser range finder disconnected. Trying to reconnect...
[2021-07-28 01:52:42.267762][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:42.294418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.325428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.356430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.387385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.418280][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.449632][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.480564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.511604][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.542517][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.573440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.604366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.635328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.666312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.697284][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.728236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.759186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.790150][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.821154][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.852071][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.883020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.913986][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.945015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.975983][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.007018][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.038033][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.069006][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.130680][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.161614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.192664][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.223593][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.254752][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.285692][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.316807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.347745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.378716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.409769][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.440803][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.471758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.502691][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.533609][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.564684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.595672][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.626711][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.657687][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.688875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.719822][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.750805][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.781767][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.812760][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.843728][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.874707][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.905722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.936671][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.967568][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.998461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.029374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.060424][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.091407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.122407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.153367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.184411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.215357][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.246338][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.277225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.308226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.339172][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.370183][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.401108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.432136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.463051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.493940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.524935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.556153][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.587141][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.618328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.649248][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.680232][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.711162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.772943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.803992][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.834920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.865966][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.896945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.927971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.958968][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.989995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.021017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.051886][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.082798][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.113868][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.144870][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.175864][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.237592][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.268540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.299591][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.330623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.338348][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:45.338391][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:52:45.361580][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.392524][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.423501][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.454756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.485742][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.516667][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.547694][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.578652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.609625][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.640547][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.671607][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.702548][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.733451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.764405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.795346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.826258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.857186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.888100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.919254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.950204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.981184][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.012095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.043120][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.074047][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.105006][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.135951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.166944][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.197926][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.228886][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.259943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.290961][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.321887][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.353076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.384105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.415017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.445948][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.476976][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.508062][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.539064][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.569987][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.601145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.632044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.663037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.693939][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.724971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.755900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.786785][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.817639][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.848620][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.879538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.910541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.941442][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.972414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.003311][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.034234][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.065208][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.096125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.127065][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.158044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.188985][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.219887][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.250828][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.281935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.312997][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.338523][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:47.343920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.374854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.405763][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.436700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.467658][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.498581][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.529926][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.560877][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.591804][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.622713][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.653716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.684722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.715660][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.746597][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.777791][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.808760][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.839771][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.870744][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.901840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.932790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.963818][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.994782][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.025809][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.056787][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.087774][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.118700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.149748][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.180687][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.211752][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.242674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.273690][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.304762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.335757][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.366656][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.397623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.410389][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:48.410446][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:52:48.428567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.459711][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.490640][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.521618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.552576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.583629][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.614593][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.676262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.707243][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.738246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.769311][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.800236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.831206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.862181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.893242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.924246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.955264][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.986243][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.017252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.048183][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.079225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.110191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.141112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.172372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.203283][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.234228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.265214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.296130][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.327090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.358057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.389141][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.420055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.451031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.481981][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.512912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.543800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.574753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.636382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.667387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.698331][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.729308][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.760350][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.791283][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.822192][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.853095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.884087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.915053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.946051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.977133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.008073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.039011][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.070329][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.101281][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.132404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.163346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.194421][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.225343][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.256313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.287250][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.318442][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.349361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.380251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.410543][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:50.411217][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.442218][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.473118][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.504019][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.535140][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.566073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.597017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.628013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.658920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.689870][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.720835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.751851][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.782805][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.813807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.844747][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.875727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.906670][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.937738][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.968693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.999976][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.030871][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.061846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.092789][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.123758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.154702][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.185634][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.216727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.247746][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.278665][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.309658][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.340578][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.371606][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.402520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.464730][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.482390][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:51.482444][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:52:51.495758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.526758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.557780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.588791][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.619755][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.650681][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.681629][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.713010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.743932][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.774948][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.805908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.836877][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.867861][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.929515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.960492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.991575][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.022574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.053563][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.084573][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.115512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.146538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.177876][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.208964][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.239952][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.270960][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.301950][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.332925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.394572][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.425528][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.456547][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.487554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.518550][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.549492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.580448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.611445][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.642546][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.673474][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.704450][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.735446][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.766448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.797414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.828344][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.859320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.890277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.921204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.952133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.983069][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.014040][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.045111][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.076079][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.106989][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.137968][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.169021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.200002][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.230936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.261863][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.292828][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.323847][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.354807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.385822][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.416810][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.447693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.478677][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.482570][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:53.509585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.540483][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.571568][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.602512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.633522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.664490][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.681044][MultiLaser][info] Connection to scanner at 192.168.192.100 succeed!
[2021-07-28 01:52:53.681072][Robokit][error] [Alarm][Error|52100|cannot receive laser data within 500 ms|0]
[2021-07-28 01:52:53.681102][MultiLaser][info] set sample and frequency
[2021-07-28 01:52:53.690607][MultiLaser][info] success set samples : 2800
[2021-07-28 01:52:53.695408][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.718598][MultiLaser][info] success set frequency : 30
[2021-07-28 01:52:53.726273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.757171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.788080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.819185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.850145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.881166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.905756][MultiLaser][info] Current scanner settings:
[2021-07-28 01:52:53.905777][MultiLaser][info] ============================================================
[2021-07-28 01:52:53.905784][MultiLaser][info] angular_fov : 360.000000
[2021-07-28 01:52:53.905790][MultiLaser][info] angular_resolution : 0.000100
[2021-07-28 01:52:53.905796][MultiLaser][info] contamination : 0
[2021-07-28 01:52:53.905802][MultiLaser][info] device_family : 3
[2021-07-28 01:52:53.905807][MultiLaser][info] emitter_type : 2
[2021-07-28 01:52:53.905812][MultiLaser][info] feature_flags : 
[2021-07-28 01:52:53.905817][MultiLaser][info] filter_error_handling : tolerant
[2021-07-28 01:52:53.905824][MultiLaser][info] filter_maximum_margin : 100
[2021-07-28 01:52:53.905834][MultiLaser][info] filter_remission_threshold : reflector_std
[2021-07-28 01:52:53.905843][MultiLaser][info] filter_type : none
[2021-07-28 01:52:53.905854][MultiLaser][info] filter_width : 4
[2021-07-28 01:52:53.905865][MultiLaser][info] gateway : 192.168.192.1
[2021-07-28 01:52:53.905875][MultiLaser][info] gateway_current : 192.168.192.1
[2021-07-28 01:52:53.905884][MultiLaser][info] hmi_application_bitmap : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[2021-07-28 01:52:53.905913][MultiLaser][info] hmi_application_text_1 : 
[2021-07-28 01:52:53.905921][MultiLaser][info] hmi_application_text_2 : 
[2021-07-28 01:52:53.905927][MultiLaser][info] hmi_button_lock : off
[2021-07-28 01:52:53.905934][MultiLaser][info] hmi_display_mode : static_logo
[2021-07-28 01:52:53.905940][MultiLaser][info] hmi_language : english
[2021-07-28 01:52:53.905947][MultiLaser][info] hmi_parameter_lock : off
[2021-07-28 01:52:53.905953][MultiLaser][info] hmi_static_logo : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////x/4/x/4/x/4/wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/////////////////////////wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/x/4/x/4/x/4/x/4/w/w/4fh/4fh/4AB/8AD/+AH//gf//gf//gf/////////////wAA/wAA/wAA/wAA/wAA/wAA/x44/x44/x44/x44/x44/x44/x44/x44/x44/x44/x/4/////z///z///wf//wD//wD//wAf/wAf/4AD/4AD/+AA/+AA/+Pg/+Pg/+MA/+AA/+AA/+AA/4AD/wAf/wD//wf//wf//z///////////////////////////////////////////////////////////////////////////////////
[2021-07-28 01:52:53.905960][MultiLaser][info] hmi_static_text_1 :                  IDEA
[2021-07-28 01:52:53.905966][MultiLaser][info] hmi_static_text_2 : 
[2021-07-28 01:52:53.905971][MultiLaser][info] ip_address : 192.168.192.100
[2021-07-28 01:52:53.905978][MultiLaser][info] ip_address_current : 192.168.192.100
[2021-07-28 01:52:53.905984][MultiLaser][info] ip_mode : static
[2021-07-28 01:52:53.905989][MultiLaser][info] ip_mode_current : static
[2021-07-28 01:52:53.905994][MultiLaser][info] lcm_detection_period : 5000
[2021-07-28 01:52:53.906002][MultiLaser][info] lcm_detection_sensitivity : disabled
[2021-07-28 01:52:53.906008][MultiLaser][info] lcm_num_sectors : 12
[2021-07-28 01:52:53.906014][MultiLaser][info] lcm_sector_enable : 
[2021-07-28 01:52:53.906020][MultiLaser][info] lcm_sector_error_flags : 0
[2021-07-28 01:52:53.906027][MultiLaser][info] lcm_sector_warn_flags : 0
[2021-07-28 01:52:53.906033][MultiLaser][info] load_indication : 0
[2021-07-28 01:52:53.906039][MultiLaser][info] locator_indication : off
[2021-07-28 01:52:53.906046][MultiLaser][info] mac_address : 000d810989d4
[2021-07-28 01:52:53.906052][MultiLaser][info] max_connections : 3
[2021-07-28 01:52:53.906058][MultiLaser][info] operating_mode : measure
[2021-07-28 01:52:53.906067][MultiLaser][info] operation_time : 70260
[2021-07-28 01:52:53.906072][MultiLaser][info] operation_time_scaled : 122828
[2021-07-28 01:52:53.906078][MultiLaser][info] part : 305986
[2021-07-28 01:52:53.906083][MultiLaser][info] power_cycles : 664
[2021-07-28 01:52:53.906089][MultiLaser][info] product : OMD30M-R2000-B23-V1V1D-HD-1L
[2021-07-28 01:52:53.906099][MultiLaser][info] radial_range_max : 30.000000
[2021-07-28 01:52:53.906135][MultiLaser][info] radial_range_min : 0.000000
[2021-07-28 01:52:53.906148][MultiLaser][info] radial_resolution : 0.001000
[2021-07-28 01:52:53.906155][MultiLaser][info] revision_fw : 1.60
[2021-07-28 01:52:53.906161][MultiLaser][info] revision_hw : 1.62
[2021-07-28 01:52:53.906167][MultiLaser][info] samples_per_scan : 2800
[2021-07-28 01:52:53.906178][MultiLaser][info] sampling_rate_max : 84000
[2021-07-28 01:52:53.906184][MultiLaser][info] sampling_rate_min : 100
[2021-07-28 01:52:53.906190][MultiLaser][info] scan_direction : ccw
[2021-07-28 01:52:53.906195][MultiLaser][info] scan_frequency : 30
[2021-07-28 01:52:53.906202][MultiLaser][info] scan_frequency_max : 50.000000
[2021-07-28 01:52:53.906207][MultiLaser][info] scan_frequency_measured : 30.100000
[2021-07-28 01:52:53.906216][MultiLaser][info] scan_frequency_min : 10.000000
[2021-07-28 01:52:53.906221][MultiLaser][info] serial : 40000088016603
[2021-07-28 01:52:53.906228][MultiLaser][info] status_flags : 0
[2021-07-28 01:52:53.906234][MultiLaser][info] subnet_mask : 255.255.255.0
[2021-07-28 01:52:53.906239][MultiLaser][info] subnet_mask_current : 255.255.255.0
[2021-07-28 01:52:53.906244][MultiLaser][info] system_time_raw : 1129749740865
[2021-07-28 01:52:53.906250][MultiLaser][info] temperature_current : 29
[2021-07-28 01:52:53.906257][MultiLaser][info] temperature_max : 67
[2021-07-28 01:52:53.906263][MultiLaser][info] temperature_min : 45
[2021-07-28 01:52:53.906270][MultiLaser][info] up_time : 4
[2021-07-28 01:52:53.906275][MultiLaser][info] user_notes : 
[2021-07-28 01:52:53.906281][MultiLaser][info] user_tag : OMDxxx-R2000 HD
[2021-07-28 01:52:53.906287][MultiLaser][info] vendor : Pepperl+Fuchs
[2021-07-28 01:52:53.906292][MultiLaser][info] ============================================================
[2021-07-28 01:52:53.906299][MultiLaser][info] Starting capturing: 
[2021-07-28 01:52:53.912137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.937272][MultiLaser][info] [Text][Connecting to TCP data channel at 192.168.192.100:51400 ... ]
[2021-07-28 01:52:53.942977][MultiLaser][info] OK
[2021-07-28 01:52:53.943078][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.973998][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:54.004909][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:54.024975][MCLoc][info] Scan data update recover
[2021-07-28 01:52:54.025036][Robokit][error] [Alarm][Error|52102|localization module cannot get laser data|0]
[2021-07-28 01:52:54.136289][DSPChassis][info] [Text][update hostErrState to false]
[2021-07-28 01:53:41.514062][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.799988 to -337.000000]
[2021-07-28 01:53:41.514138][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.799988 to -337.000000|7]
[2021-07-28 01:54:18.604235][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.500000 to -335.299988]
[2021-07-28 01:54:18.604267][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.500000 to -335.299988|8]
[2021-07-28 01:54:21.667392][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.299988 to -335.100006]
[2021-07-28 01:54:21.667431][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.299988 to -335.100006|9]
[2021-07-28 01:54:25.927634][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.000000 to -334.799988]
[2021-07-28 01:54:25.927680][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.000000 to -334.799988|10]
[2021-07-28 01:54:52.231148][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -334.899994 to -335.100006]
[2021-07-28 01:54:52.231207][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -334.899994 to -335.100006|11]
[2021-07-28 01:54:56.094395][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.200012 to -335.399994]
[2021-07-28 01:54:56.094445][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.200012 to -335.399994|12]
[2021-07-28 01:55:22.233909][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.299988 to -336.500000]
[2021-07-28 01:55:22.233966][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.299988 to -336.500000|13]
[2021-07-28 01:55:59.280307][Robokit][info] [Text][Robokit version: 3.2.4+release]
[2021-07-28 01:55:59.280369][Robokit][info] [Text][Used system memory: 0.400883 GB]
[2021-07-28 01:55:59.280466][Robokit][info] [Text][Free system memory: 3.3739 GB]
[2021-07-28 01:55:59.280540][Robokit][info] [Text][Robokit physical memory usage: 186.238 MB]
[2021-07-28 01:55:59.280621][Robokit][info] [Text][Robokit virtual memory usage: 4467.55 MB]
[2021-07-28 01:55:59.280688][Robokit][info] [Text][Robokit Max physical memory usage: 186.238 MB]
[2021-07-28 01:55:59.280755][Robokit][info] [Text][Robokit Max virtual memory usage: 4467.55 MB]
^C
root@srs:/usr/local/SeerRobotics/rbk# ./rbk.sh start

  Sentinel RMS Development Kit 9.5.0.0221 Initialization Demo Program
  Copyright (C) 2019 SafeNet, Inc.

1800  *1DD WUQE MF7W 9DLZ INFO :   [GPlannerAdapter:65]: gplanner status size use is 4160192
RUN  :   [LPlannerAdapter:44]: LocalPlannerAdapter size use status is 12884060
terminate called after throwing an instance of 'std::runtime_error'
  what():  bind: Address already in use
Quit (core dumped)
root@srs:/usr/local/SeerRobotics/rbk# sudo lsof -i -P -n | grep LISTEN
systemd-r  780 systemd-resolve   13u  IPv4  18295      0t0  TCP 127.0.0.53:53 (LISTEN)
node       847            root   21u  IPv6  25275      0t0  TCP *:80 (LISTEN)
robod      849            root    8u  IPv4  28016      0t0  TCP *:19208 (LISTEN)
rbk       1019            root  113u  IPv4  27901      0t0  TCP *:19204 (LISTEN)
rbk       1019            root  114u  IPv4  28773      0t0  TCP *:19205 (LISTEN)
rbk       1019            root  116u  IPv4  27903      0t0  TCP *:19207 (LISTEN)
rbk       1019            root  117u  IPv4  28775      0t0  TCP *:19206 (LISTEN)
rbk       1019            root  118u  IPv4  27335      0t0  TCP *:19210 (LISTEN)
rbk       1019            root  119u  IPv4  27996      0t0  TCP *:502 (LISTEN)
sshd      1058            root    3u  IPv4  28684      0t0  TCP *:22 (LISTEN)
sshd      1058            root    4u  IPv6  28686      0t0  TCP *:22 (LISTEN)
root@srs:/usr/local/SeerRobotics/rbk# kill -p 19208
bash: kill: p: invalid signal specification
root@srs:/usr/local/SeerRobotics/rbk# kill -p rpk
bash: kill: p: invalid signal specification
root@srs:/usr/local/SeerRobotics/rbk# kill -p 25275
bash: kill: p: invalid signal specification
root@srs:/usr/local/SeerRobotics/rbk# sudo lsof -i -P -n | grep LISTEN
systemd-r  780 systemd-resolve   13u  IPv4  18295      0t0  TCP 127.0.0.53:53 (LISTEN)
node       847            root   21u  IPv6  25275      0t0  TCP *:80 (LISTEN)
robod      849            root    8u  IPv4  28016      0t0  TCP *:19208 (LISTEN)
rbk       1019            root  113u  IPv4  27901      0t0  TCP *:19204 (LISTEN)
rbk       1019            root  114u  IPv4  28773      0t0  TCP *:19205 (LISTEN)
rbk       1019            root  116u  IPv4  27903      0t0  TCP *:19207 (LISTEN)
rbk       1019            root  117u  IPv4  28775      0t0  TCP *:19206 (LISTEN)
rbk       1019            root  118u  IPv4  27335      0t0  TCP *:19210 (LISTEN)
rbk       1019            root  119u  IPv4  27996      0t0  TCP *:502 (LISTEN)
sshd      1058            root    3u  IPv4  28684      0t0  TCP *:22 (LISTEN)
sshd      1058            root    4u  IPv6  28686      0t0  TCP *:22 (LISTEN)
root@srs:/usr/local/SeerRobotics/rbk# sudo kill -9 `sudo lsof -t -i:19208`
root@srs:/usr/local/SeerRobotics/rbk# sudo lsof -i -P -n | grep LISTEN
systemd-r  780 systemd-resolve   13u  IPv4  18295      0t0  TCP 127.0.0.53:53 (LISTEN)
node       847            root   21u  IPv6  25275      0t0  TCP *:80 (LISTEN)
rbk       1019            root  113u  IPv4  27901      0t0  TCP *:19204 (LISTEN)
rbk       1019            root  114u  IPv4  28773      0t0  TCP *:19205 (LISTEN)
rbk       1019            root  116u  IPv4  27903      0t0  TCP *:19207 (LISTEN)
rbk       1019            root  117u  IPv4  28775      0t0  TCP *:19206 (LISTEN)
rbk       1019            root  118u  IPv4  27335      0t0  TCP *:19210 (LISTEN)
rbk       1019            root  119u  IPv4  27996      0t0  TCP *:502 (LISTEN)
sshd      1058            root    3u  IPv4  28684      0t0  TCP *:22 (LISTEN)
sshd      1058            root    4u  IPv6  28686      0t0  TCP *:22 (LISTEN)
root@srs:/usr/local/SeerRobotics/rbk# sudo kill -9 `sudo lsof -t -i:19204`
root@srs:/usr/local/SeerRobotics/rbk# sudo kill -9 `sudo lsof -t -i:19205`

Usage:
 kill [options] <pid> [...]

Options:
 <pid> [...]            send signal to every <pid> listed
 -<signal>, -s, --signal <signal>
                        specify the <signal> to be sent
 -l, --list=[<signal>]  list all signal names, or convert one to a name
 -L, --table            list all signal names in a nice table

 -h, --help     display this help and exit
 -V, --version  output version information and exit

For more details see kill(1).
root@srs:/usr/local/SeerRobotics/rbk# sudo kill -9 `sudo lsof -t -i:19207`

Usage:
 kill [options] <pid> [...]

Options:
 <pid> [...]            send signal to every <pid> listed
 -<signal>, -s, --signal <signal>
                        specify the <signal> to be sent
 -l, --list=[<signal>]  list all signal names, or convert one to a name
 -L, --table            list all signal names in a nice table

 -h, --help     display this help and exit
 -V, --version  output version information and exit

For more details see kill(1).
root@srs:/usr/local/SeerRobotics/rbk# sudo lsof -i -P -n | grep LISTEN
systemd-r  780 systemd-resolve   13u  IPv4  18295      0t0  TCP 127.0.0.53:53 (LISTEN)
node       847            root   21u  IPv6  25275      0t0  TCP *:80 (LISTEN)
sshd      1058            root    3u  IPv4  28684      0t0  TCP *:22 (LISTEN)
sshd      1058            root    4u  IPv6  28686      0t0  TCP *:22 (LISTEN)
root@srs:/usr/local/SeerRobotics/rbk# sudo kill -9 `sudo lsof -t -i:80`
root@srs:/usr/local/SeerRobotics/rbk# ./rbk.sh start

  Sentinel RMS Development Kit 9.5.0.0221 Initialization Demo Program
  Copyright (C) 2019 SafeNet, Inc.

1800  *1DD WUQE MF7W 9DLZ INFO :   [GPlannerAdapter:65]: gplanner status size use is 4160192
RUN  :   [LPlannerAdapter:44]: LocalPlannerAdapter size use status is 12884060
No LandMark in The map!
^CSegmentation fault (core dumped)

root@srs:/usr/local/SeerRobotics/rbk# ./rbk.sh printlog
[2021-07-28 01:48:25.148679][Robokit][info] [Text][RoboKit Log Start...]
[2021-07-28 01:48:25.148783][Robokit][info] [Text][Robokit version: 3.2.4+release]
[2021-07-28 01:48:25.148827][Robokit][info] [Text][System memory      : 3.77478 GB]
[2021-07-28 01:48:25.148868][Robokit][info] [Text][Used system memory : 0.344135 GB]
[2021-07-28 01:48:25.148962][Robokit][info] [Text][Free system memory : 3.43064 GB]
[2021-07-28 01:48:25.149015][Robokit][info] [Text][Number CPU of cores: 4]
[2021-07-28 01:48:25.149046][Robokit][info] [Text][User Data Dir     : /usr/local/etc/.SeerRobotics/rbk/]
[2021-07-28 01:48:25.149059][Robokit][info] [Text][echoType 0x1800]
[2021-07-28 01:48:25.199575][Robokit][info] [Text][Read ./rbk.feature success]
[2021-07-28 01:48:25.213557][Robokit][info] [Text][echoid type: 0x1800     echoid: *1DD WUQE MF7W 9DLZ ]
[2021-07-28 01:48:25.285617][Robokit][info] [Text][# rbk_diff set activate success]
[2021-07-28 01:48:25.392954][Robokit][info] [Text][# rbk_omni activate fail with code: 210018]
[2021-07-28 01:48:25.528119][Robokit][info] [Text][# rbk_steer activate fail with code: 210018]
[2021-07-28 01:48:25.616756][Robokit][info] [Text][# rbk_multisteer activate fail with code: 210018]
[2021-07-28 01:48:25.711358][Robokit][info] [Text][# rbk_fork activate fail with code: 210018]
[2021-07-28 01:48:25.786081][Robokit][info] [Text][# rbk_pallet activate fail with code: 210018]
[2021-07-28 01:48:25.954353][Robokit][info] [Text][# rbk_pgv_loc activate fail with code: 210018]
[2021-07-28 01:48:26.127645][Robokit][info] [Text][# rbk_pgv_nav activate fail with code: 210018]
[2021-07-28 01:48:26.420941][Robokit][info] [Text][# rbk_spin activate fail with code: 210018]
[2021-07-28 01:48:26.468430][Robokit][info] [Text][# rbk_reflector activate fail with code: 210018]
[2021-07-28 01:48:26.675584][Robokit][info] [Text][# rbk_3dcamera activate fail with code: 210018]
[2021-07-28 01:48:26.717526][Robokit][info] [Text][# rbk_dynamic_nav activate fail with code: 210018]
[2021-07-28 01:48:26.727989][Robokit][info] [Text][Read rbk.error success]
[2021-07-28 01:48:26.802813][Robokit][info] [Text][md5: 602c4ab7d683b6bacd4fb05e2c9f7f21]
[2021-07-28 01:48:26.802895][Robokit][info] [Text][name: MP10S]
[2021-07-28 01:48:26.804083][Robokit][info] [Text][robot.cp md5: b27fc2e5143505200d5a90e5656b247d]
[2021-07-28 01:48:26.833332][Robokit][info] [Delegate][auto|NetProtocol|create]
[2021-07-28 01:48:26.833414][Robokit][info] [Delegate][manual|NetProtocol|create]
[2021-07-28 01:48:26.833437][Robokit][info] [Delegate][afd_lift|NetProtocol|create]
[2021-07-28 01:48:26.833463][Robokit][info] [Event][set_DI|NetProtocol|create]
[2021-07-28 01:48:26.833611][NetProtocol][info] [Service][setInitStatus|NetProtocol|create]
[2021-07-28 01:48:26.833671][NetProtocol][info] [Service][setRelocStatus|NetProtocol|create]
[2021-07-28 01:48:26.833692][NetProtocol][info] [Service][setLoadmapStatus|NetProtocol|create]
[2021-07-28 01:48:26.833726][NetProtocol][info] [Service][runTaskchain|NetProtocol|create]
[2021-07-28 01:48:26.833757][NetProtocol][info] [Service][release|NetProtocol|create]
[2021-07-28 01:48:26.833778][NetProtocol][info] [Service][require|NetProtocol|create]
[2021-07-28 01:48:26.833808][NetProtocol][info] [Service][uwb_follow|NetProtocol|create]
[2021-07-28 01:48:26.833841][NetProtocol][info] [Service][updateMoveTask|NetProtocol|create]
[2021-07-28 01:48:26.833993][NetProtocol][info] [Text][Robot Mac Address: 40623110507B]
[2021-07-28 01:48:26.834037][NetProtocol][info] [Text][wlan0 Mac Address: C0E4348C6271]
[2021-07-28 01:48:26.834347][NetProtocol][info] [Text][UUID: 3600250013504D3256313920]
[2021-07-28 01:48:26.834751][Robokit][info] [Initialized OK][NetProtocol]
[2021-07-28 01:48:26.850155][Robokit][info] [Initialized OK][RobotPosEKF]
[2021-07-28 01:48:26.864514][MapConstructor][info] [Service][sendMapImmediately|MapConstructor|create]
[2021-07-28 01:48:26.864608][MapConstructor][info] [Service][changeMap|MapConstructor|create]
[2021-07-28 01:48:26.864646][MapConstructor][info] [Service][reloadMap|MapConstructor|create]
[2021-07-28 01:48:26.864687][MapConstructor][info] [Service][getCurrentMapName|MapConstructor|create]
[2021-07-28 01:48:26.864721][Robokit][info] [Initialized OK][MapConstructor]
[2021-07-28 01:48:26.880499][Robokit][info] [Event][relocStarted|MCLoc|create]
[2021-07-28 01:48:26.880549][Robokit][info] [Event][relocFinished|MCLoc|create]
[2021-07-28 01:48:26.880573][Robokit][info] [Event][changeToOdoMode|MCLoc|create]
[2021-07-28 01:48:26.880612][Robokit][info] [Event][changeToNormalMode|MCLoc|create]
[2021-07-28 01:48:26.880633][Robokit][info] [Event][relocSuccessed|MCLoc|create]
[2021-07-28 01:48:26.880653][Robokit][info] [Event][relocFailed|MCLoc|create]
[2021-07-28 01:48:26.880716][MCLoc][info] [Service][getIsOnlyOdoMode|MCLoc|create]
[2021-07-28 01:48:26.880783][MCLoc][info] [Service][setOnlyOdoMode|MCLoc|create]
[2021-07-28 01:48:26.880822][MCLoc][info] [Service][relocService|MCLoc|create]
[2021-07-28 01:48:26.880856][MCLoc][info] [Service][refreshMCLocMap|MCLoc|create]
[2021-07-28 01:48:26.880889][MCLoc][info] [Service][reloadMapObj|MCLoc|create]
[2021-07-28 01:48:26.880924][MCLoc][info] [Service][startMCLocFromPoses|MCLoc|create]
[2021-07-28 01:48:26.880963][MCLoc][info] [Service][relocServiceFromPose|MCLoc|create]
[2021-07-28 01:48:26.880986][MCLoc][info] [Service][cancelReloc|MCLoc|create]
[2021-07-28 01:48:26.881006][MCLoc][info] [Service][testService|MCLoc|create]
[2021-07-28 01:48:26.881031][MCLoc][info] [Service][setCalibLaser|MCLoc|create]
[2021-07-28 01:48:26.881051][MCLoc][info] [Service][setLaserOdoStart|MCLoc|create]
[2021-07-28 01:48:26.881510][Robokit][info] [Initialized OK][MCLoc]
[2021-07-28 01:48:26.928900][MoveFactory][info] status size use is 14843092 10000
[2021-07-28 01:48:26.955800][MoveFactory][info] [Service][update_rbk.protocol.Message_MoveTask|MoveFactory|create]
[2021-07-28 01:48:26.957351][MoveFactory][info] [Service][suspendTask|MoveFactory|create]
[2021-07-28 01:48:26.957408][MoveFactory][info] [Service][resumeTask|MoveFactory|create]
[2021-07-28 01:48:26.957435][MoveFactory][info] [Service][cancelTask|MoveFactory|create]
[2021-07-28 01:48:26.957458][MoveFactory][info] [Service][setChargingIO|MoveFactory|create]
[2021-07-28 01:48:26.957477][MoveFactory][info] [Service][setAutoMode|MoveFactory|create]
[2021-07-28 01:48:26.957510][MoveFactory][info] [Service][startPatrol|MoveFactory|create]
[2021-07-28 01:48:26.957545][MoveFactory][info] [Service][getTargetPath|MoveFactory|create]
[2021-07-28 01:48:26.957581][MoveFactory][info] [Service][clearMoveTaskList|MoveFactory|create]
[2021-07-28 01:48:26.957648][MoveFactory][info] [Service][updateMoveTaskList|MoveFactory|create]
[2021-07-28 01:48:26.957695][MoveFactory][info] [Service][clearGoodsShape|MoveFactory|create]
[2021-07-28 01:48:26.957754][MoveFactory][info] [Service][setShelfShape|MoveFactory|create]
[2021-07-28 01:48:26.957802][Robokit][info] [Event][targetReached|MoveFactory|create]
[2021-07-28 01:48:26.957847][Robokit][info] [Event][needGyroCali|MoveFactory|create]
[2021-07-28 01:48:26.957888][Robokit][info] [Event][chargingStopped|MoveFactory|create]
[2021-07-28 01:48:26.957930][Robokit][info] [Event][ultrasonicChanged|MoveFactory|create]
[2021-07-28 01:48:26.957970][Robokit][info] [Event][fallingdownChanged|MoveFactory|create]
[2021-07-28 01:48:26.958009][Robokit][info] [Event][infraredChanged|MoveFactory|create]
[2021-07-28 01:48:26.958047][Robokit][info] [Event][chargingFailed|MoveFactory|create]
[2021-07-28 01:48:26.958086][Robokit][info] [Event][isBlocked|MoveFactory|create]
[2021-07-28 01:48:26.958174][Robokit][info] [Event][isNotBlocked|MoveFactory|create]
[2021-07-28 01:48:26.958221][Robokit][info] [Initialized OK][MoveFactory]
[2021-07-28 01:48:26.964583][OnlineMapLogger][info] [Service][startScanMap|OnlineMapLogger|create]
[2021-07-28 01:48:26.964675][OnlineMapLogger][info] [Service][stopScanMap|OnlineMapLogger|create]
[2021-07-28 01:48:26.964715][OnlineMapLogger][info] [Service][getScanMap|OnlineMapLogger|create]
[2021-07-28 01:48:26.964738][Robokit][info] [Initialized OK][OnlineMapLogger]
[2021-07-28 01:48:26.987533][SoundPlayer][info] [Service][play|SoundPlayer|create]
[2021-07-28 01:48:26.987629][SoundPlayer][info] [Service][pause|SoundPlayer|create]
[2021-07-28 01:48:26.987651][SoundPlayer][info] [Service][stop|SoundPlayer|create]
[2021-07-28 01:48:26.987678][SoundPlayer][info] [Service][resume|SoundPlayer|create]
[2021-07-28 01:48:26.987711][SoundPlayer][info] [Service][getStatus|SoundPlayer|create]
[2021-07-28 01:48:26.987743][SoundPlayer][info] [Service][getSoundName|SoundPlayer|create]
[2021-07-28 01:48:26.987772][SoundPlayer][info] [Service][getLoop|SoundPlayer|create]
[2021-07-28 01:48:26.987862][Robokit][info] [Initialized OK][SoundPlayer]
[2021-07-28 01:48:26.991241][TaskManager][info] [Service][setTaskList|TaskManager|create]
[2021-07-28 01:48:26.991325][TaskManager][info] [Service][suspend|TaskManager|create]
[2021-07-28 01:48:26.991349][TaskManager][info] [Service][resume|TaskManager|create]
[2021-07-28 01:48:26.991376][TaskManager][info] [Service][cancel|TaskManager|create]
[2021-07-28 01:48:26.991397][TaskManager][info] [Service][next|TaskManager|create]
[2021-07-28 01:48:26.991429][TaskManager][info] [Service][getDI|TaskManager|create]
[2021-07-28 01:48:26.991460][TaskManager][info] [Service][setDI|TaskManager|create]
[2021-07-28 01:48:26.991492][TaskManager][info] [Service][clearDI|TaskManager|create]
[2021-07-28 01:48:26.991568][Robokit][info] [Initialized OK][TaskManager]
[2021-07-28 01:48:26.996255][LaserSegmentation][info] [Service][look_for_shelf|LaserSegmentation|create]
[2021-07-28 01:48:26.996322][LaserSegmentation][info] [Service][look_for_leg|LaserSegmentation|create]
[2021-07-28 01:48:26.996348][LaserSegmentation][info] [Service][look_for_charger|LaserSegmentation|create]
[2021-07-28 01:48:26.996370][Robokit][info] [Initialized OK][LaserSegmentation]
[2021-07-28 01:48:27.002495][SensorFuser][info] [Service][insertObstacleInRobotFrame|SensorFuser|create]
[2021-07-28 01:48:27.002561][SensorFuser][info] [Service][insertObstacleInWorldFrame|SensorFuser|create]
[2021-07-28 01:48:27.002592][SensorFuser][info] [Service][removeAllObstacle|SensorFuser|create]
[2021-07-28 01:48:27.002636][SensorFuser][info] [Service][removeObstacle|SensorFuser|create]
[2021-07-28 01:48:27.002657][SensorFuser][info] [Service][clearPointCloudInRobotFrame|SensorFuser|create]
[2021-07-28 01:48:27.002673][SensorFuser][info] [Service][clearPointCloudInWorldFrame|SensorFuser|create]
[2021-07-28 01:48:27.002690][SensorFuser][info] [Service][recoverAllPointCloud|SensorFuser|create]
[2021-07-28 01:48:27.002712][SensorFuser][info] [Service][recoverPointCloud|SensorFuser|create]
[2021-07-28 01:48:27.002733][SensorFuser][info] [Service][clearReservedPoint|SensorFuser|create]
[2021-07-28 01:48:27.002752][SensorFuser][info] [Service][clearReservedDepthCameraPoint|SensorFuser|create]
[2021-07-28 01:48:27.002788][Robokit][info] [Initialized OK][SensorFuser]
[2021-07-28 01:48:27.005694][RecoFactory][info] [Service][RecognizeObject|RecoFactory|create]
[2021-07-28 01:48:27.005760][Robokit][info] [Initialized OK][RecoFactory]
[2021-07-28 01:48:28.322724][MultiDcamera][info] [Service][getCalibRes|MultiDcamera|create]
[2021-07-28 01:48:28.322834][MultiDcamera][info] [Service][getObjPos|MultiDcamera|create]
[2021-07-28 01:48:28.322857][MultiDcamera][info] [Service][getScanRange|MultiDcamera|create]
[2021-07-28 01:48:28.322945][MultiDcamera][info] [Service][getCalibImg|MultiDcamera|create]
[2021-07-28 01:48:28.323002][Robokit][info] [Initialized OK][MultiDcamera]
[2021-07-28 01:48:28.333068][CalibrationTask][info] [Service][getCalibList|CalibrationTask|create]
[2021-07-28 01:48:28.333146][CalibrationTask][info] [Service][setCalibTask|CalibrationTask|create]
[2021-07-28 01:48:28.333174][CalibrationTask][info] [Service][setCalibData|CalibrationTask|create]
[2021-07-28 01:48:28.333219][CalibrationTask][info] [Service][setManualCalibEnd|CalibrationTask|create]
[2021-07-28 01:48:28.333249][CalibrationTask][info] [Service][getCalibResultStr|CalibrationTask|create]
[2021-07-28 01:48:28.333269][CalibrationTask][info] [Service][clearCalibAll|CalibrationTask|create]
[2021-07-28 01:48:28.333287][CalibrationTask][info] [Service][clearCalib|CalibrationTask|create]
[2021-07-28 01:48:28.333309][CalibrationTask][info] [Service][cancelCalib|CalibrationTask|create]
[2021-07-28 01:48:28.333326][CalibrationTask][info] [Service][saveCalibResult|CalibrationTask|create]
[2021-07-28 01:48:28.333357][CalibrationTask][info] [Service][setRelocStatus|CalibrationTask|create]
[2021-07-28 01:48:28.346621][DSPChassis][info] [Service][calGyro|DSPChassis|create]
[2021-07-28 01:48:28.346706][DSPChassis][info] [Service][setDO|DSPChassis|create]
[2021-07-28 01:48:28.346729][DSPChassis][info] [Service][setVirtualDI|DSPChassis|create]
[2021-07-28 01:48:28.346761][DSPChassis][info] [Service][getFirmwareVersion|DSPChassis|create]
[2021-07-28 01:48:28.346784][DSPChassis][info] [Service][getUID|DSPChassis|create]
[2021-07-28 01:48:28.346806][DSPChassis][info] [Service][getGyroVersion|DSPChassis|create]
[2021-07-28 01:48:28.346834][DSPChassis][info] [Service][setWarningLight|DSPChassis|create]
[2021-07-28 01:48:28.346868][DSPChassis][info] [Service][setForkHeight|DSPChassis|create]
[2021-07-28 01:48:28.346890][DSPChassis][info] [Service][setForkForward|DSPChassis|create]
[2021-07-28 01:48:28.346908][DSPChassis][info] [Service][setRelayState|DSPChassis|create]
[2021-07-28 01:48:28.346927][DSPChassis][info] [Service][setSoftIOEMC|DSPChassis|create]
[2021-07-28 01:48:28.346947][DSPChassis][info] [Service][stopForkAction|DSPChassis|create]
[2021-07-28 01:48:28.346975][DSPChassis][info] [Service][reloadRfidTagValue|DSPChassis|create]
[2021-07-28 01:48:28.346996][DSPChassis][info] [Service][readHinsonRfidOnce|DSPChassis|create]
[2021-07-28 01:48:28.347022][DSPChassis][info] [Service][setUltrasonicValid|DSPChassis|create]
[2021-07-28 01:48:28.347052][DSPChassis][info] [Service][setDIValid|DSPChassis|create]
[2021-07-28 01:48:28.347084][DSPChassis][info] [Service][cleanCANOpenEncoder|DSPChassis|create]
[2021-07-28 01:48:28.347118][DSPChassis][info] [Service][DIValidStatus|DSPChassis|create]
[2021-07-28 01:48:28.347147][DSPChassis][info] [Service][DOStatus|DSPChassis|create]
[2021-07-28 01:48:28.347169][DSPChassis][info] [Service][setBatteryChargeRelay|DSPChassis|create]
[2021-07-28 01:48:28.347201][DSPChassis][info] [Service][setListeningMode|DSPChassis|create]
[2021-07-28 01:48:28.347236][DSPChassis][info] [Service][setMotorSpeed|DSPChassis|create]
[2021-07-28 01:48:28.347259][DSPChassis][info] [Service][setMotorPosition|DSPChassis|create]
[2021-07-28 01:48:28.347465][Robokit][info] [Event][gyro_cali_completed|DSPChassis|create]
[2021-07-28 01:48:28.347495][Robokit][info] [Event][emc_pressed|DSPChassis|create]
[2021-07-28 01:48:28.347517][Robokit][info] [Event][emc_released|DSPChassis|create]
[2021-07-28 01:48:28.347548][Robokit][info] [Event][di0_released|DSPChassis|create]
[2021-07-28 01:48:28.347569][Robokit][info] [Event][di1_released|DSPChassis|create]
[2021-07-28 01:48:28.347591][Robokit][info] [Event][di2_released|DSPChassis|create]
[2021-07-28 01:48:28.347612][Robokit][info] [Event][di3_released|DSPChassis|create]
[2021-07-28 01:48:28.347633][Robokit][info] [Event][di4_released|DSPChassis|create]
[2021-07-28 01:48:28.347655][Robokit][info] [Event][di5_released|DSPChassis|create]
[2021-07-28 01:48:28.347676][Robokit][info] [Event][di6_released|DSPChassis|create]
[2021-07-28 01:48:28.347696][Robokit][info] [Event][di7_released|DSPChassis|create]
[2021-07-28 01:48:28.347718][Robokit][info] [Event][di8_released|DSPChassis|create]
[2021-07-28 01:48:28.347738][Robokit][info] [Event][di9_released|DSPChassis|create]
[2021-07-28 01:48:28.347760][Robokit][info] [Event][di10_released|DSPChassis|create]
[2021-07-28 01:48:28.347782][Robokit][info] [Event][di11_released|DSPChassis|create]
[2021-07-28 01:48:28.347803][Robokit][info] [Event][di12_released|DSPChassis|create]
[2021-07-28 01:48:28.347822][Robokit][info] [Event][di13_released|DSPChassis|create]
[2021-07-28 01:48:28.347843][Robokit][info] [Event][di14_released|DSPChassis|create]
[2021-07-28 01:48:28.347864][Robokit][info] [Event][di15_released|DSPChassis|create]
[2021-07-28 01:48:30.371042][DSPChassis][info] [Text][UDP Config socket init success.]
[2021-07-28 01:48:30.371124][DSPChassis][info] [Text][get Model device type num  Command 40973]
[2021-07-28 01:48:30.371164][DSPChassis][info] [Text][try write through config udp socket ]
[2021-07-28 01:48:30.371466][DSPChassis][info] [Text][receive return]
[2021-07-28 01:48:30.371493][DSPChassis][info] [Text][Got device type num 9]
[2021-07-28 01:48:30.371511][DSPChassis][warning] [Text][try to send getModelCommand0]
[2021-07-28 01:48:30.371593][DSPChassis][info] [Text][get Model Command 40971]
[2021-07-28 01:48:30.372020][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.372442][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.372898][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.372922][DSPChassis][info] [Text][RCV upload json data 628]
[2021-07-28 01:48:30.373955][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.374608][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.375260][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.375914][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.376570][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.377224][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.377880][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.378505][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.379159][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.379781][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.380403][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.381059][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.381715][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.382371][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.383025][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.383680][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.384302][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.384959][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.385613][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.386272][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.386926][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.387579][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.388203][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.388857][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.389481][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.390203][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.390227][DSPChassis][info] [Text][RCV upload json data 7477]
[2021-07-28 01:48:30.392143][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.392661][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.393152][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.393642][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.394141][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.394626][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.395149][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.395641][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.396165][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.396688][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.396712][DSPChassis][info] [Text][RCV upload json data 2839]
[2021-07-28 01:48:30.397844][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.398299][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.398754][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.399277][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.399300][DSPChassis][info] [Text][RCV upload json data 1117]
[2021-07-28 01:48:30.400104][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.400589][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.400614][DSPChassis][info] [Text][RCV upload json data 351]
[2021-07-28 01:48:30.401247][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.401276][DSPChassis][info] [Text][RCV upload json data 229]
[2021-07-28 01:48:30.401838][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.402294][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.402319][DSPChassis][info] [Text][RCV upload json data 323]
[2021-07-28 01:48:30.402953][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.403408][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.403834][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.404324][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.404348][DSPChassis][info] [Text][RCV upload json data 945]
[2021-07-28 01:48:30.405084][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.405538][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.406029][DSPChassis][info] [Text][RCV RET PACK LEN 308]
[2021-07-28 01:48:30.406054][DSPChassis][info] [Text][RCV upload json data 675]
[2021-07-28 01:48:30.406375][DSPChassis][info] [Text][get Firmware model...]
[2021-07-28 01:48:30.406434][Robokit][info] [Initialized OK][DSPChassis]
[2021-07-28 01:48:30.440532][MultiLaser][info] [Service][setDataFilter|MultiLaser|create]
[2021-07-28 01:48:30.440657][Robokit][info] [Initialized OK][MultiLaser]
[2021-07-28 01:48:30.446885][SeerRoller][info] [Service][writeUserData|SeerRoller|create]
[2021-07-28 01:48:30.446969][SeerRoller][info] [Service][rollerFrontPreLoad|SeerRoller|create]
[2021-07-28 01:48:30.446992][SeerRoller][info] [Service][rollerFrontLoad|SeerRoller|create]
[2021-07-28 01:48:30.447019][SeerRoller][info] [Service][rollerFrontUnload|SeerRoller|create]
[2021-07-28 01:48:30.447040][SeerRoller][info] [Service][rollerFrontRoll|SeerRoller|create]
[2021-07-28 01:48:30.447056][SeerRoller][info] [Service][rollerBackPreLoad|SeerRoller|create]
[2021-07-28 01:48:30.447072][SeerRoller][info] [Service][rollerBackLoad|SeerRoller|create]
[2021-07-28 01:48:30.447090][SeerRoller][info] [Service][rollerBackUnload|SeerRoller|create]
[2021-07-28 01:48:30.447105][SeerRoller][info] [Service][rollerBackRoll|SeerRoller|create]
[2021-07-28 01:48:30.447125][SeerRoller][info] [Service][rollerLeftPreLoad|SeerRoller|create]
[2021-07-28 01:48:30.447142][SeerRoller][info] [Service][rollerLeftLoad|SeerRoller|create]
[2021-07-28 01:48:30.447160][SeerRoller][info] [Service][rollerLeftUnload|SeerRoller|create]
[2021-07-28 01:48:30.447178][SeerRoller][info] [Service][rollerLeftRoll|SeerRoller|create]
[2021-07-28 01:48:30.447195][SeerRoller][info] [Service][rollerRightPreLoad|SeerRoller|create]
[2021-07-28 01:48:30.447214][SeerRoller][info] [Service][rollerRightLoad|SeerRoller|create]
[2021-07-28 01:48:30.447238][SeerRoller][info] [Service][rollerRightUnload|SeerRoller|create]
[2021-07-28 01:48:30.447256][SeerRoller][info] [Service][rollerRightRoll|SeerRoller|create]
[2021-07-28 01:48:30.447273][SeerRoller][info] [Service][rollerStop|SeerRoller|create]
[2021-07-28 01:48:30.447304][SeerRoller][info] [Service][rollerFrontBackInverse|SeerRoller|create]
[2021-07-28 01:48:30.447327][SeerRoller][info] [Service][rollerLeftRightInverse|SeerRoller|create]
[2021-07-28 01:48:30.447347][SeerRoller][info] [Service][rollerLeftPass|SeerRoller|create]
[2021-07-28 01:48:30.447366][SeerRoller][info] [Service][rollerRightPass|SeerRoller|create]
[2021-07-28 01:48:30.447387][SeerRoller][info] [Service][jackLoad|SeerRoller|create]
[2021-07-28 01:48:30.447406][SeerRoller][info] [Service][jackUnload|SeerRoller|create]
[2021-07-28 01:48:30.447436][SeerRoller][info] [Service][jackHeight|SeerRoller|create]
[2021-07-28 01:48:30.447457][SeerRoller][info] [Service][jackStop|SeerRoller|create]
[2021-07-28 01:48:30.447476][SeerRoller][info] [Service][hookPreClamp|SeerRoller|create]
[2021-07-28 01:48:30.447494][SeerRoller][info] [Service][hookClamping|SeerRoller|create]
[2021-07-28 01:48:30.447512][SeerRoller][info] [Service][hookDetach|SeerRoller|create]
[2021-07-28 01:48:30.447530][SeerRoller][info] [Service][hookReset|SeerRoller|create]
[2021-07-28 01:48:30.447549][SeerRoller][info] [Service][hookAdjustToRecognized|SeerRoller|create]
[2021-07-28 01:48:30.447576][SeerRoller][info] [Service][hookStop|SeerRoller|create]
[2021-07-28 01:48:30.447738][Robokit][info] [Initialized OK][SeerRoller]
[2021-07-28 01:48:30.508582][NetProtocol][info] [Text][model updated]
[2021-07-28 01:48:30.508778][CalibrationTask][warning] laser parameters in .cp file: 0 0 0
[2021-07-28 01:48:30.508887][CalibrationTask][info] Update params because model file changed
[2021-07-28 01:48:30.509044][SeerRoller][info] [Text][model updated]
[2021-07-28 01:48:30.509268][Robokit][info] [PubSub][rbk.protocol.Message_SensorPointCloud|SensorFuser|MoveFactory|connect]
[2021-07-28 01:48:30.509305][Robokit][info] [PubSub][rbk.protocol.Message_Localization|MCLoc|SensorFuser|connect]
[2021-07-28 01:48:30.509326][Robokit][info] [PubSub][rbk.protocol.Message_Map|MapConstructor|SensorFuser|connect]
[2021-07-28 01:48:30.509345][Robokit][info] [PubSub][rbk.protocol.Message_VirtualLineList|MoveFactory|SensorFuser|connect]
[2021-07-28 01:48:30.509364][Robokit][info] [PubSub][rbk.protocol.Message_Debug|SensorFuser|QtDebugGui|connect]
[2021-07-28 01:48:30.509386][Robokit][info] [PubSub][rbk.protocol.Message_UserObject|SensorFuser|NetProtocol|connect]
[2021-07-28 01:48:30.509408][Robokit][info] [PubSub][rbk.protocol.Message_AllLasers|MultiLaser|SensorFuser|connect]
[2021-07-28 01:48:30.509436][Robokit][info] [PubSub][rbk.protocol.Message_AllLasers|MultiLaser|NetProtocol|connect]
[2021-07-28 01:48:30.509458][Robokit][info] [PubSub][rbk.protocol.Message_Map|MapConstructor|MoveFactory|connect]
[2021-07-28 01:48:30.509475][Robokit][info] [PubSub][rbk.protocol.Message_Map|MapConstructor|NetProtocol|connect]
[2021-07-28 01:48:30.509494][Robokit][info] [PubSub][rbk.protocol.Message_Localization|MCLoc|MoveFactory|connect]
[2021-07-28 01:48:30.509512][Robokit][info] [PubSub][rbk.protocol.Message_NavSpeed|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509533][Robokit][info] [PubSub][rbk.protocol.Message_Battery|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509554][Robokit][info] [PubSub][rbk.protocol.Message_DI|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509572][Robokit][info] [PubSub][rbk.protocol.Message_DO|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509593][Robokit][info] [PubSub][rbk.protocol.Message_Magnetic|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509612][Robokit][info] [PubSub][rbk.protocol.Message_RFID|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509638][Robokit][info] [PubSub][rbk.protocol.Message_Ultrasonic|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509659][Robokit][info] [PubSub][rbk.protocol.Message_Controller|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509680][Robokit][info] [PubSub][rbk.protocol.Message_Fork|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.509703][Robokit][info] [PubSub][rbk.protocol.Message_Ultrasonic|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.509722][Robokit][info] [PubSub][rbk.protocol.Message_Fork|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.509743][Robokit][info] [PubSub][rbk.protocol.Message_Ultrasonic|DSPChassis|SensorFuser|connect]
[2021-07-28 01:48:30.509766][Robokit][info] [PubSub][rbk.protocol.Message_DI|DSPChassis|SensorFuser|connect]
[2021-07-28 01:48:30.509787][Robokit][info] [PubSub][rbk.protocol.Message_Localization|MCLoc|LaserSegmentation|connect]
[2021-07-28 01:48:30.509807][Robokit][info] [PubSub][rbk.protocol.Message_AllLasers|MultiLaser|LaserSegmentation|connect]
[2021-07-28 01:48:30.509829][Robokit][info] [PubSub][rbk.protocol.Message_Debug|LaserSegmentation|QtDebugGui|connect]
[2021-07-28 01:48:30.509850][Robokit][info] [PubSub][rbk.protocol.Message_LaserSegResult|LaserSegmentation|MoveFactory|connect]
[2021-07-28 01:48:30.509871][Robokit][info] [PubSub][rbk.protocol.Message_Map|MapConstructor|MCLoc|connect]
[2021-07-28 01:48:30.509889][Robokit][info] [PubSub][rbk.protocol.Message_Odometer|RobotPosEKF|MCLoc|connect]
[2021-07-28 01:48:30.509910][Robokit][info] [PubSub][rbk.protocol.Message_NavSpeed|MoveFactory|NetProtocol|connect]
[2021-07-28 01:48:30.509931][Robokit][info] [PubSub][rbk.protocol.Message_Odometer|DSPChassis|RobotPosEKF|connect]
[2021-07-28 01:48:30.509953][Robokit][info] [PubSub][rbk.protocol.Message_IMU|DSPChassis|RobotPosEKF|connect]
[2021-07-28 01:48:30.509972][Robokit][info] [PubSub][rbk.protocol.Message_Map|MapConstructor|QtDebugGui|connect]
[2021-07-28 01:48:30.509993][Robokit][info] [PubSub][rbk.protocol.Message_Debug|MCLoc|QtDebugGui|connect]
[2021-07-28 01:48:30.510012][Robokit][info] [PubSub][rbk.protocol.Message_Debug|MoveFactory|QtDebugGui|connect]
[2021-07-28 01:48:30.510035][Robokit][info] [PubSub][rbk.protocol.Message_NavSpeed|MoveFactory|DSPChassis|connect]
[2021-07-28 01:48:30.510055][Robokit][info] [PubSub][rbk.protocol.Message_NavPath|MoveFactory|NetProtocol|connect]
[2021-07-28 01:48:30.510076][Robokit][info] [PubSub][rbk.protocol.Message_MoveStatus|MoveFactory|NetProtocol|connect]
[2021-07-28 01:48:30.510104][Robokit][info] [PubSub][rbk.protocol.Message_Localization|MCLoc|NetProtocol|connect]
[2021-07-28 01:48:30.510139][Robokit][info] [PubSub][rbk.protocol.Message_LiveRefPos|MCLoc|NetProtocol|connect]
[2021-07-28 01:48:30.510161][Robokit][info] [PubSub][rbk.protocol.Message_Battery|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510182][Robokit][info] [PubSub][rbk.protocol.Message_DI|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510202][Robokit][info] [PubSub][rbk.protocol.Message_DO|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510222][Robokit][info] [PubSub][rbk.protocol.Message_Controller|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510245][Robokit][info] [PubSub][rbk.protocol.Message_AllLasers|MultiLaser|OnlineMapLogger|connect]
[2021-07-28 01:48:30.510266][Robokit][info] [PubSub][rbk.protocol.Message_Odometer|RobotPosEKF|OnlineMapLogger|connect]
[2021-07-28 01:48:30.510287][Robokit][info] [PubSub][rbk.protocol.Message_Odometer|RobotPosEKF|MoveFactory|connect]
[2021-07-28 01:48:30.510308][Robokit][info] [PubSub][rbk.protocol.Message_Odometer|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510330][Robokit][info] [PubSub][rbk.protocol.Message_DI|DSPChassis|TaskManager|connect]
[2021-07-28 01:48:30.510352][Robokit][info] [PubSub][rbk.protocol.Message_RFID|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510371][Robokit][info] [PubSub][rbk.protocol.Message_IMU|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510392][Robokit][info] [PubSub][rbk.protocol.Message_IMU|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.510413][Robokit][info] [PubSub][rbk.protocol.Message_AllLasers|MultiLaser|MCLoc|connect]
[2021-07-28 01:48:30.510434][Robokit][info] [PubSub][rbk.protocol.Message_MoveStatus|MoveFactory|DSPChassis|connect]
[2021-07-28 01:48:30.510455][Robokit][info] [PubSub][rbk.protocol.Message_TaskStatus|TaskManager|NetProtocol|connect]
[2021-07-28 01:48:30.510479][Robokit][info] [PubSub][rbk.protocol.Message_Peripheral|SeerRoller|NetProtocol|connect]
[2021-07-28 01:48:30.510499][Robokit][info] [PubSub][rbk.protocol.Message_Roller|SeerRoller|NetProtocol|connect]
[2021-07-28 01:48:30.510521][Robokit][info] [PubSub][rbk.protocol.Message_Roller|SeerRoller|MoveFactory|connect]
[2021-07-28 01:48:30.510541][Robokit][info] [PubSub][rbk.protocol.Message_Jack|SeerRoller|NetProtocol|connect]
[2021-07-28 01:48:30.510562][Robokit][info] [PubSub][rbk.protocol.Message_Jack|SeerRoller|MoveFactory|connect]
[2021-07-28 01:48:30.510585][Robokit][info] [PubSub][rbk.protocol.Message_Hook|SeerRoller|NetProtocol|connect]
[2021-07-28 01:48:30.510606][Robokit][info] [PubSub][rbk.protocol.Message_Hook|SeerRoller|MoveFactory|connect]
[2021-07-28 01:48:30.510627][Robokit][info] [PubSub][rbk.protocol.Message_Hook|SeerRoller|QtDebugGui|connect]
[2021-07-28 01:48:30.510647][Robokit][info] [PubSub][rbk.protocol.Message_MoveStatus|MoveFactory|SeerRoller|connect]
[2021-07-28 01:48:30.510668][Robokit][info] [PubSub][rbk.protocol.Message_Jack|MoveFactory|NetProtocol|connect]
[2021-07-28 01:48:30.510688][Robokit][info] [PubSub][rbk.protocol.Message_Jack|MoveFactory|MoveFactory|connect]
[2021-07-28 01:48:30.510708][Robokit][info] [PubSub][rbk.protocol.Message_Jack|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510728][Robokit][info] [PubSub][rbk.protocol.Message_Jack|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.510750][Robokit][info] [PubSub][rbk.protocol.Message_PGV|DSPChassis|MoveFactory|connect]
[2021-07-28 01:48:30.510769][Robokit][info] [PubSub][rbk.protocol.Message_PGV|DSPChassis|MCLoc|connect]
[2021-07-28 01:48:30.510790][Robokit][info] [PubSub][rbk.protocol.Message_PGV|DSPChassis|NetProtocol|connect]
[2021-07-28 01:48:30.510814][Robokit][info] [PubSub][rbk.protocol.Message_Tag_position|MCLoc|NetProtocol|connect]
[2021-07-28 01:48:30.510834][Robokit][info] [PubSub][rbk.protocol.Message_AllCameraCloud|MultiDcamera|SensorFuser|connect]
[2021-07-28 01:48:30.510855][Robokit][info] [PubSub][rbk.protocol.Message_Localization|MCLoc|MultiDcamera|connect]
[2021-07-28 01:48:30.510877][Robokit][info] [PubSub][rbk.protocol.Message_Localization|MCLoc|DSPChassis|connect]
[2021-07-28 01:48:30.510898][Robokit][info] [PubSub][rbk.protocol.Message_MoveStatus|MoveFactory|CalibrationTask|connect]
[2021-07-28 01:48:30.510919][Robokit][info] [PubSub][rbk.protocol.Message_Localization|MCLoc|CalibrationTask|connect]
[2021-07-28 01:48:30.510939][Robokit][info] [PubSub][rbk.protocol.Message_Odometer|DSPChassis|CalibrationTask|connect]
[2021-07-28 01:48:30.510960][Robokit][info] [PubSub][rbk.protocol.Message_CalibStatus|CalibrationTask|NetProtocol|connect]
[2021-07-28 01:48:30.510982][Robokit][info] [PubSub][rbk.protocol.Message_ManualSpeed|NetProtocol|MoveFactory|connect]
[2021-07-28 01:48:30.511002][Robokit][info] [PubSub][rbk.protocol.Message_MoveTaskList|NetProtocol|MoveFactory|connect]
[2021-07-28 01:48:30.511022][Robokit][info] [PubSub][rbk.protocol.Message_Sound|SoundPlayer|MoveFactory|connect]
[2021-07-28 01:48:30.512496][SeerRoller][info] [Text][SeerRoller disabled]
[2021-07-28 01:48:30.512532][SeerRoller][info] [Text][SeerJack disabled]
[2021-07-28 01:48:30.512554][SeerRoller][info] [Text][SeerHook disabled]
[2021-07-28 01:48:30.525608][MapConstructor][info] [Text][Before make normal points unique: 978]
[2021-07-28 01:48:30.525742][MapConstructor][info] [Text][After make normal points unique: 978]
[2021-07-28 01:48:30.525764][MapConstructor][info] [Text][Before make rssi points unique: 0]
[2021-07-28 01:48:30.525777][MapConstructor][info] [Text][After make rssi points unique: 0]
[2021-07-28 01:48:30.525915][MapConstructor][info] [Text][Parse map 20210713140105885 success, md5: 4d900956fb909c1b0bfab417411eba54, normal md5: fe805164d3c0c0b11ebf6ea6a4eaf880]
[2021-07-28 01:48:30.527447][MCLoc][info] Reflector size : 0 found in map
[2021-07-28 01:48:31.512560][DSPChassis][info] [Text][UDP control socket init success.]
[2021-07-28 01:48:31.512721][DSPChassis][info] [Text][UDP Report Socket init success.]
[2021-07-28 01:48:31.512772][DSPChassis][info] [Text][UDP Warning Socket init success.]
[2021-07-28 01:48:32.512878][DSPChassis][info] [Text][UDP Config socket init success.]
[2021-07-28 01:48:32.513152][DSPChassis][warning] [Text][DSP has been reboot, DSP need get Model]
[2021-07-28 01:48:32.513276][Robokit][warning] [Alarm][Warning|54100|DSP reconfiging...|1]
[2021-07-28 01:48:33.519987][MoveFactory][info] model Differential has been actived
[2021-07-28 01:48:33.520552][MoveFactory][info] model Differential has been actived
[2021-07-28 01:48:33.564750][MoveFactory][info] [Text][model updated in movefactory]
[2021-07-28 01:48:33.564792][MoveFactory][info] [Text][calibration updated in movefactory]
[2021-07-28 01:48:35.513397][CalibrationTask][warning] laser parameters in .cp file: 0 0 0
[2021-07-28 01:48:35.513484][CalibrationTask][info] Read model params as the CalibrationTask plugin started
[2021-07-28 01:48:37.513414][DSPChassis][info] [Text][confirm version...]
[2021-07-28 01:48:37.513878][DSPChassis][info] [Text][get firmware version: 1.9.42]
[2021-07-28 01:48:37.513909][DSPChassis][info] [Text][Version match]
[2021-07-28 01:48:37.513922][DSPChassis][info] [Text][confirm Gyro Version...]
[2021-07-28 01:48:37.514413][DSPChassis][info] [Text][The Gyro Version is: f103-1.4.3]
[2021-07-28 01:48:37.514437][DSPChassis][info] [Text][query DIO num...]
[2021-07-28 01:48:37.515940][DSPChassis][info] [Text][confirm UID...]
[2021-07-28 01:48:37.516332][DSPChassis][info] ************************* THE EMBEDDED SYS UID *************************
[2021-07-28 01:48:37.516350][DSPChassis][info] [Text][************ 3600250013504D3256313920 ************]
[2021-07-28 01:48:37.516361][DSPChassis][info] ************************* THE EMBEDDED SYS UID *************************
[2021-07-28 01:48:37.516401][DSPChassis][info] [Text][get reset config data  Command 40974]
[2021-07-28 01:48:37.516695][DSPChassis][info] [Text][warning port: DeviceDemandConfig]
[2021-07-28 01:48:37.517235][DSPChassis][info] [Text][add deviceType Name...CAN]
[2021-07-28 01:48:37.517276][DSPChassis][info] [Text][add device ID 0 name CAN1]
[2021-07-28 01:48:37.517294][DSPChassis][info] [Text][Param ID 0 name canPort type comboParam]
[2021-07-28 01:48:37.517306][DSPChassis][info] [Text][deviceParam 0 is Combo]
[2021-07-28 01:48:37.517327][DSPChassis][info] [Text][add param key canPort value port1]
[2021-07-28 01:48:37.517339][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.517353][DSPChassis][info] [Text][Param ID 1 name baudrate type comboParam]
[2021-07-28 01:48:37.517362][DSPChassis][info] [Text][deviceParam 1 is Combo]
[2021-07-28 01:48:37.517370][DSPChassis][info] [Text][add param key baudrate value 250K]
[2021-07-28 01:48:37.517379][DSPChassis][info] [Text][deviceComboOption 4 is Selected]
[2021-07-28 01:48:37.517391][DSPChassis][info] [Text][Param ID 2 name basic type arrayParam]
[2021-07-28 01:48:37.517413][DSPChassis][info] [Text][deviceParam 2 is Array]
[2021-07-28 01:48:37.517433][DSPChassis][info] [Text][add bool param key terminalResistance value true]
[2021-07-28 01:48:37.517457][DSPChassis][info] [Text][{"name":"CAN","devices":[{"canPort":"port1","baudrate":"250K","terminalResistance":true}]}]
[2021-07-28 01:48:37.518177][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.518221][DSPChassis][info] [Text][add deviceType Name...DI]
[2021-07-28 01:48:37.518236][DSPChassis][info] [Text][add device ID 1 name DI1]
[2021-07-28 01:48:37.518253][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.518267][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.518284][DSPChassis][info] [Text][add uint32 param key id value 1]
[2021-07-28 01:48:37.518295][DSPChassis][info] [Text][add bool param key inverse value false]
[2021-07-28 01:48:37.518311][DSPChassis][info] [Text][add device ID 3 name DI3]
[2021-07-28 01:48:37.518324][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.518331][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.518339][DSPChassis][info] [Text][add uint32 param key id value 3]
[2021-07-28 01:48:37.518346][DSPChassis][info] [Text][add bool param key inverse value false]
[2021-07-28 01:48:37.518359][DSPChassis][info] [Text][add device ID 6 name DI6]
[2021-07-28 01:48:37.518369][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.518376][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.518385][DSPChassis][info] [Text][add uint32 param key id value 6]
[2021-07-28 01:48:37.518393][DSPChassis][info] [Text][add bool param key inverse value false]
[2021-07-28 01:48:37.518404][DSPChassis][info] [Text][add device ID 7 name DI7]
[2021-07-28 01:48:37.518414][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.518421][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.518429][DSPChassis][info] [Text][add uint32 param key id value 7]
[2021-07-28 01:48:37.518436][DSPChassis][info] [Text][add bool param key inverse value false]
[2021-07-28 01:48:37.518449][DSPChassis][info] [Text][add device ID 8 name DI8]
[2021-07-28 01:48:37.518460][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.518469][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.518478][DSPChassis][info] [Text][add uint32 param key id value 8]
[2021-07-28 01:48:37.518486][DSPChassis][info] [Text][add bool param key inverse value false]
[2021-07-28 01:48:37.518523][DSPChassis][info] [Text][{"name":"DI","devices":[{"id":1,"inverse":false},{"id":3,"inverse":false},{"id":6,"inverse":false},{"id":7,"inverse":false},{"id":8,"inverse":false}]}]
[2021-07-28 01:48:37.519562][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.519612][DSPChassis][info] [Text][add deviceType Name...DO]
[2021-07-28 01:48:37.519624][DSPChassis][info] [Text][add device ID 0 name DO0]
[2021-07-28 01:48:37.519637][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.519646][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.519654][DSPChassis][info] [Text][add uint32 param key id value 0]
[2021-07-28 01:48:37.519663][DSPChassis][info] [Text][add bool param key default value true]
[2021-07-28 01:48:37.519675][DSPChassis][info] [Text][add device ID 1 name DO1]
[2021-07-28 01:48:37.519684][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.519692][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.519700][DSPChassis][info] [Text][add uint32 param key id value 1]
[2021-07-28 01:48:37.519708][DSPChassis][info] [Text][add bool param key default value false]
[2021-07-28 01:48:37.519720][DSPChassis][info] [Text][add device ID 2 name DO2]
[2021-07-28 01:48:37.519733][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.519741][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.519749][DSPChassis][info] [Text][add uint32 param key id value 2]
[2021-07-28 01:48:37.519756][DSPChassis][info] [Text][add bool param key default value false]
[2021-07-28 01:48:37.519767][DSPChassis][info] [Text][add device ID 3 name DO3]
[2021-07-28 01:48:37.519776][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.519784][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.519792][DSPChassis][info] [Text][add uint32 param key id value 3]
[2021-07-28 01:48:37.519799][DSPChassis][info] [Text][add bool param key default value true]
[2021-07-28 01:48:37.519812][DSPChassis][info] [Text][add device ID 4 name DO4]
[2021-07-28 01:48:37.519823][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.519831][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.519838][DSPChassis][info] [Text][add uint32 param key id value 4]
[2021-07-28 01:48:37.519845][DSPChassis][info] [Text][add bool param key default value false]
[2021-07-28 01:48:37.519891][DSPChassis][info] [Text][add device ID 5 name DO5]
[2021-07-28 01:48:37.519903][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.519910][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.519918][DSPChassis][info] [Text][add uint32 param key id value 5]
[2021-07-28 01:48:37.519925][DSPChassis][info] [Text][add bool param key default value false]
[2021-07-28 01:48:37.519937][DSPChassis][info] [Text][add device ID 6 name DO6]
[2021-07-28 01:48:37.519950][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.519958][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.519965][DSPChassis][info] [Text][add uint32 param key id value 6]
[2021-07-28 01:48:37.519972][DSPChassis][info] [Text][add bool param key default value false]
[2021-07-28 01:48:37.519996][DSPChassis][info] [Text][{"name":"DO","devices":[{"id":0,"default":true},{"id":1,"default":false},{"id":2,"default":false},{"id":3,"default":true},{"id":4,"default":false},{"id":5,"default":false},{"id":6,"default":false}]}]
[2021-07-28 01:48:37.521160][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.521199][DSPChassis][info] [Text][add deviceType Name...EMC]
[2021-07-28 01:48:37.521216][DSPChassis][info] [Text][add device ID 0 name EMC]
[2021-07-28 01:48:37.521225][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.521235][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.521247][DSPChassis][info] [Text][add bool param key recycleControl value false]
[2021-07-28 01:48:37.521258][DSPChassis][info] [Text][add bool param key powerOffWhenCANError value false]
[2021-07-28 01:48:37.521265][DSPChassis][info] [Text][add bool param key cancelTask value true]
[2021-07-28 01:48:37.521279][DSPChassis][info] [Text][Param ID 1 name func type comboParam]
[2021-07-28 01:48:37.521287][DSPChassis][info] [Text][deviceParam 1 is Combo]
[2021-07-28 01:48:37.521297][DSPChassis][info] [Text][add param key func value driver IO EMC]
[2021-07-28 01:48:37.521304][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.521321][DSPChassis][info] [Text][{"name":"EMC","devices":[{"recycleControl":false,"powerOffWhenCANError":false,"cancelTask":true,"func":"driver IO EMC"}]}]
[2021-07-28 01:48:37.522454][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.522503][DSPChassis][info] [Text][add deviceType Name...RFID]
[2021-07-28 01:48:37.522518][DSPChassis][info] [Text][{"name":"RFID","devices":[]}]
[2021-07-28 01:48:37.523136][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.523200][DSPChassis][info] [Text][add deviceType Name...battery]
[2021-07-28 01:48:37.523238][DSPChassis][info] [Text][add device ID 0 name battery]
[2021-07-28 01:48:37.523250][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.523261][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.523272][DSPChassis][info] [Text][add int32 param key warningPercentage value -1]
[2021-07-28 01:48:37.523280][DSPChassis][info] [Text][add int32 param key errorPercentage value -1]
[2021-07-28 01:48:37.523288][DSPChassis][info] [Text][add int32 param key shutdownPercentage value -1]
[2021-07-28 01:48:37.523303][DSPChassis][info] [Text][Param ID 1 name brand type comboParam]
[2021-07-28 01:48:37.523320][DSPChassis][info] [Text][deviceParam 1 is Combo]
[2021-07-28 01:48:37.523334][DSPChassis][info] [Text][add param key brand value YiHe-XZ-Protocol1363]
[2021-07-28 01:48:37.523344][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.523363][DSPChassis][info] [Text][Param ID 2 name voltage type comboParam]
[2021-07-28 01:48:37.523373][DSPChassis][info] [Text][deviceParam 2 is Combo]
[2021-07-28 01:48:37.523380][DSPChassis][info] [Text][add param key voltage value 48V]
[2021-07-28 01:48:37.523388][DSPChassis][info] [Text][deviceComboOption 2 is Selected]
[2021-07-28 01:48:37.523398][DSPChassis][info] [Text][Param ID 3 name capacity type arrayParam]
[2021-07-28 01:48:37.523404][DSPChassis][info] [Text][deviceParam 3 is Array]
[2021-07-28 01:48:37.523412][DSPChassis][info] [Text][add double param key capacity value 24]
[2021-07-28 01:48:37.523433][DSPChassis][info] [Text][Param ID 4 name percentageCal type comboParam]
[2021-07-28 01:48:37.523443][DSPChassis][info] [Text][deviceParam 4 is Combo]
[2021-07-28 01:48:37.523450][DSPChassis][info] [Text][add param key percentageCal value byProtocol]
[2021-07-28 01:48:37.523456][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.523466][DSPChassis][info] [Text][Param ID 5 name type type comboParam]
[2021-07-28 01:48:37.523476][DSPChassis][info] [Text][deviceParam 5 is Combo]
[2021-07-28 01:48:37.523485][DSPChassis][info] [Text][add param key type value RS485]
[2021-07-28 01:48:37.523491][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.523499][DSPChassis][info] [Text][add bool param key terminator value false]
[2021-07-28 01:48:37.523514][DSPChassis][info] [Text][Param ID 6 name baudrate type comboParam]
[2021-07-28 01:48:37.523522][DSPChassis][info] [Text][deviceParam 6 is Combo]
[2021-07-28 01:48:37.523529][DSPChassis][info] [Text][add param key baudrate value 9600]
[2021-07-28 01:48:37.523536][DSPChassis][info] [Text][deviceComboOption 2 is Selected]
[2021-07-28 01:48:37.523564][DSPChassis][info] [Text][{"name":"battery","devices":[{"warningPercentage":-1,"errorPercentage":-1,"shutdownPercentage":-1,"brand":"YiHe-XZ-Protocol1363","voltage":"48V","capacity":24,"percentageCal":"byProtocol","type":"RS485","terminator":false,"baudrate":"9600"}]}]
[2021-07-28 01:48:37.524712][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.524772][DSPChassis][info] [Text][add deviceType Name...chassis]
[2021-07-28 01:48:37.524789][DSPChassis][info] [Text][add device ID 0 name chassis]
[2021-07-28 01:48:37.524798][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.524807][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.524817][DSPChassis][info] [Text][add string param key name value MP10S]
[2021-07-28 01:48:37.524828][DSPChassis][info] [Text][Param ID 1 name mode type comboParam]
[2021-07-28 01:48:37.524838][DSPChassis][info] [Text][deviceParam 1 is Combo]
[2021-07-28 01:48:37.524848][DSPChassis][info] [Text][add param key mode value differential]
[2021-07-28 01:48:37.524855][DSPChassis][info] [Text][deviceComboOption 1 is Selected]
[2021-07-28 01:48:37.524863][DSPChassis][info] [Text][add uint32 param key wheelNum value 2]
[2021-07-28 01:48:37.524878][DSPChassis][info] [Text][Param ID 2 name shape type comboParam]
[2021-07-28 01:48:37.524888][DSPChassis][info] [Text][deviceParam 2 is Combo]
[2021-07-28 01:48:37.524897][DSPChassis][info] [Text][add param key shape value rectangle]
[2021-07-28 01:48:37.524905][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.524913][DSPChassis][info] [Text][add double param key width value 0.735]
[2021-07-28 01:48:37.524928][DSPChassis][info] [Text][add double param key head value 0.945]
[2021-07-28 01:48:37.524937][DSPChassis][info] [Text][add double param key tail value 0.495]
[2021-07-28 01:48:37.524965][DSPChassis][info] [Text][{"name":"chassis","devices":[{"name":"MP10S","mode":"differential","wheelNum":2,"shape":"rectangle","width":0.735,"head":0.945,"tail":0.495}]}]
[2021-07-28 01:48:37.525889][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.525937][DSPChassis][info] [Text][add deviceType Name...fork]
[2021-07-28 01:48:37.525961][DSPChassis][info] [Text][{"name":"fork","devices":[]}]
[2021-07-28 01:48:37.526572][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.526610][DSPChassis][info] [Text][add deviceType Name...hook]
[2021-07-28 01:48:37.526629][DSPChassis][info] [Text][{"name":"hook","devices":[]}]
[2021-07-28 01:48:37.527229][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.527258][DSPChassis][info] [Text][add deviceType Name...jack]
[2021-07-28 01:48:37.527287][DSPChassis][info] [Text][{"name":"jack","devices":[]}]
[2021-07-28 01:48:37.527870][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.527921][DSPChassis][info] [Text][add deviceType Name...led]
[2021-07-28 01:48:37.527951][DSPChassis][info] [Text][{"name":"led","devices":[]}]
[2021-07-28 01:48:37.528564][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.528602][DSPChassis][info] [Text][add deviceType Name...magneticSensor]
[2021-07-28 01:48:37.528621][DSPChassis][info] [Text][{"name":"magneticSensor","devices":[]}]
[2021-07-28 01:48:37.529233][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.529339][DSPChassis][info] [Text][add deviceType Name...motor]
[2021-07-28 01:48:37.529392][DSPChassis][info] [Text][add device ID 0 name motor]
[2021-07-28 01:48:37.529408][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.529423][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.529440][DSPChassis][info] [Text][add double param key x value 0]
[2021-07-28 01:48:37.529456][DSPChassis][info] [Text][add double param key y value 0.2]
[2021-07-28 01:48:37.529478][DSPChassis][info] [Text][add double param key yaw value 0]
[2021-07-28 01:48:37.529489][DSPChassis][info] [Text][add uint32 param key canID value 1]
[2021-07-28 01:48:37.529498][DSPChassis][info] [Text][add uint32 param key maxRPM value 3000]
[2021-07-28 01:48:37.529507][DSPChassis][info] [Text][add bool param key inverse value true]
[2021-07-28 01:48:37.529515][DSPChassis][info] [Text][add uint32 param key encoderLine value 2500]
[2021-07-28 01:48:37.529529][DSPChassis][info] [Text][Param ID 1 name canPort type comboParam]
[2021-07-28 01:48:37.529537][DSPChassis][info] [Text][deviceParam 1 is Combo]
[2021-07-28 01:48:37.529547][DSPChassis][info] [Text][add param key canPort value port1]
[2021-07-28 01:48:37.529553][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.529570][DSPChassis][info] [Text][Param ID 2 name brand type comboParam]
[2021-07-28 01:48:37.529591][DSPChassis][info] [Text][deviceParam 2 is Combo]
[2021-07-28 01:48:37.529618][DSPChassis][info] [Text][add param key brand value Copley-ADP-CANOpen]
[2021-07-28 01:48:37.529628][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.529665][DSPChassis][info] [Text][Param ID 3 name func type comboParam]
[2021-07-28 01:48:37.529703][DSPChassis][info] [Text][deviceParam 3 is Combo]
[2021-07-28 01:48:37.529739][DSPChassis][info] [Text][add param key func value walk]
[2021-07-28 01:48:37.529754][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.529765][DSPChassis][info] [Text][add double param key wheelRadius value 0.04]
[2021-07-28 01:48:37.529777][DSPChassis][info] [Text][add double param key reductionRatio value 16]
[2021-07-28 01:48:37.529788][DSPChassis][info] [Text][add double param key minimumSpeed value 0.05]
[2021-07-28 01:48:37.529841][DSPChassis][info] [Text][Param ID 4 name outEncoderBrand type comboParam]
[2021-07-28 01:48:37.529853][DSPChassis][info] [Text][deviceParam 4 is Combo]
[2021-07-28 01:48:37.529863][DSPChassis][info] [Text][add param key outEncoderBrand value none]
[2021-07-28 01:48:37.529870][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.529881][DSPChassis][info] [Text][Param ID 5 name outEncoder type arrayParam]
[2021-07-28 01:48:37.529889][DSPChassis][info] [Text][deviceParam 5 is Array]
[2021-07-28 01:48:37.529897][DSPChassis][info] [Text][add uint32 param key outEncoderID value 1]
[2021-07-28 01:48:37.529905][DSPChassis][info] [Text][Param ID 6 name outEncoderPort type comboParam]
[2021-07-28 01:48:37.529913][DSPChassis][info] [Text][deviceParam 6 is Combo]
[2021-07-28 01:48:37.529920][DSPChassis][info] [Text][add param key outEncoderPort value port1]
[2021-07-28 01:48:37.529927][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.529937][DSPChassis][info] [Text][Param ID 7 name resetMode type comboParam]
[2021-07-28 01:48:37.529945][DSPChassis][info] [Text][deviceParam 7 is Combo]
[2021-07-28 01:48:37.529954][DSPChassis][info] [Text][add param key resetMode value none]
[2021-07-28 01:48:37.529961][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.530012][DSPChassis][info] [Text][add device ID 1 name motor1]
[2021-07-28 01:48:37.530023][DSPChassis][info] [Text][Param ID 0 name basic type arrayParam]
[2021-07-28 01:48:37.530034][DSPChassis][info] [Text][deviceParam 0 is Array]
[2021-07-28 01:48:37.530048][DSPChassis][info] [Text][add double param key x value 0]
[2021-07-28 01:48:37.530060][DSPChassis][info] [Text][add double param key y value -0.2]
[2021-07-28 01:48:37.530069][DSPChassis][info] [Text][add double param key yaw value 0]
[2021-07-28 01:48:37.530077][DSPChassis][info] [Text][add uint32 param key canID value 2]
[2021-07-28 01:48:37.530085][DSPChassis][info] [Text][add uint32 param key maxRPM value 3000]
[2021-07-28 01:48:37.530092][DSPChassis][info] [Text][add bool param key inverse value true]
[2021-07-28 01:48:37.530099][DSPChassis][info] [Text][add uint32 param key encoderLine value 2500]
[2021-07-28 01:48:37.530128][DSPChassis][info] [Text][Param ID 1 name canPort type comboParam]
[2021-07-28 01:48:37.530138][DSPChassis][info] [Text][deviceParam 1 is Combo]
[2021-07-28 01:48:37.530146][DSPChassis][info] [Text][add param key canPort value port1]
[2021-07-28 01:48:37.530153][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.530170][DSPChassis][info] [Text][Param ID 2 name brand type comboParam]
[2021-07-28 01:48:37.530187][DSPChassis][info] [Text][deviceParam 2 is Combo]
[2021-07-28 01:48:37.530206][DSPChassis][info] [Text][add param key brand value Copley-ADP-CANOpen]
[2021-07-28 01:48:37.530216][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.530249][DSPChassis][info] [Text][Param ID 3 name func type comboParam]
[2021-07-28 01:48:37.530307][DSPChassis][info] [Text][deviceParam 3 is Combo]
[2021-07-28 01:48:37.530338][DSPChassis][info] [Text][add param key func value walk]
[2021-07-28 01:48:37.530357][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.530369][DSPChassis][info] [Text][add double param key wheelRadius value 0.04]
[2021-07-28 01:48:37.530382][DSPChassis][info] [Text][add double param key reductionRatio value 16]
[2021-07-28 01:48:37.530393][DSPChassis][info] [Text][add double param key minimumSpeed value 0.05]
[2021-07-28 01:48:37.530438][DSPChassis][info] [Text][Param ID 4 name outEncoderBrand type comboParam]
[2021-07-28 01:48:37.530449][DSPChassis][info] [Text][deviceParam 4 is Combo]
[2021-07-28 01:48:37.530470][DSPChassis][info] [Text][add param key outEncoderBrand value none]
[2021-07-28 01:48:37.530476][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.530485][DSPChassis][info] [Text][Param ID 5 name outEncoder type arrayParam]
[2021-07-28 01:48:37.530491][DSPChassis][info] [Text][deviceParam 5 is Array]
[2021-07-28 01:48:37.530500][DSPChassis][info] [Text][add uint32 param key outEncoderID value 1]
[2021-07-28 01:48:37.530510][DSPChassis][info] [Text][Param ID 6 name outEncoderPort type comboParam]
[2021-07-28 01:48:37.530518][DSPChassis][info] [Text][deviceParam 6 is Combo]
[2021-07-28 01:48:37.530524][DSPChassis][info] [Text][add param key outEncoderPort value port1]
[2021-07-28 01:48:37.530532][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.530540][DSPChassis][info] [Text][Param ID 7 name resetMode type comboParam]
[2021-07-28 01:48:37.530547][DSPChassis][info] [Text][deviceParam 7 is Combo]
[2021-07-28 01:48:37.530554][DSPChassis][info] [Text][add param key resetMode value none]
[2021-07-28 01:48:37.530561][DSPChassis][info] [Text][deviceComboOption 0 is Selected]
[2021-07-28 01:48:37.530634][DSPChassis][info] [Text][{"name":"motor","devices":[{"x":0,"y":0.2,"yaw":0,"canID":1,"maxRPM":3000,"inverse":true,"encoderLine":2500,"canPort":"port1","brand":"Copley-ADP-CANOpen","func":"walk","wheelRadius":0.04,"reductionRatio":16,"minimumSpeed":0.05,"outEncoderBrand":"none","outEncoderID":1,"outEncoderPort":"port1","resetMode":"none"},{"x":0,"y":-0.2,"yaw":0,"canID":2,"maxRPM":3000,"inverse":true,"encoderLine":2500,"canPort":"port1","brand":"Copley-ADP-CANOpen","func":"walk","wheelRadius":0.04,"reductionRatio":16,"minimumSpeed":0.05,"outEncoderBrand":"none","outEncoderID":1,"outEncoderPort":"port1","resetMode":"none"}]}]
[2021-07-28 01:48:37.531077][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.531340][DSPChassis][info] [Text][Model configure Packet...1]
[2021-07-28 01:48:37.534430][DSPChassis][info] [Text][Model configure Packet...2]
[2021-07-28 01:48:37.534511][DSPChassis][info] [Text][add deviceType Name...pgv]
[2021-07-28 01:48:37.534545][DSPChassis][info] [Text][{"name":"pgv","devices":[]}]
[2021-07-28 01:48:37.534746][DSPChassis][info] [Text][task 9 use 2.904762 ms to run]
[2021-07-28 01:48:37.534780][Robokit][warning] [Alarm][Warning|54021|task 9 use 2.904762 ms to run|1]
[2021-07-28 01:48:37.535207][Robokit][warning] [Alarm][Warning|54021|task 9 use 2.904762 ms to run|0]
[2021-07-28 01:48:37.535598][DSPChassis][info] [Text][Motor in NMT process]
[2021-07-28 01:48:37.535622][Robokit][warning] [Alarm][Warning|54301|Motor in NMT process|1]
[2021-07-28 01:48:37.536088][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.536136][DSPChassis][info] [Text][add deviceType Name...sonic]
[2021-07-28 01:48:37.536161][DSPChassis][info] [Text][{"name":"sonic","devices":[]}]
[2021-07-28 01:48:37.536781][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.536819][DSPChassis][info] [Text][add deviceType Name...soundplayer]
[2021-07-28 01:48:37.536840][DSPChassis][info] [Text][{"name":"soundplayer","devices":[]}]
[2021-07-28 01:48:37.537485][DSPChassis][info] [Text][Model configure Packet...0]
[2021-07-28 01:48:37.537846][DSPChassis][info] [Text][Config DSP Chassis success]
[2021-07-28 01:48:37.580875][DSPChassis][info] [Text][warning port: Copley only velocity loop]
[2021-07-28 01:48:37.581381][DSPChassis][info] [Text][warning port: Copley only velocity loop]
[2021-07-28 01:48:37.610021][DSPChassis][info] [Text][Controller Emergency Stop!]
[2021-07-28 01:48:37.610054][Robokit][warning] [Alarm][Warning|54004|Controller Emergency Stop!|1]
[2021-07-28 01:48:37.610350][DSPChassis][info] [Text][Motor is calibrating]
[2021-07-28 01:48:37.610372][Robokit][warning] [Alarm][Warning|54301|Motor is calibrating|2]
[2021-07-28 01:48:37.610969][Robokit][warning] [Alarm][Warning|54301|Motor is calibrating|0]
[2021-07-28 01:48:40.512645][MultiLaser][info] typeName = PepperlR2000-HD-TCP
[2021-07-28 01:48:40.512709][MultiLaser][info] [Text][Laser Device 0: laser init!!]
[2021-07-28 01:48:40.512926][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:48:40.515181][NetProtocol][info] [Text][DSP init completed, got UUID: 3600250013504D3256313920, i: 0]
[2021-07-28 01:48:40.515598][MCLoc][info] [Event][relocStarted|MCLoc]
[2021-07-28 01:48:40.515672][NetProtocol][info] [Delegate][manual|NetProtocol]
[2021-07-28 01:48:40.515417][NetProtocol][info] [Text][Starting status API server on :19204]
[2021-07-28 01:48:40.515917][NetProtocol][info] [Text][DNSServiceRegister: Robokit:srs:19204._robokitV2._tcp.local:19204]
[2021-07-28 01:48:40.515902][NetProtocol][info] [Text][Starting other API server on :19210]
[2021-07-28 01:48:40.516988][NetProtocol][info] [Text][Starting config API server on :19207]
[2021-07-28 01:48:40.517075][NetProtocol][info] [Text][Starting task API server on :19206]
[2021-07-28 01:48:40.517152][NetProtocol][info] [Text][Starting control API server on :19205]
[2021-07-28 01:48:40.535912][Robokit][warning] [PubSub][rbk.protocol.Message_ManualSpeed|NetProtocol|MoveFactory|connect failed, already connected]
[2021-07-28 01:48:40.715026][MultiLaser][info] Connection to scanner at 192.168.192.100 succeed!
[2021-07-28 01:48:40.715059][MultiLaser][info] set sample and frequency
[2021-07-28 01:48:40.724562][MultiLaser][info] success set samples : 2800
[2021-07-28 01:48:40.752501][MultiLaser][info] success set frequency : 30
[2021-07-28 01:48:40.935888][MultiLaser][info] Current scanner settings:
[2021-07-28 01:48:40.935912][MultiLaser][info] ============================================================
[2021-07-28 01:48:40.935920][MultiLaser][info] angular_fov : 360.000000
[2021-07-28 01:48:40.935941][MultiLaser][info] angular_resolution : 0.000100
[2021-07-28 01:48:40.935950][MultiLaser][info] contamination : 0
[2021-07-28 01:48:40.935956][MultiLaser][info] device_family : 3
[2021-07-28 01:48:40.935961][MultiLaser][info] emitter_type : 2
[2021-07-28 01:48:40.935967][MultiLaser][info] feature_flags : 
[2021-07-28 01:48:40.935974][MultiLaser][info] filter_error_handling : tolerant
[2021-07-28 01:48:40.935981][MultiLaser][info] filter_maximum_margin : 100
[2021-07-28 01:48:40.935987][MultiLaser][info] filter_remission_threshold : reflector_std
[2021-07-28 01:48:40.935994][MultiLaser][info] filter_type : none
[2021-07-28 01:48:40.936000][MultiLaser][info] filter_width : 4
[2021-07-28 01:48:40.936020][MultiLaser][info] gateway : 192.168.192.1
[2021-07-28 01:48:40.936027][MultiLaser][info] gateway_current : 192.168.192.1
[2021-07-28 01:48:40.936033][MultiLaser][info] hmi_application_bitmap : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[2021-07-28 01:48:40.936039][MultiLaser][info] hmi_application_text_1 : 
[2021-07-28 01:48:40.936045][MultiLaser][info] hmi_application_text_2 : 
[2021-07-28 01:48:40.936051][MultiLaser][info] hmi_button_lock : off
[2021-07-28 01:48:40.936057][MultiLaser][info] hmi_display_mode : static_logo
[2021-07-28 01:48:40.936062][MultiLaser][info] hmi_language : english
[2021-07-28 01:48:40.936067][MultiLaser][info] hmi_parameter_lock : off
[2021-07-28 01:48:40.936075][MultiLaser][info] hmi_static_logo : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////x/4/x/4/x/4/wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/////////////////////////wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/x/4/x/4/x/4/x/4/w/w/4fh/4fh/4AB/8AD/+AH//gf//gf//gf/////////////wAA/wAA/wAA/wAA/wAA/wAA/x44/x44/x44/x44/x44/x44/x44/x44/x44/x44/x/4/////z///z///wf//wD//wD//wAf/wAf/4AD/4AD/+AA/+AA/+Pg/+Pg/+MA/+AA/+AA/+AA/4AD/wAf/wD//wf//wf//z///////////////////////////////////////////////////////////////////////////////////
[2021-07-28 01:48:40.936081][MultiLaser][info] hmi_static_text_1 :                  IDEA
[2021-07-28 01:48:40.936087][MultiLaser][info] hmi_static_text_2 : 
[2021-07-28 01:48:40.936094][MultiLaser][info] ip_address : 192.168.192.100
[2021-07-28 01:48:40.936099][MultiLaser][info] ip_address_current : 192.168.192.100
[2021-07-28 01:48:40.936105][MultiLaser][info] ip_mode : static
[2021-07-28 01:48:40.936111][MultiLaser][info] ip_mode_current : static
[2021-07-28 01:48:40.936116][MultiLaser][info] lcm_detection_period : 5000
[2021-07-28 01:48:40.936121][MultiLaser][info] lcm_detection_sensitivity : disabled
[2021-07-28 01:48:40.936126][MultiLaser][info] lcm_num_sectors : 12
[2021-07-28 01:48:40.936131][MultiLaser][info] lcm_sector_enable : 
[2021-07-28 01:48:40.936136][MultiLaser][info] lcm_sector_error_flags : 0
[2021-07-28 01:48:40.936141][MultiLaser][info] lcm_sector_warn_flags : 0
[2021-07-28 01:48:40.936150][MultiLaser][info] load_indication : 0
[2021-07-28 01:48:40.936155][MultiLaser][info] locator_indication : off
[2021-07-28 01:48:40.936162][MultiLaser][info] mac_address : 000d810989d4
[2021-07-28 01:48:40.936168][MultiLaser][info] max_connections : 3
[2021-07-28 01:48:40.936173][MultiLaser][info] operating_mode : measure
[2021-07-28 01:48:40.936181][MultiLaser][info] operation_time : 70260
[2021-07-28 01:48:40.936187][MultiLaser][info] operation_time_scaled : 122828
[2021-07-28 01:48:40.936192][MultiLaser][info] part : 305986
[2021-07-28 01:48:40.936200][MultiLaser][info] power_cycles : 664
[2021-07-28 01:48:40.936205][MultiLaser][info] product : OMD30M-R2000-B23-V1V1D-HD-1L
[2021-07-28 01:48:40.936213][MultiLaser][info] radial_range_max : 30.000000
[2021-07-28 01:48:40.936253][MultiLaser][info] radial_range_min : 0.000000
[2021-07-28 01:48:40.936261][MultiLaser][info] radial_resolution : 0.001000
[2021-07-28 01:48:40.936266][MultiLaser][info] revision_fw : 1.60
[2021-07-28 01:48:40.936272][MultiLaser][info] revision_hw : 1.62
[2021-07-28 01:48:40.936278][MultiLaser][info] samples_per_scan : 2800
[2021-07-28 01:48:40.936284][MultiLaser][info] sampling_rate_max : 84000
[2021-07-28 01:48:40.936289][MultiLaser][info] sampling_rate_min : 100
[2021-07-28 01:48:40.936295][MultiLaser][info] scan_direction : ccw
[2021-07-28 01:48:40.936300][MultiLaser][info] scan_frequency : 30
[2021-07-28 01:48:40.936308][MultiLaser][info] scan_frequency_max : 50.000000
[2021-07-28 01:48:40.936314][MultiLaser][info] scan_frequency_measured : 30.000000
[2021-07-28 01:48:40.936319][MultiLaser][info] scan_frequency_min : 10.000000
[2021-07-28 01:48:40.936326][MultiLaser][info] serial : 40000088016603
[2021-07-28 01:48:40.936332][MultiLaser][info] status_flags : 0
[2021-07-28 01:48:40.936338][MultiLaser][info] subnet_mask : 255.255.255.0
[2021-07-28 01:48:40.936346][MultiLaser][info] subnet_mask_current : 255.255.255.0
[2021-07-28 01:48:40.936364][MultiLaser][info] system_time_raw : 43326083370
[2021-07-28 01:48:40.936370][MultiLaser][info] temperature_current : 25
[2021-07-28 01:48:40.936376][MultiLaser][info] temperature_max : 67
[2021-07-28 01:48:40.936382][MultiLaser][info] temperature_min : 45
[2021-07-28 01:48:40.936390][MultiLaser][info] up_time : 0
[2021-07-28 01:48:40.936395][MultiLaser][info] user_notes : 
[2021-07-28 01:48:40.936407][MultiLaser][info] user_tag : OMDxxx-R2000 HD
[2021-07-28 01:48:40.936414][MultiLaser][info] vendor : Pepperl+Fuchs
[2021-07-28 01:48:40.936419][MultiLaser][info] ============================================================
[2021-07-28 01:48:40.936425][MultiLaser][info] Starting capturing: 
[2021-07-28 01:48:40.967767][MultiLaser][info] [Text][Connecting to TCP data channel at 192.168.192.100:51812 ... ]
[2021-07-28 01:48:40.972961][MultiLaser][info] OK
[2021-07-28 01:48:41.055454][MCLoc][info] Scan received
[2021-07-28 01:48:41.076892][SensorFuser][info] Recv Map in FusedLaser!!!
[2021-07-28 01:48:44.524590][DSPChassis][info] [Text][UART Battery response time out]
[2021-07-28 01:48:44.524636][Robokit][warning] [Alarm][Warning|54001|UART Battery response time out|1]
[2021-07-28 01:48:47.538019][Robokit][warning] [Alarm][Warning|54100|DSP reconfiging...|0]
[2021-07-28 01:48:47.738241][DSPChassis][info] Dsp2Ground params load compeletly.
[2021-07-28 01:48:47.738331][DSPChassis][info] [Text][update hostErrState to false]
[2021-07-28 01:48:48.542225][RobotPosEKF][info] [Text][EKF Odom Received: 30431462662]
[2021-07-28 01:48:48.561504][RobotPosEKF][info] [Text][EKF IMU Received: 30450578948]
[2021-07-28 01:48:48.571415][MCLoc][info] Odom received 30450578948
[2021-07-28 01:48:48.625722][MCLoc][info] InitialPose Size: 0
[2021-07-28 01:48:48.625765][MCLoc][info] No InitialPose, init from last location. x:781.037, y:-143.85, angle:166.164
[2021-07-28 01:48:48.626515][MCLoc][info] Create MCLoc Motion Model
[2021-07-28 01:48:48.626527][MCLoc][info] Clear MCLoc Motion Model
[2021-07-28 01:48:48.628984][MCLoc][info] Create Observation Model
[2021-07-28 01:48:48.629224][MCLoc][info] Point size: 4890 Line size: 0
[2021-07-28 01:48:48.629993][MCLoc][info] Size1 Cell Number: 80
[2021-07-28 01:48:48.630023][MCLoc][info] Ann cost 0.0223846Mb
[2021-07-28 01:48:48.630581][MCLoc][info] Quad Tree cost 0.0167694MB
[2021-07-28 01:48:48.630607][MCLoc][info] Grid map cost 0.190735 MB * 3
[2021-07-28 01:48:48.630622][MCLoc][info] Quad Grid size: 50 50 resolution in mm:500 gridsize in mm:10
[2021-07-28 01:48:48.630639][MCLoc][info] GridMapGaussinDist: 20 100
[2021-07-28 01:48:48.630667][MCLoc][info] Using: 3 Threads to Load Map, total s1 cell size: 80 deal with 80 cells
[2021-07-28 01:48:48.630794][MoveFactory][info] Clear Move Task List!
[2021-07-28 01:48:48.631036][MCLoc][info] begin to fill grid map patch
[2021-07-28 01:48:48.631098][MCLoc][info] begin to fill grid map patch
[2021-07-28 01:48:48.631130][MCLoc][info] begin to fill grid map patch
[2021-07-28 01:48:48.745144][MCLoc][info] calc occupied map cost 0.114461s
[2021-07-28 01:48:48.747572][MCLoc][info] Create Reflector Observation Model
[2021-07-28 01:48:48.747596][MCLoc][info] Point size: 0 Line size: 0
[2021-07-28 01:48:48.747620][MCLoc][info] Size1 Cell Number: 0
[2021-07-28 01:48:48.747635][MCLoc][info] Ann cost 0Mb
[2021-07-28 01:48:48.747657][MCLoc][info] Map doesn't contain any point!
[2021-07-28 01:48:48.747675][MCLoc][info] Quad Tree cost 0.000167847MB
[2021-07-28 01:48:48.747692][MCLoc][info] Grid map cost 0 MB * 3
[2021-07-28 01:48:48.747707][MCLoc][info] Quad Grid size: 50 50 resolution in mm:500 gridsize in mm:10
[2021-07-28 01:48:48.747726][MCLoc][info] GridMapGaussinDist: 20 255
[2021-07-28 01:48:48.747741][MCLoc][info] begin to fill grid map patch
[2021-07-28 01:48:48.747753][MCLoc][info] calc occupied map cost 1.3579e-05s
[2021-07-28 01:48:48.747789][MCLoc][info] Initialize pf 2: 500 0 166.164
[2021-07-28 01:48:48.747876][MCLoc][info] Use Last Localization Pose: 781.037 -143.85 2.90011
[2021-07-28 01:48:48.747894][MCLoc][info] ALL INITIAL STEPS IN MCLOC IS DONE ........
[2021-07-28 01:48:48.759182][MCLoc][info] [Event][relocFinished|MCLoc]
[2021-07-28 01:48:48.759200][MCLoc][info] relocFinished
[2021-07-28 01:48:48.759759][MCLoc][info] [Event][relocFailed|MCLoc]
[2021-07-28 01:48:48.759784][MCLoc][info] relocFailed
[2021-07-28 01:48:48.772132][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:48:56.033300][MCLoc][error] Scan has not been updated for 306 ms, waiting for recover by robot itself.37587615939 37587615939
[2021-07-28 01:48:56.033408][Robokit][error] [Alarm][Error|52102|localization module cannot get laser data|1]
[2021-07-28 01:48:56.144877][DSPChassis][info] [Text][update hostErrState to true]
[2021-07-28 01:48:56.199448][MultiLaser][error] cannot receive laser data within 500 ms
[2021-07-28 01:48:56.199537][Robokit][error] [Alarm][Error|52100|cannot receive laser data within 500 ms|1]
[2021-07-28 01:49:05.733924][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.764940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.795944][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.827015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.858028][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.888962][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.920049][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.951035][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:05.982011][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.013029][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.043977][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.074888][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.105800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.136801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.167827][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.198890][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.229880][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.260821][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.291734][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.322822][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.353850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.384854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.415802][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.446777][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.477694][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.508587][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.539536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.570548][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.601538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.632533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.663427][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.694314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.725283][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.756248][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.787228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.818242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.849184][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.880129][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.911076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.942089][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:06.973086][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.004008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.034858][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.065723][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.096679][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.127648][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.158656][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.189636][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.220586][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.251467][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.282371][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.313295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.344335][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.375299][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.406287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.437265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.468277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.499632][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.530525][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.561448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.592404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.623374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.654278][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.685224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.716256][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.747423][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.778328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.809302][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.840231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.871262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.902331][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.933404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.964413][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:07.995391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.026328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.057267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.088207][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.119120][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.150087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.181038][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.211918][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.242814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.273743][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.304673][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.335569][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.366551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.397493][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.428431][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.459410][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.490363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.521341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.552266][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.583258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.614254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.645194][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.676192][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.707148][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.738087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.769078][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.800271][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.831210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.862108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.893053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.924022][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.955013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:08.986094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.017129][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.048055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.079045][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.110015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.141043][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.172034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.203033][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.233946][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.295674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.326660][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.357689][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.388707][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.419633][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.450583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.481940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.513153][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.544162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.575140][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.606145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.637088][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.668093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.699157][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.730222][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.761215][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.792298][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.823227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.854281][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.885206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.916183][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.947128][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:09.978175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.009122][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.040086][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.071066][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.102133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.133142][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.164125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.195053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.225950][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.287622][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.318538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.349451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.380432][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.411364][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.442269][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.473369][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.504322][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.535398][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.566401][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.597464][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.628512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.659482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.690380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.721363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.752314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.783251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.814205][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.875931][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.906976][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.937928][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.969039][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:10.999956][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.030931][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.061908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.093158][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.124091][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.155198][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.186147][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.217218][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.248202][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.279420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.310390][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.341589][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.372536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.403662][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.434576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.465707][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.496647][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.527701][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.558588][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.589525][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.620630][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.651623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.682564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.713430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.744350][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.775360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.806298][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.868035][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.898993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.929938][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.960968][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:11.991911][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.022875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.053863][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.084816][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.115738][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.146984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.177899][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.208881][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.240191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.271114][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.302070][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.333100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.364041][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.425618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.456608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.487529][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.518452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.549455][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.580418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.611433][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.642682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.673764][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.709834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.740826][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.771751][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.802678][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.833586][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.864574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.895585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.926572][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.957567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:12.988560][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.019500][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.081293][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.112253][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.143239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.174284][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.205306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.236267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.267329][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.298327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.329311][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.360319][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.391328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.422267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.453223][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.484182][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.515186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.546166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.577163][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.608125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.670347][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.701439][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.732447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.763438][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.794448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.825393][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.856473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.887462][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.918402][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.949408][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:13.980435][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.011427][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.042341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.073302][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.104283][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.135285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.166283][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.197217][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.258932][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.289904][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.320912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.351929][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.382842][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.413821][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.445233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.476279][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.507279][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.538268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.569217][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.600115][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.661872][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.692874][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.723863][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.754893][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.785897][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.816912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.848334][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.879320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.910314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.941375][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:14.972388][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.003387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.034935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.065922][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.096937][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.127963][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.159019][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.190023][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.251827][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.282823][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.313835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.344805][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.375866][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.406809][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.437767][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.468715][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.499636][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.530594][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.561605][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.592604][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.623687][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.654712][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.685686][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.716716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.747660][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.778587][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.840442][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.871430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.902387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.933429][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.964506][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:15.995466][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.026451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.057420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.088477][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.119415][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.150540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.181511][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.212788][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.243953][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.275076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.306056][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.337187][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.368135][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.399218][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.430172][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.461380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.492315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.523373][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.554308][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.585386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.616324][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.647545][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.678464][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.709434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.740422][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.771421][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.802412][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.833404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.864509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.895529][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.926473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.957456][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:16.988405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.019323][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.050378][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.081309][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.112220][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.143240][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.174211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.205091][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.235988][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.267051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.297971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.328976][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.359877][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.390849][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.452589][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.483529][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.514517][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.545403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.576367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.607277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.638320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.669278][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.700306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.731251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.762237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.793250][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.824312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.855252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.886237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.917254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.948466][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:17.979396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.010326][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.041268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.072299][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.103230][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.134221][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.165139][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.196089][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.227031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.258004][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.288963][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.319922][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.350863][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.381851][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.412839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.443939][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.474870][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.505785][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.536721][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.598406][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.629454][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.660396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.691365][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.722302][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.753250][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.784251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.815227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.846202][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.877256][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.908231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.939126][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:18.970135][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.001286][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.032222][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.063261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.094202][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.125255][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.156171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.187292][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.218287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.249269][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.280197][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.311170][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.342108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.373105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.404059][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.435158][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.466101][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.497089][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.528042][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.558945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.590176][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.621149][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.652085][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.683083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.714003][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.744956][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.775848][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.806789][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.837980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.869116][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.900037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.930951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.961902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:19.992908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.023918][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.054980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.085909][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.116927][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.147889][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.178854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.209912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.240832][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.271723][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.302698][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.333685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.364702][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.395618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.426603][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.457628][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.488619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.519535][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.550536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.581568][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.612622][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.643619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.674571][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.705518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.736415][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.767328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.798296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.829299][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.860306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.891321][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.922327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.953275][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:20.984619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.015634][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.046626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.077748][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.108784][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.139729][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.170680][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.202010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.233010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.264019][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.295022][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.326024][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.387794][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.418762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.449756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.480772][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.511771][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.542719][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.573754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.604867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.635861][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.666834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.697803][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.728866][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.760065][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.791405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.822356][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.853363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.884370][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.915308][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.946285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:21.977562][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.008576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.039483][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.070403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.101367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.132408][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.163407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.194487][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.225514][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.256554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.287521][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.318495][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.349479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.380518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.411473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.442513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.473468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.504423][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.566133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.597147][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.628083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.659064][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.690057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.721031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.752060][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.783069][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.814068][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.845128][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.876052][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.906971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.937927][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:22.969202][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.000193][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.031186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.062215][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.093172][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.124143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.155569][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.186569][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.217578][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.248595][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.279592][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.310536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.341452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.372447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.403437][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.434495][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.465534][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.496537][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.527488][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.558688][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.589686][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.620617][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.682244][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.713428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.744540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.775527][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.806521][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.837492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.868510][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.899517][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.930533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.961531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:23.992553][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.023571][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.054636][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.085613][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.116593][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.147712][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.178651][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.209644][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.240663][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.271628][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.302657][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.333666][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.364704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.395834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.426792][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.457799][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.488775][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.519889][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.550896][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.581930][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.613010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.643992][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.674936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.705900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.737042][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.768213][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.799239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.830199][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.861205][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.892163][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.923175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.954159][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:24.985192][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.016313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.047279][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.078204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.109156][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.140134][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.171135][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.202081][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.233036][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.263951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.294912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.326245][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.357220][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.388146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.419138][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.450181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.481108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.512185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.543160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.574196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.605211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.636207][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.697835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.728801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.759787][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.790790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.821862][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.852887][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.883894][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.915146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.946170][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:25.977168][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.008162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.039145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.070105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.101119][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.132087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.163092][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.194096][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.225209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.256149][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.287175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.318360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.349456][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.380483][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.411577][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.442585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.473590][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.504570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.535765][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.566713][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.597980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.628976][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.660117][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.691037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.722286][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.753222][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.784356][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.815297][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.846476][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.877487][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.939351][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:26.970563][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.001619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.032795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.063709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.095012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.126073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.141411][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -337.600006 to -337.399994]
[2021-07-28 01:49:27.141479][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -337.600006 to -337.399994|1]
[2021-07-28 01:49:27.157020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.187934][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.219000][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.249980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.280936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.311842][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.342815][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.373734][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.404840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.435738][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.466703][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.497619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.528607][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.559521][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.590442][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.621342][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.652253][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.683159][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.714193][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.745106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.776055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.807002][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.837948][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.868894][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.899967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.930966][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.961973][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:27.992892][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.023885][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.054846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.085916][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.116844][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.147941][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.178849][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.209745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.240672][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.271651][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.302560][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.333484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.364418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.395358][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.426273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.457304][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.488247][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.519173][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.550152][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.581091][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.612016][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.642995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.673926][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.704964][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.735880][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.766894][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.797867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.828838][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.859809][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.890736][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.921693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.952655][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:28.983626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.014534][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.045448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.076440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.107404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.138334][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.169218][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.200123][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.230993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.261951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.292853][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.323913][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.354782][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.385753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.447456][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.478357][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.509423][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.540365][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.571250][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.602220][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.633142][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.664054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.694985][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.725904][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.756984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.787958][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.818950][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.849884][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.881008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.911951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.943010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:29.973937][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.035772][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.067052][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.098289][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.129254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.160138][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.191115][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.222097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.253147][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.284127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.315077][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.345957][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.376908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.407891][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.438867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.469825][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.500846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.531745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.562708][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.593614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.624571][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.655514][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.686557][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.717484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.748453][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.779348][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.779734][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:49:30.779794][MultiLaser][error] ERROR: No connection to laser range finder or connection lost!
[2021-07-28 01:49:30.779859][MultiLaser][error] ERROR: data connection error: 125
[2021-07-28 01:49:30.781152][MultiLaser][error] ERROR: Laser range finder disconnected. Trying to reconnect...
[2021-07-28 01:49:30.781219][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:49:30.810890][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.841807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.864576][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -337.299988 to -337.100006]
[2021-07-28 01:49:30.864634][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -337.299988 to -337.100006|2]
[2021-07-28 01:49:30.872792][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.903710][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.934617][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.965608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:30.996914][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.027848][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.058753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.089780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.120824][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.151970][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.213558][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.244468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.275344][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.306295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.337166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.368130][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.399052][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.430047][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.461043][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.491943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.522833][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.553852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.584919][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.615962][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.646859][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.677820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.708748][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.739668][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.770694][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.801641][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.832609][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.863513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.894440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.925368][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.956324][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:31.987374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.018312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.049394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.080398][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.111441][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.173498][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.204411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.235384][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.266306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.297203][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.328131][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.359122][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.390051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.420975][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.451906][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.482804][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.513686][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.544831][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.575799][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.606812][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.637721][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.668833][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.699725][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.730709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.761618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.792553][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.823471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.854440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.885386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.916398][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.947319][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:32.978230][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.009242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.040240][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.071176][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.102194][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.133163][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.164097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.195106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.226060][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.257094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.288057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.319050][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.350039][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.380969][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.411945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.442957][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.473896][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.504841][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.536235][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.567209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.598165][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.629231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.660252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.691185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.722258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.753200][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.784166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.815173][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.846207][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.854346][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:49:33.854407][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:49:33.877130][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.908023][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.939012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:33.970049][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.001102][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.032090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.063017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.093953][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.124988][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.155964][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.186863][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.217840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.248953][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.310732][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.341705][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.372668][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.403594][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.434551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.465461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.496532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.527555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.558474][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.589476][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.620419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.651435][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.682356][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.713354][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.744322][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.775352][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.806385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.837369][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.899234][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.930243][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.961232][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:34.992211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.023143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.054309][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.085399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.116952][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.148007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.178981][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.209979][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.240994][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.271932][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.302998][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.333966][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.364897][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.395884][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.426907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.457820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.519693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.550623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.581602][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.612615][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.643561][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.665833][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.899994 to -336.700012]
[2021-07-28 01:49:35.665876][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.899994 to -336.700012|3]
[2021-07-28 01:49:35.674560][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.705962][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.736931][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.767885][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.798828][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.829901][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.854550][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:49:35.860880][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.891967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.922959][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.953951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:35.984967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.015957][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.046889][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.077885][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.108843][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.139840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.170814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.201793][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.232781][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.263756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.294934][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.325936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.357021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.388032][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.418958][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.480704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.511712][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.542661][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.573654][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.604742][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.635661][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.666596][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.697584][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.728531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.759631][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.790570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.821493][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.852463][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.883634][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.914844][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.922468][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:49:36.922529][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:49:36.945791][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:36.976808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.007743][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.038746][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.070043][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.101031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.132060][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.163010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.193950][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.224886][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.255977][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.286950][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.317945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.348979][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.380021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.411133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.472939][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.503890][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.534879][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.565875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.596886][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.627848][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.659228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.690254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.721268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.752242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.783225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.814162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.845124][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.876127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.907145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.938172][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:37.969184][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.000101][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.031088][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.062136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.093111][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.124164][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.155171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.186178][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.217057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.247969][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.278949][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.309962][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.341005][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.372025][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.402935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.433902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.465009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.495960][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.527010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.558032][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.589033][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.619985][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.651095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.682096][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.713196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.744165][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.775439][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.806370][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.837511][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.868509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.899522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.922707][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:49:38.930444][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.961434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:38.992459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.054251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.085262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.116226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.147136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.178085][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.209077][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.240095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.271106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.302061][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.333070][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.364017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.394972][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.425914][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.457021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.487977][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.519154][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.550066][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.581031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.611940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.642990][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.673933][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.704947][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.735874][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.767007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.797929][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.829057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.859967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.891087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.922044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.953188][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.984107][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:39.994365][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:49:39.994423][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:49:40.015118][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.046160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.077153][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.108060][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.138995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.169942][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.200879][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.231836][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.262854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.293794][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.324849][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.355786][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.386768][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.417682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.448726][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.479670][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.510584][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.541526][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.572568][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.634407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.665330][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.696335][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.727246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.758299][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.789222][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.820179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.851082][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.882088][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.913020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.944072][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:40.975028][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.005978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.037019][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.068048][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.099022][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.129997][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.160938][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.222831][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.253786][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.284752][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.315780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.346724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.377795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.408831][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.439813][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.470720][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.501624][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.532563][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.563512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.594540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.625652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.656564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.687569][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.718482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.749452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.780391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.811560][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.842476][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.873449][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.904415][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.935305][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.966236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:41.994607][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:49:41.997168][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.028071][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.058984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.089982][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.121008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.183055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.214132][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.245257][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.276233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.307415][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.338346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.369504][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.400496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.431504][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.462418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.493515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.524472][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.586337][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.617497][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.648457][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.679609][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.710560][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.741548][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.772515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.803919][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.834805][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.865792][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.896725][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.927677][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.958576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:42.989545][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.020462][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.051418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.066463][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:49:43.066519][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:49:43.082342][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.113306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.144221][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.206034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.237050][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.268004][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.298989][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.329946][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.360908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.391852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.422834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.453727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.484739][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.515673][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.546653][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.577629][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.608586][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.639509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.670457][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.701341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.732342][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.763280][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.794189][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.825103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.856119][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.887047][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.917978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.948908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:43.979991][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.010921][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.041903][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.072868][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.103782][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.134724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.165732][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.196682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.227667][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.258688][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.289608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.320519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.351497][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.382466][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.413436][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.444385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.475357][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.506266][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.537250][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.568440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.599394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.630308][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.661274][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.692170][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.723188][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.754108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.785126][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.816027][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.846995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.877907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.908905][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.939827][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:44.970790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.001733][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.032683][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.063592][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.066646][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:49:45.094664][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.125927][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.156910][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.187839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.218815][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.249788][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.311600][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.342559][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.373461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.404434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.435459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.466379][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.497272][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.528289][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.559296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.590297][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.621323][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.652226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.683148][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.714137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.745139][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.776123][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.807062][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.838163][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.869094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.900115][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.931022][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.961992][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:45.992943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.023847][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.054833][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.085816][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.116900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.138373][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:49:46.138437][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:49:46.147918][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.178849][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.209765][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.240871][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.303023][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.334010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.365034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.395942][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.426907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.457841][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.489026][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.520011][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.551020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.581940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.612936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.643854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.675004][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.706004][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.736982][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.768013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.799019][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.829949][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.860966][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.892097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.923098][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.954103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:46.985100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.016095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.047050][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.078145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.109126][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.140133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.171108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.202027][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.233008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.264046][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.295054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.326082][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.357112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.388125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.419179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.450211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.481293][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.512261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.543253][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.574260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.605274][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.636228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.667241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.698257][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.729257][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.760276][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.791241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.822232][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.853190][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.884621][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.915587][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.946677][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:47.977660][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.008673][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.039590][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.070574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.101538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.132549][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.138559][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:49:48.163506][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.194397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.225341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.256284][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.287344][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.318631][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.338530][MultiLaser][info] Connection to scanner at 192.168.192.100 succeed!
[2021-07-28 01:49:48.338561][Robokit][error] [Alarm][Error|52100|cannot receive laser data within 500 ms|0]
[2021-07-28 01:49:48.338590][MultiLaser][info] set sample and frequency
[2021-07-28 01:49:48.349295][MultiLaser][info] success set samples : 2800
[2021-07-28 01:49:48.349690][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.379262][MultiLaser][info] success set frequency : 30
[2021-07-28 01:49:48.380600][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.411541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.442442][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.504279][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.535285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.561764][MultiLaser][info] Current scanner settings:
[2021-07-28 01:49:48.561789][MultiLaser][info] ============================================================
[2021-07-28 01:49:48.561801][MultiLaser][info] angular_fov : 360.000000
[2021-07-28 01:49:48.561811][MultiLaser][info] angular_resolution : 0.000100
[2021-07-28 01:49:48.561822][MultiLaser][info] contamination : 0
[2021-07-28 01:49:48.561832][MultiLaser][info] device_family : 3
[2021-07-28 01:49:48.561841][MultiLaser][info] emitter_type : 2
[2021-07-28 01:49:48.561851][MultiLaser][info] feature_flags : 
[2021-07-28 01:49:48.561861][MultiLaser][info] filter_error_handling : tolerant
[2021-07-28 01:49:48.561871][MultiLaser][info] filter_maximum_margin : 100
[2021-07-28 01:49:48.561881][MultiLaser][info] filter_remission_threshold : reflector_std
[2021-07-28 01:49:48.561890][MultiLaser][info] filter_type : none
[2021-07-28 01:49:48.561900][MultiLaser][info] filter_width : 4
[2021-07-28 01:49:48.561912][MultiLaser][info] gateway : 192.168.192.1
[2021-07-28 01:49:48.561926][MultiLaser][info] gateway_current : 192.168.192.1
[2021-07-28 01:49:48.561936][MultiLaser][info] hmi_application_bitmap : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[2021-07-28 01:49:48.561955][MultiLaser][info] hmi_application_text_1 : 
[2021-07-28 01:49:48.561968][MultiLaser][info] hmi_application_text_2 : 
[2021-07-28 01:49:48.561977][MultiLaser][info] hmi_button_lock : off
[2021-07-28 01:49:48.561988][MultiLaser][info] hmi_display_mode : static_logo
[2021-07-28 01:49:48.561999][MultiLaser][info] hmi_language : english
[2021-07-28 01:49:48.562009][MultiLaser][info] hmi_parameter_lock : off
[2021-07-28 01:49:48.562018][MultiLaser][info] hmi_static_logo : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////x/4/x/4/x/4/wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/////////////////////////wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/x/4/x/4/x/4/x/4/w/w/4fh/4fh/4AB/8AD/+AH//gf//gf//gf/////////////wAA/wAA/wAA/wAA/wAA/wAA/x44/x44/x44/x44/x44/x44/x44/x44/x44/x44/x/4/////z///z///wf//wD//wD//wAf/wAf/4AD/4AD/+AA/+AA/+Pg/+Pg/+MA/+AA/+AA/+AA/4AD/wAf/wD//wf//wf//z///////////////////////////////////////////////////////////////////////////////////
[2021-07-28 01:49:48.562029][MultiLaser][info] hmi_static_text_1 :                  IDEA
[2021-07-28 01:49:48.562043][MultiLaser][info] hmi_static_text_2 : 
[2021-07-28 01:49:48.562054][MultiLaser][info] ip_address : 192.168.192.100
[2021-07-28 01:49:48.562067][MultiLaser][info] ip_address_current : 192.168.192.100
[2021-07-28 01:49:48.562078][MultiLaser][info] ip_mode : static
[2021-07-28 01:49:48.562092][MultiLaser][info] ip_mode_current : static
[2021-07-28 01:49:48.562103][MultiLaser][info] lcm_detection_period : 5000
[2021-07-28 01:49:48.562130][MultiLaser][info] lcm_detection_sensitivity : disabled
[2021-07-28 01:49:48.562145][MultiLaser][info] lcm_num_sectors : 12
[2021-07-28 01:49:48.562156][MultiLaser][info] lcm_sector_enable : 
[2021-07-28 01:49:48.562168][MultiLaser][info] lcm_sector_error_flags : 0
[2021-07-28 01:49:48.562179][MultiLaser][info] lcm_sector_warn_flags : 0
[2021-07-28 01:49:48.562192][MultiLaser][info] load_indication : 30
[2021-07-28 01:49:48.562203][MultiLaser][info] locator_indication : off
[2021-07-28 01:49:48.562216][MultiLaser][info] mac_address : 000d810989d4
[2021-07-28 01:49:48.562227][MultiLaser][info] max_connections : 3
[2021-07-28 01:49:48.562240][MultiLaser][info] operating_mode : measure
[2021-07-28 01:49:48.562251][MultiLaser][info] operation_time : 70260
[2021-07-28 01:49:48.562264][MultiLaser][info] operation_time_scaled : 122828
[2021-07-28 01:49:48.562275][MultiLaser][info] part : 305986
[2021-07-28 01:49:48.562284][MultiLaser][info] power_cycles : 664
[2021-07-28 01:49:48.562293][MultiLaser][info] product : OMD30M-R2000-B23-V1V1D-HD-1L
[2021-07-28 01:49:48.562303][MultiLaser][info] radial_range_max : 30.000000
[2021-07-28 01:49:48.562323][MultiLaser][info] radial_range_min : 0.000000
[2021-07-28 01:49:48.562337][MultiLaser][info] radial_resolution : 0.001000
[2021-07-28 01:49:48.562347][MultiLaser][info] revision_fw : 1.60
[2021-07-28 01:49:48.562357][MultiLaser][info] revision_hw : 1.62
[2021-07-28 01:49:48.562366][MultiLaser][info] samples_per_scan : 2800
[2021-07-28 01:49:48.562378][MultiLaser][info] sampling_rate_max : 84000
[2021-07-28 01:49:48.562397][MultiLaser][info] sampling_rate_min : 100
[2021-07-28 01:49:48.562407][MultiLaser][info] scan_direction : ccw
[2021-07-28 01:49:48.562416][MultiLaser][info] scan_frequency : 30
[2021-07-28 01:49:48.562426][MultiLaser][info] scan_frequency_max : 50.000000
[2021-07-28 01:49:48.562435][MultiLaser][info] scan_frequency_measured : 30.000000
[2021-07-28 01:49:48.562449][MultiLaser][info] scan_frequency_min : 10.000000
[2021-07-28 01:49:48.562461][MultiLaser][info] serial : 40000088016603
[2021-07-28 01:49:48.562472][MultiLaser][info] status_flags : 0
[2021-07-28 01:49:48.562483][MultiLaser][info] subnet_mask : 255.255.255.0
[2021-07-28 01:49:48.562496][MultiLaser][info] subnet_mask_current : 255.255.255.0
[2021-07-28 01:49:48.562507][MultiLaser][info] system_time_raw : 333756237630
[2021-07-28 01:49:48.562519][MultiLaser][info] temperature_current : 27
[2021-07-28 01:49:48.562530][MultiLaser][info] temperature_max : 67
[2021-07-28 01:49:48.562542][MultiLaser][info] temperature_min : 45
[2021-07-28 01:49:48.562553][MultiLaser][info] up_time : 1
[2021-07-28 01:49:48.562566][MultiLaser][info] user_notes : 
[2021-07-28 01:49:48.562577][MultiLaser][info] user_tag : OMDxxx-R2000 HD
[2021-07-28 01:49:48.562589][MultiLaser][info] vendor : Pepperl+Fuchs
[2021-07-28 01:49:48.562600][MultiLaser][info] ============================================================
[2021-07-28 01:49:48.562613][MultiLaser][info] Starting capturing: 
[2021-07-28 01:49:48.566197][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.594251][MultiLaser][info] [Text][Connecting to TCP data channel at 192.168.192.100:34165 ... ]
[2021-07-28 01:49:48.597117][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.600043][MultiLaser][info] OK
[2021-07-28 01:49:48.628091][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.659112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:49:48.690167][SensorFuser][debug] [Text][Insert Last Laser error!!!!]
[2021-07-28 01:49:48.690202][MCLoc][info] Scan data update recover
[2021-07-28 01:49:48.690248][Robokit][error] [Alarm][Error|52102|localization module cannot get laser data|0]
[2021-07-28 01:49:48.789540][DSPChassis][info] [Text][update hostErrState to false]
[2021-07-28 01:51:17.610737][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.600006 to -336.399994]
[2021-07-28 01:51:17.610781][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.600006 to -336.399994|4]
[2021-07-28 01:51:35.054513][MCLoc][error] Scan has not been updated for 303 ms, waiting for recover by robot itself.196623043377 196623043377
[2021-07-28 01:51:35.054591][Robokit][error] [Alarm][Error|52102|localization module cannot get laser data|1]
[2021-07-28 01:51:35.070736][DSPChassis][info] [Text][update hostErrState to true]
[2021-07-28 01:51:35.234633][MultiLaser][error] cannot receive laser data within 500 ms
[2021-07-28 01:51:35.234715][Robokit][error] [Alarm][Error|52100|cannot receive laser data within 500 ms|1]
[2021-07-28 01:51:44.774808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:44.805726][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:44.836716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:44.867658][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:44.898652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:44.929662][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:44.960710][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:44.991744][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.053479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.084524][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.115513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.146473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.177401][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.208352][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.239261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.270245][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.301463][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.332434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.363424][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.394347][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.425336][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.456262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.487264][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.518291][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.549288][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.580294][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.611366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.642343][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.673297][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.704224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.735197][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.766265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.797268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.828281][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.859306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.890315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.921434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.952414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:45.983434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.014473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.045535][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.076460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.107446][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.138537][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.169520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.231256][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.262289][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.293296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.324345][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.355386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.386363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.417320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.448264][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.479254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.510320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.541362][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.572363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.603482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.634434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.696316][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.727370][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.758397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.789366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.820399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.851398][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.882363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.913314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.944361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:46.975374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.006346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.037326][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.068285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.099289][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.130263][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.161304][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.192479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.223482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.254509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.285455][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.316482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.347406][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.378409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.409567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.440544][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.471540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.502571][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.533531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.564582][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.595527][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.626500][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.657522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.688538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.719640][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.750628][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.781602][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.812603][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.874460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.905519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.936519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.967590][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:47.998542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.029465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.060443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.091447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.122744][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.153745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.184767][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.215790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.246852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.277830][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.339663][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.370689][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.401652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.432676][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.463693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.494675][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.525641][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.556685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.587774][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.618778][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.650037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.681190][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.712160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.743174][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.774246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.805285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.836546][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.867540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.898541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.929574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.960700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:48.991698][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.022646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.053744][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.084833][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.115797][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.146757][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.177698][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.208702][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.239650][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.270704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.302053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.333051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.363955][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.394909][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.425828][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.456846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.487819][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.518878][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.549865][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.580890][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.611816][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.642919][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.673850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.704814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.735748][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.766820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.797808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.828915][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.859872][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.890877][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.921807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:49.983539][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.014614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.045661][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.076841][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.107800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.138852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.169855][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.200883][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.231818][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.262850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.293857][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.324879][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.355881][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.386875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.448631][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.479563][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.510532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.541438][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.572455][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.603956][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.634940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.665935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.697020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.728043][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.759039][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.790042][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.820996][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.852127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.883152][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.914080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.945097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:50.976113][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.007145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.038099][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.069137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.100190][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.131176][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.162127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.193131][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.224195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.255168][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.286228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.317185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.348224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.379259][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.410325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.441303][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.472399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.503382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.534395][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.565440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.596405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.658239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.689206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.720157][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.751115][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.782127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.813092][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.844082][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.875134][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.906103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.937203][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.968167][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:51.999179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.030213][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.061223][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.123032][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.154021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.185054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.216163][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.247265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.278330][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.309331][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.340371][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.371470][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.402513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.433535][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.464637][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.495668][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.526601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.588385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.619409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.650467][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.681407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.712363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.743413][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.774380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.805333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.836370][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.867327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.898332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.929353][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.960345][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:52.991475][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.022452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.053477][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.084540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.115493][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.146450][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.177461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.208456][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.239423][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.270371][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.301391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.332536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.363530][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.394555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.425616][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.456669][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.487653][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.518782][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.549795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.580826][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.611798][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.642808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.673839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.704906][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.735907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.797672][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.828688][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.859718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.890754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.921779][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.952790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:53.983799][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.014845][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.045969][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.077012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.108268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.139438][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.170380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.201397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.232385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.263460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.294401][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.325361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.356398][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.387409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.418346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.449314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.480318][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.511332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.542276][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.573421][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.604381][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.635346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.666254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.697210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.728248][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.759166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.790164][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.820949][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -337.600006 to -337.399994]
[2021-07-28 01:51:54.820997][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -337.600006 to -337.399994|5]
[2021-07-28 01:51:54.821116][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.852109][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.883120][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.914089][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.945038][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:54.976053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.007080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.038106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.069080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.100170][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.131209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.162140][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.193186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.224156][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.255162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.286165][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.317191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.348238][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.379257][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.441054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.472023][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.503031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.533975][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.564965][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.595893][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.626910][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.657884][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.688937][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.719972][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.751013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.782034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.813073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.844093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.905859][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.936902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.968118][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:55.999244][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.030300][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.061261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.092169][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.123214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.154350][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.185389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.216396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.247693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.278754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.309983][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.340943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.372167][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.403162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.434372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.465364][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.496542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.527471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.558494][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.589409][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.620335][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.651285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.682402][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.713388][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.744302][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.775226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.806178][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.837095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.868137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.899052][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.930022][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.961016][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:56.991997][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.022915][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.053859][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.084800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.115769][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.146722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.177722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.208754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.239818][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.270853][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.301773][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.332754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.363761][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.394708][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.425685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.456627][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.487674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.518590][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.549646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.580649][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.611686][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.642619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.673603][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.704565][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.735655][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.766591][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.797776][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.829145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.860062][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.890949][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.921888][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.952878][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:57.983790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.014673][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.046027][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.077057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.108091][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.139162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.170168][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.201205][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.232148][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.263229][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.294277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.325230][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.356211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.387241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.418287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.449275][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.480224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.511227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.542290][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.573304][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.604258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.635347][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.666295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.697228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.759326][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.790391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.821354][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.852339][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.883297][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.914328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.945321][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:58.976346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.007292][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.038293][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.069291][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.100315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.131320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.162302][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.224223][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.255186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.286103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.317131][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.348125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.379094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.410029][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.441053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.472453][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.503460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.534551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.565507][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.596518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.627564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.658505][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.689475][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.720601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.751566][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.782515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.813463][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.844505][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.875455][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.906389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.937478][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.968473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:51:59.999507][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.030451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.061416][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.092400][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.123346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.154358][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.185434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.216420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.247427][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.278468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.309471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.340500][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.371513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.402461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.433480][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.464500][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.495447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.526433][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.557421][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.588438][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.619392][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.650386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.681410][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.712492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.743503][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.774528][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.805559][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.836532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.898410][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.929426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.960485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:00.991498][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.022448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.053393][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.084389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.115435][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.146385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.177396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.208452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.239432][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.270341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.301267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.332261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.363315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.394313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.425387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.456424][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.487622][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.518646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.549556][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.580545][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.611542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.642512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.673525][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.704542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.735513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.766411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.797382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.828626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.859655][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.890645][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.921576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.952620][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:01.983635][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.014627][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.076389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.107428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.138356][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.169361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.200360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.231367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.262373][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.293345][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.324328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.355306][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.386273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.417274][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.448260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.510154][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.541106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.572143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.603145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.634080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.665056][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.696051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.727013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.758400][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.789400][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.820419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.851353][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.882259][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.913245][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:02.944175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.006057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.037084][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.068042][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.098980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.129936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.160924][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.191850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.222910][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.253900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.284920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.315913][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.346925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.377931][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.408893][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.439838][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.470854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.501853][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.532957][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.563993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.594963][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.625925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.656839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.687820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.719088][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.749998][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.780995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.812097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.843146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.874085][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.905021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.936169][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.967188][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:03.998203][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.029206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.060236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.091261][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.122231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.184262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.215287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.246239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.277231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.308231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.339231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.370226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.401136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.432313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.463288][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.494240][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.525177][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.556097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.587092][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.618064][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.649435][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.680485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.711467][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.742386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.773399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.804426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.835443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.897216][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.928227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.959211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:04.990195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.021188][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.052226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.083165][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.114307][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.145284][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.176236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.207223][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.238206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.269181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.300080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.361900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.392925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.423919][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.454924][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.485879][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.516880][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.547917][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.579162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.610203][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.641315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.672314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.703393][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.734270][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.765412][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.827387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.858320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.889533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.920562][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.951621][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:05.982565][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.013555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.044588][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.075850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.106815][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.137758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.168808][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.199824][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.230836][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.292572][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.323488][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.354394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.385414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.416469][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.447470][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.478426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.509439][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.540416][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.571519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.602485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.633453][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.664366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.695382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.726333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.757430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.788378][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.819333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.850254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.881161][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.912055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.942970][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:06.973905][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.004946][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.035901][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.066922][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.097875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.128891][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.159822][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.190819][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.221801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.252795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.283725][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.314652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.345683][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.376866][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.407762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.469522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.500488][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.531443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.562524][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.593506][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.624611][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.655651][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.686646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.717613][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.748709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.779682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.810714][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.841645][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.872612][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.903551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.934519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.965448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:07.996484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.027434][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.058392][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.089332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.120376][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.151447][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.182391][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.213331][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.244332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.275368][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.306330][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.337246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.368295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.399204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.430228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.461160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.492119][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.523048][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.554073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.585009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.616145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.647153][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.678327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.709268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.740458][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.771394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.802579][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.833523][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.864656][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.895644][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.926574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.957523][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:08.988616][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.019547][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.050449][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.081611][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.112626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.143536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.174536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.205528][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.236527][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.267424][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.298325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.329321][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.360255][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.391212][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.422315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.453231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.480857][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.500000 to -336.700012]
[2021-07-28 01:52:09.480910][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.500000 to -336.700012|6]
[2021-07-28 01:52:09.484120][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.515020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.546083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.577021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.608100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.639060][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.670093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.701044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.731968][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.762971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.793888][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.824846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.855885][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.886857][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.917824][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:09.948740][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.010686][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.041753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.072675][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.103710][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.134697][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.165682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.196635][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.227670][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.258606][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.289635][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.320570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.351574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.382562][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.413484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.475393][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.506322][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.537532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.568520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.599684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.630638][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.662102][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.693083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.724046][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.754985][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.785951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.816929][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.848015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.878943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.910007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.940917][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:10.971852][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.002783][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.033814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.064788][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.095780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.126700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.157801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.188750][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.219837][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.250780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.281734][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.312682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.343703][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.374678][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.405722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.436738][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.467759][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.498705][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.529630][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.560554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.622425][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.653430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.684388][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.715556][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.746543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.777504][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.808464][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.839529][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.870436][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.901403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.932377][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.963445][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:11.994368][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.025368][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.056330][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.087294][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.118253][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.149245][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.180211][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.211144][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.242051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.273007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.304029][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.335049][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.366009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.397012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.427967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.458975][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.489990][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.521210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.552174][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.583363][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.614319][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.645496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.676464][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.707479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.738410][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.769608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.800543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.831507][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.862403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.893382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.924337][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.955214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:12.986132][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.017212][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.048143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.079171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.110096][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.141010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.171901][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.233633][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.264762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.295684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.326582][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.357496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.388657][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.419598][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.450638][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.481587][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.512602][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.543719][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.574664][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.605589][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.636518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.667432][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.698419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.729370][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.760354][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.791266][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.822403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.853366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.884333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.915296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.946227][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:13.977183][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.008233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.039145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.070260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.101180][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.132085][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.163014][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.194005][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.225034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.256020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.286934][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.317973][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.348916][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.379945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.410902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.441913][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.472865][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.503797][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.534737][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.565745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.596755][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.628026][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.658922][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.689898][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.720873][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.751814][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.782711][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.844350][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.875268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.906233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.937207][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.968210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:14.999204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.030092][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.061083][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.092219][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.123299][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.154260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.185372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.216326][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.247210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.278104][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.309242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.340199][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.371171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.402090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.433044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.463955][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.494847][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.525835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.556857][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.587769][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.618735][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.649719][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.681209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.712215][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.743162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.774076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.805017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.835928][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.866849][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.897724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.928674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.959613][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:15.990601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.021541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.052541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.083459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.114358][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.145285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.176316][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.207237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.238215][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.269108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.300103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.330981][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.361871][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.392802][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.423698][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.454584][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.485715][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.516605][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.547536][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.578418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.609419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.640325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.671327][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.702280][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.733262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.764184][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.795119][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.826027][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.856978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.887897][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.919112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.950035][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:16.980982][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.011895][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.042931][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.073826][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.104807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.135729][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.166773][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.197718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.228737][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.259659][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.290672][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.321616][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.352682][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.383690][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.414666][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.445653][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.476618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.507602][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.538793][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.569736][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.631471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.662736][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.693798][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.725046][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.756095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.787240][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.818107][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.849093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.880024][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.911054][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.941998][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:17.973053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.003954][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.034867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.096566][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.127520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.158555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.189479][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.220628][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.251570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.282734][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.313753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.345038][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.376020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.407234][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.438272][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.469293][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.500242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.531323][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.562334][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.593459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.624594][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.655540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.686480][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.717384][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.748301][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.779255][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.810285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.841285][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.872256][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.903275][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.934200][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.965127][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:18.996064][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.027254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.058239][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.089217][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.120190][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.151164][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.182098][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.213111][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.244068][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.275100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.306049][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.337196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.368136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.399265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.430201][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.461151][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.492090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.523319][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.554270][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.585451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.616399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.647425][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.678332][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.709258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.740251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.771265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.802210][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.833171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.864224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.895231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.926191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.957143][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:19.988135][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.019186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.050089][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.081099][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.112013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.143006][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.173960][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.235724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.266718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.297681][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.328632][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.359533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.390511][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.421418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.452399][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.483333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.514316][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.545355][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.576271][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.607176][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.638196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.700407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.731322][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.762314][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.793212][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.824145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.855072][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.886094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.917125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.948106][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:20.979041][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.010056][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.041009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.071908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.102842][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.133812][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.164754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.195758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.226676][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.257646][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.288576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.319548][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.350836][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.381754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.412699][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.443797][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.474752][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.505768][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.536689][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.567671][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.598762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.629707][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.660637][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.691552][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.722433][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.753333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.815397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.846328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.877288][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.908236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.939201][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:21.970231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.001157][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.032058][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.063037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.093952][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.124850][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.155867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.186855][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.217784][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.279557][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.310697][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.341701][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.372651][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.403566][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.434583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.465560][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.496875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.527811][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.558795][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.589757][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.620834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.651779][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.682684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.713608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.744632][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.775576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.806603][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.837543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.868554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.899484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.930412][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.961446][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:22.992673][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.023718][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.054791][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.085722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.116740][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.147754][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.178745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.209766][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.240843][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.271762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.302772][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.333763][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.364730][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.395678][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.457778][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.488726][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.519650][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.550701][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.581620][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.612626][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.643604][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.674611][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.705538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.736583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.767513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.798428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.829378][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.860405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.891320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.922416][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.953383][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:23.984414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.015360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.046422][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.077404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.108380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.139312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.170337][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.201324][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.232333][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.263286][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.294268][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.325233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.356179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.387353][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.418348][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.449294][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.480255][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.511178][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.542182][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.573078][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.634800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.665702][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.696601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.727573][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.758471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.789412][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.820361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.851325][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.882341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.913465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.944436][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:24.975532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.006475][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.068341][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.099496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.130525][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.161531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.192482][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.223465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.254431][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.285454][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.316476][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.347541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.378577][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.409585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.440543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.471494][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.502471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.533490][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.564460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.595499][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.626431][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.657443][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.688397][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.719463][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.750420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.781307][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.812234][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.843295][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.874237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.905274][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.936214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.967272][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:25.998252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.029297][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.060248][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.091384][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.122335][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.153468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.184495][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.246462][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.277613][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.308519][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.339527][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.370460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.401551][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.432488][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.463542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.494554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.525598][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.556567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.587727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.618691][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.649735][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.680688][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.711840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.742978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.773969][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.804935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.835951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.866907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.897928][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.928909][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.960195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:26.991114][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.022094][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.053050][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.084031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.114967][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.145915][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.176908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.207864][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.238888][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.269945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.300947][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.331867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.362789][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.424552][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.455567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.486487][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.517543][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.548491][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.579575][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.610526][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.641588][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.672582][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.703554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.734491][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.765684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.796657][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.827652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.889428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.920374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.951383][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:27.982378][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.013420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.044380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.075343][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.106277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.137367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.168348][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.199405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.230364][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.261366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.292414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.354181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.385394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.416386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.447420][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.478372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.509365][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.540305][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.571241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.602173][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.633175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.664138][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.695150][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.726149][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.757145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.788086][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.819267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.850242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.881237][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.912172][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.943103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:28.974017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.004928][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.035910][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.066957][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.097911][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.128932][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.159907][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.190902][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.221836][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.252804][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.283727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.314766][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.345840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.376867][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.407804][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.438816][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.469763][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.500756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.531735][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.562657][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.593595][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.624555][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.655491][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.686450][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.717395][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.748705][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.779637][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.810586][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.841490][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.872570][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.903524][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.965347][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:29.996374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.027286][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.058231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.089225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.120195][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.151138][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.182105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.213031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.244146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.275144][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.306161][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.337152][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.368199][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.399198][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.430244][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.461148][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.492115][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.523062][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.554134][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.585146][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.616050][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.677825][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.708815][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.740196][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.771150][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.802236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.833155][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.864179][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.895191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.926273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.957198][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:30.988279][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.019213][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.050309][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.081251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.142946][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.174137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.205086][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.236282][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.267181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.298230][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.329175][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.360287][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.391252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.422263][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.453225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.484225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.515231][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.546273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.577209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.608235][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.639160][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.670173][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.701131][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.732198][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.763102][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.794035][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.825209][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.856375][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.887241][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.918216][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.949132][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:31.980256][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.011225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.042224][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.073154][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.104136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.135061][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.166058][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.197021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.228026][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.289722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.320708][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.351704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.382674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.413687][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.444619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.475649][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.506692][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.537809][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.568784][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.599803][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.630747][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.661768][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.692706][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.723614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.754573][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.785618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.816580][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.847531][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.878452][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.909460][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.940396][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:32.971385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.002375][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.033471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.064394][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.095408][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.126381][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.157401][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.188355][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.219374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.250311][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.281348][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.312313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.343296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.374265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.405158][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.466995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.498008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.529112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.560185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.591166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.622109][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.653065][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.684008][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.715048][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.745970][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.776935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.807846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.838821][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.869733][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.900685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.931935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.962845][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:33.993737][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.024629][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.055550][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.086614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.117572][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.148617][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.179539][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.210522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.241448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.272521][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.303458][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.334484][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.365406][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.396583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.427518][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.458542][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.489476][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.520521][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.551474][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.582509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.613562][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.644535][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.675501][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.706471][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.737426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.768581][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.799502][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.830619][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.861575][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.892509][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.923541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.954623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:34.985554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.016589][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.047541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.109272][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.140298][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.171228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.202267][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.233189][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.264155][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.295082][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.326034][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.356993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.387984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.418874][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.449839][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.480747][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.542426][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.573414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.604346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.635386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.666386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.697379][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.728564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.759486][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.790532][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.821487][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.852496][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.883538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.914510][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.945459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:35.976407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.007360][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.038315][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.069296][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.100233][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.131151][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.162093][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.193076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.224220][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.255202][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.286151][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.317066][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.347949][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.378934][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.409870][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.440817][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.471727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.502775][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.533709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.564704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.595601][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.626520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.688493][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.719485][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.750403][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.781440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.812411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.843386][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.874273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.905265][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.936247][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.967123][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:36.998030][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.028972][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.059881][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.090825][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.121896][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.152962][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.183978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.214882][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.245925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.276842][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.307813][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.338723][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.369709][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.400615][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.431585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.462612][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.493585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.524513][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.555417][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.586364][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.617277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.648174][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.679078][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.709999][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.740984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.771980][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.803068][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.834052][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.865026][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.895951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.926912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.957821][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:37.988731][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.019664][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.050724][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.081660][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.112785][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.143710][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.174835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.205777][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.236680][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.267642][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.298669][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.329579][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.360608][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.391541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.422526][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.453459][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.484512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.515794][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.546719][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.577600][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.608583][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.639503][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.670429][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.732301][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.793997][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.825051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.856191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.887125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.918055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.949015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:38.980048][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.010978][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.042058][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.073009][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.104090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.135012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.166024][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.196979][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.228007][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.258935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.289938][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.320914][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.351973][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.382885][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.413848][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.444801][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.475810][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.506716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.537685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.568706][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.599830][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.630715][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.661741][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.692677][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.723654][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.754658][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.785674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.816623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.847533][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.878515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.909639][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.940618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:39.971579][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.002478][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.033411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.064380][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.095346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.126492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.157474][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.188419][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.219389][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.250336][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.281292][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.312201][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.343228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.374139][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.405139][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.436103][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.467087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.498097][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.529046][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.559984][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.590891][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.621796][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.652746][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.683704][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.714813][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.745753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.776792][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.807803][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.838876][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.869860][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.900914][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.931894][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.962897][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:40.993833][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.024787][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.055745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.086739][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.117685][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.148705][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.179615][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.210546][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.241468][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.272473][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.303429][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.334385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.365312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.396260][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.427166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.458144][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.489147][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.520170][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.551105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.582068][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.612993][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.644012][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.674995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.705929][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.736882][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.767831][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.798793][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.829869][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.860820][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.891882][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.922785][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.953766][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:41.984848][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.015834][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.046756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.077854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.108858][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.139862][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.201540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.232467][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.263465][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.266369][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:42.266426][MultiLaser][error] ERROR: No connection to laser range finder or connection lost!
[2021-07-28 01:52:42.266482][MultiLaser][error] ERROR: data connection error: 125
[2021-07-28 01:52:42.267706][MultiLaser][error] ERROR: Laser range finder disconnected. Trying to reconnect...
[2021-07-28 01:52:42.267762][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:42.294418][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.325428][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.356430][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.387385][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.418280][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.449632][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.480564][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.511604][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.542517][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.573440][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.604366][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.635328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.666312][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.697284][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.728236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.759186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.790150][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.821154][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.852071][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.883020][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.913986][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.945015][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:42.975983][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.007018][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.038033][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.069006][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.130680][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.161614][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.192664][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.223593][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.254752][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.285692][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.316807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.347745][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.378716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.409769][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.440803][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.471758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.502691][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.533609][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.564684][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.595672][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.626711][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.657687][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.688875][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.719822][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.750805][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.781767][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.812760][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.843728][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.874707][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.905722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.936671][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.967568][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:43.998461][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.029374][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.060424][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.091407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.122407][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.153367][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.184411][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.215357][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.246338][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.277225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.308226][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.339172][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.370183][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.401108][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.432136][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.463051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.493940][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.524935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.556153][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.587141][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.618328][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.649248][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.680232][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.711162][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.772943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.803992][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.834920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.865966][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.896945][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.927971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.958968][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:44.989995][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.021017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.051886][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.082798][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.113868][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.144870][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.175864][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.237592][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.268540][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.299591][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.330623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.338348][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:45.338391][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:52:45.361580][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.392524][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.423501][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.454756][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.485742][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.516667][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.547694][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.578652][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.609625][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.640547][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.671607][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.702548][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.733451][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.764405][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.795346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.826258][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.857186][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.888100][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.919254][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.950204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:45.981184][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.012095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.043120][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.074047][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.105006][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.135951][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.166944][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.197926][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.228886][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.259943][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.290961][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.321887][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.353076][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.384105][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.415017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.445948][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.476976][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.508062][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.539064][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.569987][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.601145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.632044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.663037][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.693939][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.724971][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.755900][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.786785][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.817639][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.848620][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.879538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.910541][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.941442][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:46.972414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.003311][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.034234][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.065208][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.096125][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.127065][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.158044][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.188985][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.219887][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.250828][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.281935][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.312997][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.338523][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:47.343920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.374854][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.405763][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.436700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.467658][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.498581][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.529926][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.560877][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.591804][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.622713][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.653716][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.684722][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.715660][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.746597][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.777791][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.808760][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.839771][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.870744][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.901840][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.932790][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.963818][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:47.994782][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.025809][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.056787][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.087774][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.118700][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.149748][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.180687][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.211752][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.242674][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.273690][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.304762][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.335757][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.366656][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.397623][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.410389][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:48.410446][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:52:48.428567][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.459711][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.490640][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.521618][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.552576][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.583629][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.614593][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.676262][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.707243][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.738246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.769311][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.800236][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.831206][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.862181][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.893242][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.924246][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.955264][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:48.986243][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.017252][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.048183][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.079225][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.110191][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.141112][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.172372][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.203283][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.234228][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.265214][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.296130][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.327090][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.358057][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.389141][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.420055][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.451031][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.481981][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.512912][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.543800][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.574753][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.636382][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.667387][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.698331][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.729308][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.760350][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.791283][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.822192][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.853095][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.884087][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.915053][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.946051][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:49.977133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.008073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.039011][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.070329][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.101281][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.132404][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.163346][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.194421][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.225343][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.256313][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.287250][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.318442][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.349361][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.380251][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.410543][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:50.411217][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.442218][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.473118][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.504019][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.535140][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.566073][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.597017][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.628013][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.658920][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.689870][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.720835][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.751851][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.782805][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.813807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.844747][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.875727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.906670][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.937738][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.968693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:50.999976][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.030871][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.061846][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.092789][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.123758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.154702][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.185634][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.216727][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.247746][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.278665][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.309658][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.340578][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.371606][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.402520][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.464730][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.482390][MultiLaser][error] ERROR: Exception: <unspecified file>(1): expected value
[2021-07-28 01:52:51.482444][MultiLaser][error] ERROR: Reconnect failed. Trying again in 2 seconds...
[2021-07-28 01:52:51.495758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.526758][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.557780][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.588791][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.619755][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.650681][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.681629][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.713010][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.743932][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.774948][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.805908][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.836877][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.867861][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.929515][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.960492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:51.991575][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.022574][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.053563][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.084573][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.115512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.146538][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.177876][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.208964][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.239952][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.270960][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.301950][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.332925][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.394572][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.425528][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.456547][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.487554][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.518550][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.549492][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.580448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.611445][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.642546][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.673474][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.704450][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.735446][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.766448][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.797414][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.828344][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.859320][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.890277][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.921204][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.952133][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:52.983069][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.014040][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.045111][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.076079][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.106989][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.137968][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.169021][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.200002][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.230936][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.261863][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.292828][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.323847][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.354807][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.385822][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.416810][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.447693][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.478677][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.482570][MultiLaser][info] Connecting to scanner at 192.168.192.100 ... 
[2021-07-28 01:52:53.509585][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.540483][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.571568][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.602512][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.633522][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.664490][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.681044][MultiLaser][info] Connection to scanner at 192.168.192.100 succeed!
[2021-07-28 01:52:53.681072][Robokit][error] [Alarm][Error|52100|cannot receive laser data within 500 ms|0]
[2021-07-28 01:52:53.681102][MultiLaser][info] set sample and frequency
[2021-07-28 01:52:53.690607][MultiLaser][info] success set samples : 2800
[2021-07-28 01:52:53.695408][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.718598][MultiLaser][info] success set frequency : 30
[2021-07-28 01:52:53.726273][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.757171][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.788080][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.819185][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.850145][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.881166][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.905756][MultiLaser][info] Current scanner settings:
[2021-07-28 01:52:53.905777][MultiLaser][info] ============================================================
[2021-07-28 01:52:53.905784][MultiLaser][info] angular_fov : 360.000000
[2021-07-28 01:52:53.905790][MultiLaser][info] angular_resolution : 0.000100
[2021-07-28 01:52:53.905796][MultiLaser][info] contamination : 0
[2021-07-28 01:52:53.905802][MultiLaser][info] device_family : 3
[2021-07-28 01:52:53.905807][MultiLaser][info] emitter_type : 2
[2021-07-28 01:52:53.905812][MultiLaser][info] feature_flags : 
[2021-07-28 01:52:53.905817][MultiLaser][info] filter_error_handling : tolerant
[2021-07-28 01:52:53.905824][MultiLaser][info] filter_maximum_margin : 100
[2021-07-28 01:52:53.905834][MultiLaser][info] filter_remission_threshold : reflector_std
[2021-07-28 01:52:53.905843][MultiLaser][info] filter_type : none
[2021-07-28 01:52:53.905854][MultiLaser][info] filter_width : 4
[2021-07-28 01:52:53.905865][MultiLaser][info] gateway : 192.168.192.1
[2021-07-28 01:52:53.905875][MultiLaser][info] gateway_current : 192.168.192.1
[2021-07-28 01:52:53.905884][MultiLaser][info] hmi_application_bitmap : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[2021-07-28 01:52:53.905913][MultiLaser][info] hmi_application_text_1 : 
[2021-07-28 01:52:53.905921][MultiLaser][info] hmi_application_text_2 : 
[2021-07-28 01:52:53.905927][MultiLaser][info] hmi_button_lock : off
[2021-07-28 01:52:53.905934][MultiLaser][info] hmi_display_mode : static_logo
[2021-07-28 01:52:53.905940][MultiLaser][info] hmi_language : english
[2021-07-28 01:52:53.905947][MultiLaser][info] hmi_parameter_lock : off
[2021-07-28 01:52:53.905953][MultiLaser][info] hmi_static_logo : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////x/4/x/4/x/4/wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/////////////////////////wAA/wAA/wAA/wAA/wAA/wAA/x/4/x/4/x/4/x/4/x/4/x/4/x/4/w/w/4fh/4fh/4AB/8AD/+AH//gf//gf//gf/////////////wAA/wAA/wAA/wAA/wAA/wAA/x44/x44/x44/x44/x44/x44/x44/x44/x44/x44/x/4/////z///z///wf//wD//wD//wAf/wAf/4AD/4AD/+AA/+AA/+Pg/+Pg/+MA/+AA/+AA/+AA/4AD/wAf/wD//wf//wf//z///////////////////////////////////////////////////////////////////////////////////
[2021-07-28 01:52:53.905960][MultiLaser][info] hmi_static_text_1 :                  IDEA
[2021-07-28 01:52:53.905966][MultiLaser][info] hmi_static_text_2 : 
[2021-07-28 01:52:53.905971][MultiLaser][info] ip_address : 192.168.192.100
[2021-07-28 01:52:53.905978][MultiLaser][info] ip_address_current : 192.168.192.100
[2021-07-28 01:52:53.905984][MultiLaser][info] ip_mode : static
[2021-07-28 01:52:53.905989][MultiLaser][info] ip_mode_current : static
[2021-07-28 01:52:53.905994][MultiLaser][info] lcm_detection_period : 5000
[2021-07-28 01:52:53.906002][MultiLaser][info] lcm_detection_sensitivity : disabled
[2021-07-28 01:52:53.906008][MultiLaser][info] lcm_num_sectors : 12
[2021-07-28 01:52:53.906014][MultiLaser][info] lcm_sector_enable : 
[2021-07-28 01:52:53.906020][MultiLaser][info] lcm_sector_error_flags : 0
[2021-07-28 01:52:53.906027][MultiLaser][info] lcm_sector_warn_flags : 0
[2021-07-28 01:52:53.906033][MultiLaser][info] load_indication : 0
[2021-07-28 01:52:53.906039][MultiLaser][info] locator_indication : off
[2021-07-28 01:52:53.906046][MultiLaser][info] mac_address : 000d810989d4
[2021-07-28 01:52:53.906052][MultiLaser][info] max_connections : 3
[2021-07-28 01:52:53.906058][MultiLaser][info] operating_mode : measure
[2021-07-28 01:52:53.906067][MultiLaser][info] operation_time : 70260
[2021-07-28 01:52:53.906072][MultiLaser][info] operation_time_scaled : 122828
[2021-07-28 01:52:53.906078][MultiLaser][info] part : 305986
[2021-07-28 01:52:53.906083][MultiLaser][info] power_cycles : 664
[2021-07-28 01:52:53.906089][MultiLaser][info] product : OMD30M-R2000-B23-V1V1D-HD-1L
[2021-07-28 01:52:53.906099][MultiLaser][info] radial_range_max : 30.000000
[2021-07-28 01:52:53.906135][MultiLaser][info] radial_range_min : 0.000000
[2021-07-28 01:52:53.906148][MultiLaser][info] radial_resolution : 0.001000
[2021-07-28 01:52:53.906155][MultiLaser][info] revision_fw : 1.60
[2021-07-28 01:52:53.906161][MultiLaser][info] revision_hw : 1.62
[2021-07-28 01:52:53.906167][MultiLaser][info] samples_per_scan : 2800
[2021-07-28 01:52:53.906178][MultiLaser][info] sampling_rate_max : 84000
[2021-07-28 01:52:53.906184][MultiLaser][info] sampling_rate_min : 100
[2021-07-28 01:52:53.906190][MultiLaser][info] scan_direction : ccw
[2021-07-28 01:52:53.906195][MultiLaser][info] scan_frequency : 30
[2021-07-28 01:52:53.906202][MultiLaser][info] scan_frequency_max : 50.000000
[2021-07-28 01:52:53.906207][MultiLaser][info] scan_frequency_measured : 30.100000
[2021-07-28 01:52:53.906216][MultiLaser][info] scan_frequency_min : 10.000000
[2021-07-28 01:52:53.906221][MultiLaser][info] serial : 40000088016603
[2021-07-28 01:52:53.906228][MultiLaser][info] status_flags : 0
[2021-07-28 01:52:53.906234][MultiLaser][info] subnet_mask : 255.255.255.0
[2021-07-28 01:52:53.906239][MultiLaser][info] subnet_mask_current : 255.255.255.0
[2021-07-28 01:52:53.906244][MultiLaser][info] system_time_raw : 1129749740865
[2021-07-28 01:52:53.906250][MultiLaser][info] temperature_current : 29
[2021-07-28 01:52:53.906257][MultiLaser][info] temperature_max : 67
[2021-07-28 01:52:53.906263][MultiLaser][info] temperature_min : 45
[2021-07-28 01:52:53.906270][MultiLaser][info] up_time : 4
[2021-07-28 01:52:53.906275][MultiLaser][info] user_notes : 
[2021-07-28 01:52:53.906281][MultiLaser][info] user_tag : OMDxxx-R2000 HD
[2021-07-28 01:52:53.906287][MultiLaser][info] vendor : Pepperl+Fuchs
[2021-07-28 01:52:53.906292][MultiLaser][info] ============================================================
[2021-07-28 01:52:53.906299][MultiLaser][info] Starting capturing: 
[2021-07-28 01:52:53.912137][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.937272][MultiLaser][info] [Text][Connecting to TCP data channel at 192.168.192.100:51400 ... ]
[2021-07-28 01:52:53.942977][MultiLaser][info] OK
[2021-07-28 01:52:53.943078][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:53.973998][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:54.004909][SensorFuser][debug] [Text][Insert Laser error!!!!]
[2021-07-28 01:52:54.024975][MCLoc][info] Scan data update recover
[2021-07-28 01:52:54.025036][Robokit][error] [Alarm][Error|52102|localization module cannot get laser data|0]
[2021-07-28 01:52:54.136289][DSPChassis][info] [Text][update hostErrState to false]
[2021-07-28 01:53:41.514062][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.799988 to -337.000000]
[2021-07-28 01:53:41.514138][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.799988 to -337.000000|7]
[2021-07-28 01:54:18.604235][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.500000 to -335.299988]
[2021-07-28 01:54:18.604267][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.500000 to -335.299988|8]
[2021-07-28 01:54:21.667392][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.299988 to -335.100006]
[2021-07-28 01:54:21.667431][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.299988 to -335.100006|9]
[2021-07-28 01:54:25.927634][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.000000 to -334.799988]
[2021-07-28 01:54:25.927680][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.000000 to -334.799988|10]
[2021-07-28 01:54:52.231148][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -334.899994 to -335.100006]
[2021-07-28 01:54:52.231207][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -334.899994 to -335.100006|11]
[2021-07-28 01:54:56.094395][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -335.200012 to -335.399994]
[2021-07-28 01:54:56.094445][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -335.200012 to -335.399994|12]
[2021-07-28 01:55:22.233909][DSPChassis][info] [Text][The gyro is flying in the 2 second after calibration. -336.299988 to -336.500000]
[2021-07-28 01:55:22.233966][Robokit][info] [Alarm][Notice|57009|The gyro is flying in the 2 second after calibration. -336.299988 to -336.500000|13]
[2021-07-28 01:55:59.280307][Robokit][info] [Text][Robokit version: 3.2.4+release]
[2021-07-28 01:55:59.280369][Robokit][info] [Text][Used system memory: 0.400883 GB]
[2021-07-28 01:55:59.280466][Robokit][info] [Text][Free system memory: 3.3739 GB]
[2021-07-28 01:55:59.280540][Robokit][info] [Text][Robokit physical memory usage: 186.238 MB]
[2021-07-28 01:55:59.280621][Robokit][info] [Text][Robokit virtual memory usage: 4467.55 MB]
[2021-07-28 01:55:59.280688][Robokit][info] [Text][Robokit Max physical memory usage: 186.238 MB]
[2021-07-28 01:55:59.280755][Robokit][info] [Text][Robokit Max virtual memory usage: 4467.55 MB]
^C
root@srs:/usr/local/SeerRobotics/rbk# reboot now
Connection to 172.16.120.212 closed by remote host.
Connection to 172.16.120.212 closed.
root@ideaPc:/usr/local/SeerRobotics/robod# 
root@ideaPc:/usr/local/SeerRobotics/robod# 
root@ideaPc:/usr/local/SeerRobotics/robod# 
root@ideaPc:/usr/local/SeerRobotics/robod# ls
 appInfo   dep  'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run'   lib   linuxdeploy.sh   robod   robod.sh   Roboshop.db
root@ideaPc:/usr/local/SeerRobotics/robod# cd ..
root@ideaPc:/usr/local/SeerRobotics# ls
l3server  rbk  robod  tools
root@ideaPc:/usr/local/SeerRobotics# cd rbk/
root@ideaPc:/usr/local/SeerRobotics/rbk# ls
assets  lib  log.cfg  lua_scripts  mobilerobots  plugins  proto  rbk  rbk.cfg  rbk.error  rbk.feature  rbk.sh  tools  version
root@ideaPc:/usr/local/SeerRobotics/rbk# ./rbk.sh start
/usr/local/SeerRobotics/rbk/rbk: error while loading shared libraries: libprotobuf.so.17: cannot open shared object file: No such file or directory
root@ideaPc:/usr/local/SeerRobotics/rbk# ./rbk.sh 

Usage:
     sudo ./rbk.sh start        start run rbk
     sudo ./rbk.sh stop         stop rbk, if running at the current terminal  ctrl+c 
     sudo ./rbk.sh printlog     show log
root@ideaPc:/usr/local/SeerRobotics/rbk# ./rbk.sh stop
---------------
killed 8438
---------------
root@ideaPc:/usr/local/SeerRobotics/rbk# ./rbk.sh start
/usr/local/SeerRobotics/rbk/rbk: error while loading shared libraries: libprotobuf.so.17: cannot open shared object file: No such file or directory
root@ideaPc:/usr/local/SeerRobotics/rbk# ./rbk.sh printlog
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
^C
root@ideaPc:/usr/local/SeerRobotics/rbk# sudo ./rbk.sh start
/usr/local/SeerRobotics/rbk/rbk: error while loading shared libraries: libprotobuf.so.17: cannot open shared object file: No such file or directory
root@ideaPc:/usr/local/SeerRobotics/rbk# sudo ./rbk.sh printlog
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
^C
root@ideaPc:/usr/local/SeerRobotics/rbk# sudo ./rbk.sh stop
---------------
---------------
root@ideaPc:/usr/local/SeerRobotics/rbk# sudo ./rbk.sh printlog
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
ls: cannot access '/usr/local/etc/.SeerRobotics/rbk/diagnosis/log': No such file or directory
wc: /usr/local/etc/.SeerRobotics/rbk/diagnosis/log/: No such file or directory
^C
root@ideaPc:/usr/local/SeerRobotics/rbk# cd ..
root@ideaPc:/usr/local/SeerRobotics# ls
l3server  rbk  robod  tools
root@ideaPc:/usr/local/SeerRobotics# ssh sr@172.16.120.212
sr@172.16.120.212's password: 
Last login: Tue Jul 27 20:09:42 2021 from 172.16.120.199
sr@srs:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.192.5  netmask 255.255.255.0  broadcast 192.168.192.255
        inet6 fe80::4262:31ff:fe10:507a  prefixlen 64  scopeid 0x20<link>
        ether 40:62:31:10:50:7a  txqueuelen 1000  (Ethernet)
        RX packets 258125  bytes 236207010 (236.2 MB)
        RX errors 0  dropped 304  overruns 0  frame 0
        TX packets 120397  bytes 8013371 (8.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 40:62:31:10:50:7b  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 142  bytes 10491 (10.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 142  bytes 10491 (10.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.16.120.212  netmask 255.255.255.0  broadcast 172.16.120.255
        inet6 fe80::11f3:3818:6e6f:5bb6  prefixlen 64  scopeid 0x20<link>
        ether c0:e4:34:8c:62:71  txqueuelen 1000  (Ethernet)
        RX packets 14279  bytes 2242803 (2.2 MB)
        RX errors 0  dropped 1822  overruns 0  frame 0
        TX packets 19159  bytes 27656329 (27.6 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

sr@srs:~$ ping 192.168.192.100
PING 192.168.192.100 (192.168.192.100) 56(84) bytes of data.
64 bytes from 192.168.192.100: icmp_seq=1 ttl=64 time=0.238 ms
64 bytes from 192.168.192.100: icmp_seq=2 ttl=64 time=0.547 ms
64 bytes from 192.168.192.100: icmp_seq=3 ttl=64 time=0.806 ms
64 bytes from 192.168.192.100: icmp_seq=4 ttl=64 time=0.243 ms
64 bytes from 192.168.192.100: icmp_seq=5 ttl=64 time=0.943 ms
64 bytes from 192.168.192.100: icmp_seq=6 ttl=64 time=0.744 ms
64 bytes from 192.168.192.100: icmp_seq=7 ttl=64 time=0.245 ms
64 bytes from 192.168.192.100: icmp_seq=8 ttl=64 time=0.243 ms
64 bytes from 192.168.192.100: icmp_seq=9 ttl=64 time=0.223 ms
64 bytes from 192.168.192.100: icmp_seq=10 ttl=64 time=0.229 ms
64 bytes from 192.168.192.100: icmp_seq=11 ttl=64 time=0.211 ms
64 bytes from 192.168.192.100: icmp_seq=12 ttl=64 time=0.206 ms
64 bytes from 192.168.192.100: icmp_seq=13 ttl=64 time=0.231 ms
64 bytes from 192.168.192.100: icmp_seq=14 ttl=64 time=0.218 ms
64 bytes from 192.168.192.100: icmp_seq=15 ttl=64 time=0.223 ms
64 bytes from 192.168.192.100: icmp_seq=16 ttl=64 time=0.219 ms
64 bytes from 192.168.192.100: icmp_seq=17 ttl=64 time=0.216 ms
64 bytes from 192.168.192.100: icmp_seq=18 ttl=64 time=0.218 ms
64 bytes from 192.168.192.100: icmp_seq=19 ttl=64 time=0.252 ms
64 bytes from 192.168.192.100: icmp_seq=20 ttl=64 time=0.254 ms
64 bytes from 192.168.192.100: icmp_seq=21 ttl=64 time=0.243 ms
64 bytes from 192.168.192.100: icmp_seq=22 ttl=64 time=0.317 ms
64 bytes from 192.168.192.100: icmp_seq=23 ttl=64 time=0.220 ms
64 bytes from 192.168.192.100: icmp_seq=24 ttl=64 time=0.185 ms
64 bytes from 192.168.192.100: icmp_seq=25 ttl=64 time=0.258 ms
64 bytes from 192.168.192.100: icmp_seq=26 ttl=64 time=0.263 ms
64 bytes from 192.168.192.100: icmp_seq=27 ttl=64 time=0.224 ms
64 bytes from 192.168.192.100: icmp_seq=28 ttl=64 time=0.201 ms
64 bytes from 192.168.192.100: icmp_seq=29 ttl=64 time=0.245 ms
64 bytes from 192.168.192.100: icmp_seq=30 ttl=64 time=0.183 ms
64 bytes from 192.168.192.100: icmp_seq=31 ttl=64 time=0.171 ms
64 bytes from 192.168.192.100: icmp_seq=32 ttl=64 time=0.234 ms
64 bytes from 192.168.192.100: icmp_seq=33 ttl=64 time=0.236 ms
64 bytes from 192.168.192.100: icmp_seq=34 ttl=64 time=0.210 ms
64 bytes from 192.168.192.100: icmp_seq=35 ttl=64 time=0.231 ms
64 bytes from 192.168.192.100: icmp_seq=36 ttl=64 time=0.398 ms
64 bytes from 192.168.192.100: icmp_seq=37 ttl=64 time=0.468 ms
64 bytes from 192.168.192.100: icmp_seq=38 ttl=64 time=0.255 ms
64 bytes from 192.168.192.100: icmp_seq=39 ttl=64 time=0.570 ms
64 bytes from 192.168.192.100: icmp_seq=40 ttl=64 time=0.243 ms
64 bytes from 192.168.192.100: icmp_seq=41 ttl=64 time=0.836 ms
64 bytes from 192.168.192.100: icmp_seq=42 ttl=64 time=0.243 ms
64 bytes from 192.168.192.100: icmp_seq=43 ttl=64 time=0.172 ms
64 bytes from 192.168.192.100: icmp_seq=44 ttl=64 time=0.215 ms
64 bytes from 192.168.192.100: icmp_seq=45 ttl=64 time=0.219 ms
64 bytes from 192.168.192.100: icmp_seq=46 ttl=64 time=0.215 ms
64 bytes from 192.168.192.100: icmp_seq=47 ttl=64 time=0.231 ms
64 bytes from 192.168.192.100: icmp_seq=48 ttl=64 time=0.253 ms
64 bytes from 192.168.192.100: icmp_seq=49 ttl=64 time=0.264 ms
64 bytes from 192.168.192.100: icmp_seq=50 ttl=64 time=0.415 ms
64 bytes from 192.168.192.100: icmp_seq=51 ttl=64 time=0.224 ms
64 bytes from 192.168.192.100: icmp_seq=56 ttl=64 time=0.857 ms
64 bytes from 192.168.192.100: icmp_seq=57 ttl=64 time=0.220 ms
64 bytes from 192.168.192.100: icmp_seq=58 ttl=64 time=0.217 ms
64 bytes from 192.168.192.100: icmp_seq=59 ttl=64 time=0.617 ms
64 bytes from 192.168.192.100: icmp_seq=60 ttl=64 time=0.275 ms
64 bytes from 192.168.192.100: icmp_seq=61 ttl=64 time=0.655 ms
64 bytes from 192.168.192.100: icmp_seq=62 ttl=64 time=0.688 ms
64 bytes from 192.168.192.100: icmp_seq=63 ttl=64 time=0.253 ms
64 bytes from 192.168.192.100: icmp_seq=64 ttl=64 time=0.236 ms
64 bytes from 192.168.192.100: icmp_seq=65 ttl=64 time=0.222 ms
64 bytes from 192.168.192.100: icmp_seq=66 ttl=64 time=0.195 ms
64 bytes from 192.168.192.100: icmp_seq=67 ttl=64 time=0.325 ms
64 bytes from 192.168.192.100: icmp_seq=68 ttl=64 time=0.213 ms
64 bytes from 192.168.192.100: icmp_seq=69 ttl=64 time=0.240 ms
64 bytes from 192.168.192.100: icmp_seq=70 ttl=64 time=0.324 ms
64 bytes from 192.168.192.100: icmp_seq=71 ttl=64 time=0.253 ms
64 bytes from 192.168.192.100: icmp_seq=72 ttl=64 time=0.208 ms
64 bytes from 192.168.192.100: icmp_seq=73 ttl=64 time=0.222 ms
64 bytes from 192.168.192.100: icmp_seq=74 ttl=64 time=0.219 ms
^C
--- 192.168.192.100 ping statistics ---
74 packets transmitted, 70 received, 5% packet loss, time 74724ms
rtt min/avg/max/mdev = 0.171/0.311/0.943/0.182 ms
sr@srs:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.192.5  netmask 255.255.255.0  broadcast 192.168.192.255
        inet6 fe80::4262:31ff:fe10:507a  prefixlen 64  scopeid 0x20<link>
        ether 40:62:31:10:50:7a  txqueuelen 1000  (Ethernet)
        RX packets 336448  bytes 306328695 (306.3 MB)
        RX errors 0  dropped 396  overruns 0  frame 0
        TX packets 156830  bytes 10440312 (10.4 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 40:62:31:10:50:7b  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 142  bytes 10491 (10.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 142  bytes 10491 (10.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.16.120.212  netmask 255.255.255.0  broadcast 172.16.120.255
        inet6 fe80::11f3:3818:6e6f:5bb6  prefixlen 64  scopeid 0x20<link>
        ether c0:e4:34:8c:62:71  txqueuelen 1000  (Ethernet)
        RX packets 19354  bytes 2969825 (2.9 MB)
        RX errors 0  dropped 2374  overruns 0  frame 0
        TX packets 25097  bytes 36104346 (36.1 MB)
