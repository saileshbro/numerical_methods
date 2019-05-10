# To plot the given functions on the domain [-5,5]

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2, 5, 50)

# sin cosine curve
y = np.sin(x)
z = np.cos(x)
plt.figure(1)
plt.plot(x, y, 'ro--')
# creating the x=0 and y=0 axis
plt.axhline(0, color='grey')
plt.axvline(0, color='grey')
plt.title('Sine Curve', fontsize=22,
          fontfamily='Monospace')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.figure(2)
plt.plot(x, z, 'kx-')
plt.axhline(0, color='grey')
plt.axvline(0, color='grey')
plt.title('Cosine Curves', fontsize=22,
          fontfamily='Monospace')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()
