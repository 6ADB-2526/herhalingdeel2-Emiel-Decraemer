# 5. Toon spreiding van 2 variabelen

import random
import matplotlib.pyplot as plt

x = [random.randint(1, 100) for _ in range(50)]
y = [i + random.randint(-10, 10) for i in x]

plt.plot(x,y)
plt.show()