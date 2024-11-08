"""
В матрице размером 7 х 5 переставить строки таким образом, чтобы минимальные
элементы строк следовали в порядке убывания.
"""

import numpy as np

a = np.random.randint(0, 100, size=(7, 5))
print("Исходная матрица >>")
print(a)

def row_min(i):
    return min(i)

b = sorted(a, key=row_min, reverse=True)
b = np.array(b)

print("\nОтсортированная матрица >>")
print(b)

