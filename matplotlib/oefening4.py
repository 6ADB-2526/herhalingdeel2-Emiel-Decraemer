# 4. Visualiseer verdeling van tijd per activiteit

import matplotlib.pyplot as plt

activiteiten = ["Studeren", "Sport", "Slapen", "Vrije tijd"]
uren = [5, 2, 8, 9]

plt.plot(uren)
plt.xlabel(activiteiten)
plt.show()