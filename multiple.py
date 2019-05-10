import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 50)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, 'ro--', x, z, 'kD:')
plt.title('Sine vs Cosine Curves')
plt.axhline(0, color='grey')
plt.axvline(0, color='grey')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(('$y=sinx$', '$y=cosx$'))
plt.savefig('images/sinevscosine.png')
plt.show()
