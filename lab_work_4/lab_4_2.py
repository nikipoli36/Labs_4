"""
Дана матрица А размером 7 х 5 и массив В размером 5. Заменить максимальный элемент столбца соответствующим элементом массива В,
если этот элемент больше найденного максимального эле мента столбца. В противном случае замены не производить.
"""

import numpy as np

a = np.random.randint(1, 70, size=(7, 5))
b = np.random.randint(1, 100, size=5)
print("Исходная матрица A >>")
print(a)
print("\nИсходный массив В >>")
print(b)

for i in range(len(a[0])):
    max = a[0][i]
    for j in range(len(a)):
        if a[j][i] > max:
            max = a[j][i]
    for j in range(len(a)):
        if a[j][i] == max and max < b[i]:
            a[j][i] = b[i]

print("\nИзмененная матрица А >>")
print(a)
