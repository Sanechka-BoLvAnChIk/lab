import numpy as np
from scipy.optimize import linprog

# 1. Входные данные
a = [200, 350, 300]  # Поставки (A1, A2, A3)
b = [270, 130, 190, 150, 110]  # Потребности (B1...B5)
# Матрица тарифов (проверьте порядок строк: A1, A2, A3)
D = [
    [24, 50, 55, 27, 16],
    [50, 47, 23, 17, 21],
    [35, 59, 55, 27, 41]
]

# 2. Подготовк огр
# Услов: сумм строк = a, сумм столб = b
A_eq = []
for i in range(3): A_eq.append([1 if k//5 == i else 0 for k in range(15)])
for j in range(5): A_eq.append([1 if k%5 == j else 0 for k in range(15)])

# 3. формула
res = linprog(np.ravel(D), A_eq=A_eq, b_eq=a+b, bounds=(0, None), method='highs')

# 4. Вывод
if res.success:
    print(f"Минимальные затраты: {res.fun}")
    print("План перевозок:\n", res.x.reshape(3, 5))
else:
    print("Решение не найдено")