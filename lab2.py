import numpy as np
import matplotlib.pyplot as plt

# Настройка области и сетки
x = np.linspace(0, 6, 500)
x1, x2 = np.meshgrid(x, x)
base_cond = (x1 >= 0) & (x2 >= 0) # Условие неотрицательности

# cbcntvs ythfdtycnd
systems = [
    (lambda x1, x2: (x1 + x2 <= 5) & (3*x1 - x2 <= 3), "Система (а)"),
    (lambda x1, x2: (x1 + x2 <= 4) & (6*x1 + 2*x2 >= 6) & (x1 + 5*x2 >= 5), "Система (б)")
]

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

for ax, (func, title) in zip(axs, systems):
    
    region = func(x1, x2) & base_cond
    
    # Заливка области решения
    ax.imshow(region.astype(int), extent=(0, 6, 0, 6), origin="lower", cmap="Greys", alpha=0.4)
    
    # Автоматическая отрисовка границ области
    ax.contour(x1, x2, region, levels=[0.5], colors='red', linewidths=2)
    
    ax.set_title(title)
    ax.grid(True, linestyle='--')
    ax.set_xlabel('$x_1$'); ax.set_ylabel('$x_2$')

plt.tight_layout()
plt.show()