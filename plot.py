import matplotlib.pyplot as plt
import numpy as np
import wave
import matplotlib.patches as patches
import matplotlib.cbook as cbook
import sys


spf = wave.open('wav//ed//mp3abstracted.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


fig = plt.figure(1)
print(fig.get_axes())
plt.title('Signal Wave...')
plt.plot(signal)
plt.show()

