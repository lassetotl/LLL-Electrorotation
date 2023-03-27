### Rotation spectra function ###
#data [2d array] - rpm rotation matrix
#freq [1d array]- corresponding frequencies
#color [string] - https://matplotlib.org/stable/gallery/color/named_colors.html
#date [string] - 'dd.mm.yy'
#n [integer] - interpolation points
### Call this function after making a figure, before showing!

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def Rotation_Spectra(data, freq, color, date, n=1000, detail = True):
    # plot data
    if detail == True:
        for i in range(len(data)):
            plt.scatter(freq, data[i,:], color=color, marker = 'o',
                        lw = 2, alpha = 0.5)

    # interpolate mean data and plot
    ERM_m = np.zeros(len(freq))
    for i in list(range(len(freq))):
        ERM_m[i] = (np.mean(data[:,i]))
    y = interp1d(freq, ERM_m)
    x = np.linspace(min(freq)+0.001, max(freq), n)
    plt.plot(x, y(x), color=color, lw = 3, label = f'{date} data')

    # calculate peak and turning point
    ymax = np.max(y(x))
    ymax_i = np.argmax(y(x))
    xmax = x[ymax_i]

    yturn_i = np.argmin(abs(y(x))) #abs value closest to zero
    xturn = x[yturn_i]
    if detail == True:
        plt.hlines(ymax, -0.2, xmax, color = color, linestyle = '--', lw = 3,
              label = f'Peak at {round(xmax, 3)} MHz ({round(ymax, 3)} rpm)')
        plt.vlines(xturn, -20, 0, color = color, linestyle = 'dotted', lw = 3,
                  label = f'Turning point at {round(xturn, 3)} MHz')

    return x, y, ymax, ymax_i, xmax, xturn
    #
