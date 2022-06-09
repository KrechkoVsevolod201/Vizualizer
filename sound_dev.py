import wave
import numpy as np
import matplotlib.pyplot as plt
from os import path
from pydub import AudioSegment
import matplotlib.ticker as ticker
import math

from scipy.io import wavfile

file = wave.open("Saves\\пэс.wav")
# print ('--------- звуковое сообщение ------------')
# for item in enumerate(WAVE.getparams()):
#     print(item)
a = file.getparams().nframes  # общее количество кадров
f = file.getparams().framerate  # частота дискретизации
sample_time = 1 / f  # временной интервал точки выборки
time = a / f  # длина звукового сигнала
sample_frequency, audio_sequence = wavfile.read("Saves\\пэс.wav")
# print (audio_sequence) # Размер каждого кадра аудиосигнала
x_seq = np.arange(0, time, sample_time)

plt.plot(x_seq, audio_sequence, 'blue')
plt.xlabel("time (s)")
plt.show()
