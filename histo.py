import numpy as np
import matplotlib.pyplot as plt
s = int(input("combien de fois voulez vous répeter l'experience ? :"))
np.random.seed(1234)
t1 = np.random.randint(1, 45, size=s)
plt.hist(t1, bins=range(1, 46), align='left', rwidth=1)
plt.xlabel('Numéros tirés')
plt.ylabel('Nombre de fois')
plt.title('Histogramme loto')
plt.show()
