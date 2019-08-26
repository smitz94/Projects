import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('E:\glob.d')
t = data[:,0]
E = data[:,1]
diss= data[:,2]
kmax= data[:,8]
nu=data[:,9]
Re_nu = data[:,10]
Ex = data[:,12]
Ey = data[:,13]
Ez = data[:,14]
dt = data[:,11]

Emean=np.mean(E[40000:100001])
kmaxmean=np.mean(kmax[40000:100001])

u=(np.sqrt(Emean*2))

Re= u*2*np.pi/0.01

