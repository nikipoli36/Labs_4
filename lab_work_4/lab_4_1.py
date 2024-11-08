"""
Поменять местами максимальный и 1-й элементы строк матри цы А размером 5 х 7.
"""

import numpy as np

a = np.random.randint(1, 100, size=(5, 7))
print("Исходная матрица A >>")
print(a)
for i in a:
    max_index = np.argmax(i)
    i[0], i[max_index] = i[max_index], i[0]

print("\nМатрица A после замены >>")
print(a)