import numpy as np
import matplotlib.pyplot as plt

y=[0,0.025,0.05,0.075,0.1,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.3,0.325,0.35,0.375,0.4,0.425,0.45,0.475,0.5,0.525,0.55,0.575,0.6,0.625,0.65,0.675,0.7,0.725,0.75,0.775,0.8,0.825,0.85,0.875,0.9,0.925,0.95,0.975,1]

z=[30,27.9396,25.945,24.9488,23.9837,23.3419,22.7197,22.2549,21.8042,21.4456,21.0979,20.8102,20.5312,20.2943,20.0645,19.8658,19.6732,19.5043,19.3406,19.1958,19.0555,18.9305,18.8094,18.701,18.5962,18.502,18.411,18.3291,18.2501,18.179,18.1105,18.049,17.9897,17.9368,17.8859,17.8406,17.7972,17.7589,17.7224,17.6905,17.6602]

y1=[0,0.0125,0.025,0.0375,0.05,0.0625,0.075,0.0875,0.1,0.1125,0.125,0.1375,0.15,0.1625,0.175,0.1875,0.2,0.2125,0.225,0.2375,0.25,0.2625,0.275,0.2875,0.3,0.3125,0.325,0.3375,0.35,0.3625,0.375,0.3875,0.4,0.4125,0.425,0.4375,0.45,0.4625,0.475,0.4875,0.5,0.5125,0.525,0.5375,0.55,0.5625,0.575,0.5875,0.6,0.6125,0.625,0.6375,0.65,0.6625,0.675,0.6875,0.7,0.7125,0.725,0.7375,0.75,0.7625,0.775,0.7875,0.8,0.8125,0.825,0.8375,0.85,0.8625,0.875,0.8875,0.9,0.9125,0.925,0.9375,0.95,0.9625,0.975,0.9875,1]

z1=[30,25.7845,21.638,19.5659,17.5275,16.1702,14.8349,13.8354,12.8522,12.0677,11.2961,10.6554,10.0252,9.48751,8.95869,8.49853,8.04603,7.64645,7.25358,6.90269,6.55775,6.24692,5.94142,5.66415,5.3917,5.14299,4.89867,4.67459,4.45452,4.2519,4.05296,3.86924,3.6889,3.52192,3.35807,3.20605,3.05694,2.91837,2.7825,2.65608,2.53217,2.41678,2.30374,2.19842,2.09528,1.99917,1.9051,1.81745,1.73171,1.65185,1.57379,1.50115,1.43018,1.36421,1.29983,1.24007,1.1818,1.12783,1.07526,1.02669,0.979446,0.935938,0.893683,0.854927,0.817358,0.783078,0.749922,0.719865,0.690876,0.664818,0.639775,0.617512,0.596216,0.577566,0.559839,0.54464,0.530323,0.518427,0.507377,0.498654,0.490745]

fig1=plt.figure()
plt.plot(y,z)
plt.xlabel(r'$Distance$ $x(m)$',fontsize=15)
plt.ylabel(r'$Concentration$ $c$ $(kg/m^3)$',fontsize=15)
plt.title(r'$Diffusion$ $in$ $a$ $rod$ $for$ $Input$ $1$',fontsize=20)

fig2=plt.figure()
plt.plot(y1,z1)
plt.xlabel(r'$Distance$ $x(m)$',fontsize=15)
plt.ylabel(r'$Concentration$ $c$ $(kg/m^3)$',fontsize=15)
plt.title(r'$Diffusion$ $in$ $a$ $rod$ $for$ $Input$ $2$',fontsize=20)

plt.show()