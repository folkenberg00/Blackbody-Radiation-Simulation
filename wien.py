#!/usr/bin/env python3

"""     09.01.2023
	Folkenberg, Siro
        Nuclear Engineering and Thermal Physics, National Research Nuclear University-IATE, Russia.

      	================== BLACKBODY RADIATION SIMULATION  =================================
		    ### WIEN'S DISPLACEMENT LAW ###

	NB: All physical quantities in SI units
"""


import matplotlib.pyplot as mpl
import numpy as np

#constants
c = 3.0*10**8; h = 6.626e-34; k = 1.38e-23
def intens(lambd, T):
	a = 2.0*h*c**2
	b = h*c/(lambd*k*T)
	intensity = a/((lambd**5)*(np.exp(b)-1))
	return intensity
wavs = np.arange(1e-9, 3e-6, 1e-9)
intensity4 = intens(wavs, 4000)
intensity5 = intens(wavs, 5000)
intensity6 = intens(wavs, 6000)
intensity7 = intens(wavs, 7000)


fig = mpl.figure(facecolor = 'grey', figsize=(14, 6.6))
ax = fig.add_subplot(111)
ax.set_ylabel('Power Density($10^{13} watts/m^3$)')
ax.set_xlabel('Wavelength, $\lambda\; (\mathrm{nm})$')
ax.grid(True)
ax.set_facecolor('k')
ax.set_title('Blackbody Radiation')
ax.grid(which = 'minor', linewidth = 0.5, linestyle=":", color='#EEEEEE')
ax.grid(which = 'major', linewidth = 0.7)
ax.minorticks_on()
ax.text(1, -0.9e+12, 'X-Ray', color='w', verticalalignment='top',
	fontdict={'fontsize': 9}, bbox = dict(facecolor='k', alpha=1))
ax.text(220, -0.9e+12, 'UV', color='w', verticalalignment='top',
        fontdict={'fontsize': 9}, bbox = dict(facecolor='k', alpha=1))
ax.text(480, -0.9e+12, 'Visible', color='w', verticalalignment='top',
        fontdict={'fontsize': 9}, bbox = dict(facecolor='k', alpha=1))
ax.text(1200, -0.9e+12, 'Near Infrared', color='w', verticalalignment='top',
        fontdict={'fontsize': 9}, bbox = dict(facecolor='k', alpha=1))
ax.text(2700, -0.9e+12, 'Far Infrared', color='w', verticalalignment='top',
        fontdict={'fontsize': 9}, bbox = dict(facecolor='k', alpha=1))

spectrum = {(380, 440):'#ee82ee', (440, 460):'#4b0082', (460, 495): '#0000ff',
		(495, 570): '#00ff00', (570, 590): '#ffff00', (590, 620): '#ffa500',
		(620, 750): '#ff0000', (750, 2200): '#E60000'}

for wav_range, rgb in spectrum.items():
	ax.axvspan(*wav_range, color=rgb, alpha=1)
mpl.plot(wavs*1e9, intensity4, 'w--')
mpl.text(640, 6.5e+12, '4000 K', color = 'w', fontdict={'fontsize': 10},
	bbox=dict(facecolor="k", alpha=1))
mpl.plot(wavs*1e9, intensity5, 'w--')
mpl.text(515, 1.45e+13, '5000 K', color = 'w', fontdict={'fontsize': 10},
        bbox=dict(facecolor="k", alpha=1))
mpl.plot(wavs*1e9, intensity6, 'w--')
mpl.text(415, 3.4e+13, '6000 K', color = 'w', fontdict={'fontsize': 10},
        bbox=dict(facecolor="k", alpha=1))
mpl.plot(wavs*1e9, intensity7, 'w--')
mpl.text(475, 6.9e+13, '7000 K', color = 'w', fontdict={'fontsize': 10},
        bbox=dict(facecolor="k", alpha=1))
mpl.savefig('wien.plot.pdf')
mpl.show()


