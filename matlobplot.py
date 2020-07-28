import matplotlib.pyplot as plt
import numpy as np
import math
x=np.arange(0, math.pi*2, 0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("\u03F4")
plt.ylabel("Sin(\u03F4)")
plt.title("Sine Wave")
plt.show()
