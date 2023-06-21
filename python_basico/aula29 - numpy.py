import numpy as np
import matplotlib.pylab as plt
# x = np.linspace(-2, 2, 201)
# plt.plot(x,np.sin(x))
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.axis('tight')
# plt.show()

t = np.linspace(0,2*np.pi)
plt.plot(np.sin(t),np.cos(t))
plt.show()