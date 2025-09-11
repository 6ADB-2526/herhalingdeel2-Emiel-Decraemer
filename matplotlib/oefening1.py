# 1. Plot een eenvoudige lijn van y = 2x
import matplotlib.pyplot as plt

x = list(range(0, 11))
y = [2 * i for i in x]

plt.plot(x,y)
plt.show()