import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-2*np.pi, 2*np.pi)
y = 3*x*np.sin(x)-2*x
z = 3*(x*np.cos(x)+np.sin(x))-2
plt.plot(x, y)
plt.plot(x, z)
plt.title('q1')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(('$f(x)$', "$f'(x)$"))
plt.show()


t = np.linspace(0, 7, 50)
x = 0.4*t**3-2-t**2-5*t+13
v = 1.2*t**2-4*t-5
a = 2.4*t-4
plt.subplot(5, 1, 1)
plt.xlabel('t')
plt.ylabel("$m$")
plt.plot(t, x)

plt.subplot(5, 1, 3)
plt.plot(t, v,)
plt.xlabel('t')
plt.ylabel('$ms^{-1}$')

plt.subplot(5, 1, 5)
plt.plot(t, a)
plt.xlabel('t')
plt.ylabel('$ms^{-2}$')
plt.show()


theta = np.linspace(0, np.pi*0.5)
r1 = ((50**2)/9.8)*np.sin(2*theta)
r2 = ((75**2)/9.8)*np.sin(2*theta)
r3 = ((100**2)/9.8)*np.sin(2*theta)
r4 = ((120**2)/9.8)*np.sin(2*theta)
plt.title('q3')
plt.plot(theta, r1)
plt.plot(theta, r2)
plt.plot(theta, r3)
plt.plot(theta, r4)
plt.title('Projectile')
plt.legend(('$v=50ms^{-1}$', '$v=75ms^{-1}$',
            '$v=100ms^{-1}$', '$v=120ms^{-1}$'))
plt.xlabel('$Î¸$')
plt.ylabel('Range')
plt.show()


t = np.linspace(0, 20)
x = (2+4*np.cos(t))*np.cos(t)
y = (2+4*np.cos(t))*np.sin(t)
x = t**2
plt.title('q4')
plt.plot(t, x)
plt.plot(t, y)
plt.plot(t, z)
plt.legend(('x', 'y', 'z'))
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
x = np.linspace(-5, 5, 50)
y = x
x, y = np.meshgrid(x, y)
z = (x*y*(x**2-y**2))/(x**2+y**2)
ax.plot_surface(x, y, z)
fig = plt.figure()
ax = Axes3D(fig)
z = np.cos(x)*np.cos(y)*np.e**(-np.sqrt(x**2+y**2)/4)
ax.plot_surface(x, y, z, cmap='gist_earth')
