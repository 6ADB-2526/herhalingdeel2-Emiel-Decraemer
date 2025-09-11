# 3. Visualiseer de frequentie van letters in een woord

from collections import Counter
import matplotlib.pyplot as plt

woord = "matplotlib"
frequentie = Counter(woord)
print(frequentie)

plt.plot(frequentie)
plt.show()