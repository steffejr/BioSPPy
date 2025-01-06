#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:22:57 2025

@author: jasonsteffener
"""

from biosppy import storage
# from biosppy.signals import ecg as SignalsECG
# from biosppy.synthesizers import as SynthECG
import biosppy
import numpy as np
import matplotlib.pyplot as plt

# load raw ECG signal
signal, mdata = storage.load_txt('/Users/jasonsteffener/Documents/GitHub/BioSPPy/examples/ecg.txt')

# process it and plot
out = biosppy.signals.ecg.ecg(signal=signal, sampling_rate=1000., show=True)





sampling_rate = 1000
beats = 6
noise_amplitude = 0.1
variability = 0.4
ECGtotal = np.array([])
for i in range(beats):
    ECGwave, _, _ = biosppy.synthesizers.ecg.ecg(sampling_rate=sampling_rate, var=variability)
    ECGtotal = np.concatenate((ECGtotal, ECGwave))
t = np.arange(0, len(ECGtotal)) / sampling_rate

# add powerline noise (50 Hz)
noise = noise_amplitude * np.sin(50 * (2 * np.pi) * t)
ECGtotal += noise

plt.plot(t, ECGtotal)
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude (mV)")
plt.grid()
plt.title("ECG")

plt.show()



out = biosppy.signals.ecg.ecg(signal=ECGtotal, sampling_rate=1000., show=True)

