import matplotlib.pyplot as plt

waarden = [56.8,3.0,1.8,22.1,4.8,9.2,1.8]
labels = ['Win7','Vista','NT*','WinXP','Linux','Mac','Mobile']
explode = [0,0,0,0,0,0,0.2]

fig1, ax1 = plt.subplots()
ax1.pie(waarden, labels=labels, explode=explode)
ax1.axis('equal')

fig2,ax2 = plt.subplots()
ax2.pie(waarden, labels=labels, explode=explode)
ax2.axis('equal')

plt.show()