import numpy as np
import pylab as plt

x=[6000,7000,8000,9000,10000]
y=[73,80,85,87,89]
plt.plot(x,y)

x1=(7000,8000,9000,10000,11000)
y2=(80,83,85,86,88)
plt.plot(x1,y2)

plt.xlabel('Voltaje [V]')
plt.ylabel('Eficiencia [%]')
plt.grid(True)
plt.plot(x,y,color="purple")
plt.plot(x1,y2,color="pink")

plt.savefig('graph.png')

plt.show()
