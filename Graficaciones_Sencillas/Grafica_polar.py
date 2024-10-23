import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,4*np.pi)
r = 32 + 4*theta

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta,r)

plt.show()
