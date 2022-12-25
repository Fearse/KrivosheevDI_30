#!/usr/bin/env python
# coding=utf8
import numpy as np

cityNumbers = int(input())
pathMatrix = np.zeros([cityNumbers, cityNumbers])
for i in range(0, cityNumbers, 1):
    for j in range(0, cityNumbers, 1):
        if i < j:
            pathMatrix[i, j] = int(input(f"Path between {i} and {j}:"))
            pathMatrix[j, i] = pathMatrix[i, j]
        elif i == j:
            pathMatrix[i, j] = float("inf")
startCity = 0
way = []
"""
pathMatrix = [[float('inf'), 6, 7, 8, 9],
              [6, float('inf'), 10, 11, 12],
              [6, 9, float('inf'), 13, 14],
              [7, 10, 12, float('inf'), 15],
              [8, 11, 13, 15, float('inf')]]
"""
way.append(startCity)

for i in range(1, cityNumbers, 1):
    lastCityPaths = []
    for j in range(0, cityNumbers, 1):
        lastCityPaths.append(pathMatrix[way[i - 1]][j])
    way.append(lastCityPaths.index(min(lastCityPaths)))
    for j in range(0, i, 1):
        pathMatrix[way[i]][way[j]] = float('inf')

print(way)
sum = 0
for i in range(1, cityNumbers, 1):
    sum += pathMatrix[way[i - 1]][way[i]]
sum += pathMatrix[0][way[cityNumbers - 1]]
print(sum)
"""
X1 = [X[way[i]] for i in range(0, cityNumbers, 1)]
Y1 = [Y[way[i]] for i in range(0, cityNumbers, 1)]
plt.plot(X1, Y1, color='r', linestyle='', marker='o')
plt.plot(X1, Y1, color='b', linewidth=1)
X2 = [X[way[cityNumbers - 1]], X[way[0]]]
Y2 = [Y[way[cityNumbers - 1]], Y[way[0]]]
plt.plot(X2, Y2, color='g', linewidth=2, linestyle='-')
plt.grid(True)
plt.show()

# plt.title('Общий путь-%s.Номер города-%i.Всего городов -%i.\n Координаты X,Y случайные числа от %i до %i' % (
#    round(sum, 3), startCity, cityNumbers, 0, maxOfCoordinates), size=14)
"""

"Changes for fork"