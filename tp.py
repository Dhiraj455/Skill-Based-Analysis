import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["App Development", "Game Development", "Web Development", "Graphic Designer"]

plt.pie(y, labels = mylabels)
plt.show() 