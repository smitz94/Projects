from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager, patches

Presentation = 1
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


nu = 0.01


data_spectrum = np.loadtxt('D:\\STUDY\\SEM 7\\UGP\\shaheen run3\\run3\\data\\out\\spectrum.d', comments='%%')
k = np.arange(0,len(data_spectrum[0,:]),1)
Eu = ( data_spectrum[0,:] + data_spectrum[1,:])

fig, axes = plt.subplots(figsize=(E,F))



rect1 = patches.Rectangle((40,10**-23), 1, 100, color='#ADADAD')
axes.add_patch(rect1)
axes.loglog(k,Eu,'r',linewidth = lw1,label = r'$E_{u}(k)$')
x0 = np.linspace(3,130,100)
axes.loglog(x0,2.1*x0**(-5/3),'b',linewidth=3,label = r'$k^{-12.1}$')

x1=np.linspace(30,800,100)
axes.loglog(x1,40000000*x1**(-6),'g',linewidth=3,label = r'$k^{6}$')

axes.annotate(r'$k^{-6}$', xy=(500, 3e-9), xytext=(600, 1e-7),arrowprops=dict(facecolor='black', shrink=0.05),)
axes.annotate(r'$k^{-5/3}$', xy=(100, 1e-3), xytext=(140, 1e-1),arrowprops=dict(facecolor='black', shrink=0.05),)

axes.tick_params(axis='both',labelsize=18)
plt.xlabel('k', fontsize=25)
plt.ylabel('E(k)',fontsize=25)
plt.title('Spectrum of E(k) vs k', fontsize=28)
#plt.xlim(1,310)
#plt.ylim(1e-10,10)

plt.show()