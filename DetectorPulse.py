import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

from scipy.ndimage.filters import gaussian_filter

# Noise level 
noise_level = 0.05

# The width of the pulse in units of samples 
resolution  = 50.0

# Initialize the signal and create a delta-function pulse 
signal = np.zeros(2000);
signal[500] = 100

# Add extra spikes for a non-Gaussian like pulse 
# signal[600] = 50
# signal[700] = 25
# signal[800] = 10

# The noise to be added 
noise = noise_level*np.random.randn(len(signal))

# Create the figure 
plt.figure(num=None, figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')    

# And then plot the Gaussian pulse 
plt.plot(gaussian_filter(signal,sigma=resolution)+noise,'k-')

# Remove the axis labels (looks nicer in presentations)
ax = plt.gca()
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])

# Add a grid and show 
plt.grid()
plt.show()
