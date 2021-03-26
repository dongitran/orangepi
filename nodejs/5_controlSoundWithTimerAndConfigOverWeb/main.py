from pydub import AudioSegment
from os import walk
import sys
from time import sleep
from datetime import datetime
import simpleaudio as sa

# Get list mp3 file
_,_,filenames=next(walk('/home/idea/orangepi/nodejs/5_controlSoundWithTimerAndConfigOverWeb/uploads'))

totalFiles = len(filenames)
# Convert mp3 file to wav and reduce volume
for i in range(totalFiles):
  soundMp3 = AudioSegment.from_mp3('/home/idea/orangepi/nodejs/5_controlSoundWithTimerAndConfigOverWeb/uploads/' + filenames[i])
  soundMp3ReduceVolume = soundMp3 - int(sys.argv[1])
  soundMp3ReduceVolume.export('/home/idea/wavFile/' + str(i) + '.wav', format='wav')


while True:
  now = datetime.now()
  #if now.minute == 55:
  if False:
    # Get list mp3 file
    _,_,filenames=next(walk('/home/idea/orangepi/nodejs/5_controlSoundWithTimerAndConfigOverWeb/uploads'))

    totalFiles = len(filenames)
    # Convert mp3 file to wav and reduce volume
    for i in range(totalFiles):
      soundMp3 = AudioSegment.from_mp3('/home/idea/orangepi/nodejs/5_controlSoundWithTimerAndConfigOverWeb/uploads/' + filenames[i])
      soundMp3ReduceVolume = soundMp3 - int(sys.argv[1])
      soundMp3ReduceVolume.export('/home/idea/wavFile/' + str(i) + '.wav', format='wav')

  isPlay = False
  player = None
  if now.minute == 5 or now.minute == 15 or now.minute == 25 or now.minute == 35 or now.minute == 45 or now.minute == 55: 
    print('SoundControl - Play....')
    counterPlay = 0
    wavDat = sa.WaveObject.from_wave_file('/home/idea/wavFile/' + str(counterPlay) + '.wav')
    player = wavDat.play()
    
    while True:
      if not player.is_playing():
        if counterPlay < (totalFiles - 1):
          counterPlay = counterPlay + 1
        else:
          counterPlay = 0
        wavDat = sa.WaveObject.from_wave_file('/home/idea/wavFile/' + str(counterPlay) + '.wav')
        player = wavDat.play()
      now = datetime.now()
      if now.minute == 6 or now.minute == 16 or now.minute == 26 or now.minute == 36 or now.minute == 46 or now.minute == 56: 
        player.stop()
        print('SoundControl - Stop!')
        break
      sleep(1)
  sleep(1)


