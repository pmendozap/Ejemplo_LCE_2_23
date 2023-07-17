import sys 
from matplotlib.pyplot import *
from math import exp
import numpy as np

sys.path.insert(0, '../tools')
from lectureSpicePrint import lectureSpicePrint

data = lectureSpicePrint("out_00_b.txt")
t = (data["time"] - data["time"][0])*1000 #elimino offset de tiempo y paso a milisegundos
vr = data["v(n1)"]
ir = (data["i(v1)"]*(-1))*1000 #La corriente en V1 sale del nodo + por lo que es negativa. Se pasa a miliamps

fig, axs = subplots(2)
fig.suptitle('Con subplot')
axs[0].set_xlabel('time (ms)')
axs[1].set_xlabel('time (ms)')
axs[0].set_ylabel('Vr (V)')
axs[1].set_ylabel('Ir (mA)')
axs[0].plot(t, vr)
axs[1].plot(t, ir)

show()

fig, ax1 = subplots()

color = 'tab:red'
ax1.set_xlabel('time (ms)')
ax1.set_ylabel('Vr (V)', color=color)
ax1.plot(t, vr, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 

color = 'tab:blue'
ax2.set_ylabel('Ir (mA)', color=color) 
ax2.plot(t, ir, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
show()


