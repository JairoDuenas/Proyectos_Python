# TODO $ pip3 install matplotlib

import matplotlib.pyplot as plt

x1 = [2, 4, 5, 6]
y1 = [2, 3, 6, 7]

plt.plot(x1, y1, label='Line 1',color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=8)

plt.ylim(1,8)
plt.xlim(1,8)

x2 = [2, 3, 4, 4]
y2 = [3, 4, 5, 6]

plt.plot(x2, y2, label='Line 2')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph - Two Lines')

plt.legend()

plt.show()