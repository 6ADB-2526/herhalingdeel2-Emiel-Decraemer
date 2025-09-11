# 2. Vergelijk y = x, y = x^2 en y = x^3

import matplotlib.pyplot as plt

x = list(range(0, 11))
y1 = x
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

plt.plot(x,y1,y2,y3)
plt.show()