from pydub import AudioSegment
from os import walk
import sys

# Get list mp3 file
_,_,filenames=next(walk('/home/idea/orangepi/nodejs/5_controlSoundWithTimerAndConfigOverWeb/uploads'))

totalFiles = len(filenames)
# Convert mp3 file to wav and reduce volume
for i in range(totalFiles):
  soundMp3 = AudioSegment.from_mp3('/home/idea/orangepi/nodejs/5_controlSoundWithTimerAndConfigOverWeb/uploads/' + filenames[i])
  soundMp3ReduceVolume = soundMp3 - int(sys.argv[1])
  soundMp3ReduceVolume.export('/home/idea/wavFile/' + str(i) + '.wav', format='wav')

