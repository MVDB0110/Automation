import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
minions = ('Minion1','Minion2')
ybar = np.arange(len(minions))
xbar = (percentage, 20)

ax.barh(minions, xbar, align='center',color='red', ecolor='black')
ax.set_yticks(ybar)
ax.set_yticklabels(minions)
ax.set(xlim=[0,100])
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Percentage')
ax.set_title('Memory Usage')

plt.show()