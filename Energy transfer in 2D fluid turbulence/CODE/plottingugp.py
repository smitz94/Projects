import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('D:\\STUDY\\SEM 7\\UGP\\shaheen run3\\run3\\data\\out\\glob.d')
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


fig1 = plt.figure()	
plt.xlabel(r'$t$', fontsize=28,fontweight='bold')
plt.ylabel(r'$E$', fontsize=28)
plt.title('Total Energy E vs Time t',fontsize=30)
plt.tick_params(axis='both',labelsize=19)
plt.plot(t,E)
plt.grid()

fig2=plt.figure()
plt.xlabel(r'$t$', fontsize=20)
plt.ylabel(r'$Dissipation Coefficient$', fontsize=20)
plt.title(r'Dissipation Coefficient vs Time t')
plt.plot(t,diss)
plt.grid()

fig3=plt.figure()
plt.xlabel(r'$t$', fontsize=28)
plt.ylabel(r'$kmax$ $\eta$', fontsize=28)
plt.title(r'kmax $\eta$ vs Time t',fontsize=30)
plt.tick_params(axis='both',labelsize=19)
plt.plot(t,kmax)
plt.grid()

fig4=plt.figure()
plt.xlabel(r'$t$', fontsize=20)
plt.ylabel(r'$\nu$', fontsize=20)
plt.title(r'$\nu$ vs Time t')
plt.plot(t,nu)
plt.grid()

fig5=plt.figure()
plt.xlabel(r'$t$', fontsize=28)
plt.ylabel(r'$Re_\nu$', fontsize=28)
plt.title(r'$Re_\nu$ vs Time t',fontsize=30)
plt.tick_params(axis='both',labelsize=19)
plt.plot(t,Re_nu)
plt.grid()

fig6 = plt.figure()
plt.xlabel(r'$t$', fontsize=20)
plt.ylabel(r'$E_x$', fontsize=20)
plt.title(r'$E_x$ vs Time t')
plt.plot(t,Ex)
plt.grid()

fig7=plt.figure()
plt.xlabel(r'$t$', fontsize=20)
plt.ylabel(r'$E_y$', fontsize=20)
plt.title(r'$E_y$ vs Time t')
plt.plot(t,Ey)
plt.grid()

fig8=plt.figure()
plt.xlabel(r'$t$', fontsize=20)
plt.ylabel(r'$E_z$', fontsize=20)
plt.title(r'$E_z$ vs Time t')
plt.plot(t,Ez)
plt.grid()

fig9=plt.figure()
plt.xlabel(r'$t$', fontsize=20)
plt.ylabel(r'$dt$', fontsize=20)
plt.title('dt vs Time t')
plt.plot(t,dt)
plt.grid()

plt.show()

