from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
#from scipy.interpolate import splrep, splev
#import matplotlib
from matplotlib import rc, font_manager, patches

Presentation = 0
if Presentation == True:
  A = 28
  
  B = 18
  C = 2
  D = 10
  
  E = 13
  F = 8
  
  G = 35
  
  lw0 = 2
  lw1 = 6
  lw2 = 8
else:
  A = 10
  
  B = 6.5
  C = 0.6
  D = 4
  
  E = 3.5
  F = 2.5
  
  G = 11
  
  lw0 = 0.5
  lw1 = 1.5
  lw2 = 2.5

font = {'family' : 'serif', 'weight' : 'normal', 'size' : A}
plt.rc('font', **font)

plt.rcParams['xtick.major.size'] = B
plt.rcParams['xtick.major.width'] = C
plt.rcParams['xtick.minor.size'] = D
plt.rcParams['xtick.minor.width'] = C
plt.rcParams['ytick.major.size'] = B
plt.rcParams['ytick.major.width'] = C
plt.rcParams['ytick.minor.size'] = D
plt.rcParams['ytick.minor.width'] = C






data_flux = np.loadtxt('D:\\STUDY\\SEM 7\\UGP\\shaheen run3\\run3\\data\\out\\flux.d', comments='%%')
kf  = np.array([0, 2, 4, 8, 10.0781, 12.6959, 15.9937, 20.1482, 25.3819, 31.975, 40.2807, 50.7439, 63.925, 80.5299, 101.448, 127.8, 160.997, 202.817, 255.5, 511])
i =len(data_flux[0,:])-1
pu = data_flux[0,:][0:i]
ptheta = data_flux[1,:][0:i]

fig, axes = plt.subplots(figsize=(E,F))
rect1 = patches.Rectangle((40,0), 1, 1, color='#ADADAD')
axes.add_patch(rect1)
rect1 = patches.Rectangle((40,0), 1, -1e1, color='#ADADAD')
axes.add_patch(rect1)
axes.plot(kf,(pu),'r-', linewidth=lw1, label=r'$\Pi_u(k)$')
axes.axhline(0,color='k')
x0 = np.linspace(6.0,80.0,100)
#axes.plot(x0,-0.02*x0**(-0.98),'k',linewidth=lw0,label = r'$k^{-0.98}$')
#axes.legend(loc=0,prop={'size':A*0.8})
#axes.plot(x0,5*10**5*y0,'k',linewidth=lw0)
#axes.axis([1.5,100,-1e-1,1e-2])
axes.set_xscale('log')
axes.set_yscale('symlog',linthreshy=1e-6)
axes.set_xlabel(r'$k$' , fontsize=22)
axes.set_ylabel(r'$\Pi_u(k)$' , fontsize=22)
fig.tight_layout()
plt.tick_params(axis='both',labelsize=14)
plt.title(r'$\Pi_u(k)$ vs k', fontsize=26)
plt.show()