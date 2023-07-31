import numpy as np
import matplotlib.pylab as plt

t = np.linspace(1,10)
dt=0.2

x1=0.64
x2=-0.43
x3=0.63
X=[[x1,x2,x3]]


# Convexo K
k1=0.5*np.cos(t)+0.25
k2=0.5*np.sin(t)
k3=np.sqrt(1-k1**2-k2**2)

A=[]
# Projeção sobre K
for i in t:
    A.append(np.arccos((0.5*np.cos(i)+0.25)*x1+(0.5*np.sin(i))*x2+(np.sqrt(1-(0.5*np.cos(i)+0.25)**2-(0.5*np.sin(i))**2))*x3))

tmin=t[A.index(min(np.array(A)))]
print(tmin)


comprimentoDeArco=np.arccos(x1*k1+x2*k2+x3*k3)

#Convexo U
u1=0.5*np.cos(t)-0.25
u2=0.5*np.sin(t)
u3=np.sqrt(1-k1**2-k2**2)

plt.plot(t,np.arccos(x1*k1+x2*k2+x3*k3))
plt.plot(t,np.arccos(x1*u1+x2*u2+x3*u3))
plt.show()

