import numpy as np
import matplotlib.pyplot as plt

# Генерация данных для примера
np.random.seed(42)
num_points = 100  # Количество точек звуков

# Координаты (x, y) звуков
x_coords = np.random.uniform(0, 100, num_points)
y_coords = np.random.uniform(0, 100, num_points)

# Интенсивность звуков в условных единицах
intensities = np.random.uniform(0, 1, num_points)

# Создание сетки для интерполяции данных
grid_x, grid_y = np.mgrid[0:100:200j, 0:100:200j]

# Интерполяция данных для создания карты
from scipy.interpolate import griddata

grid_intensities = griddata((x_coords, y_coords), intensities, (grid_x, grid_y), method='cubic')

# Визуализация температурной карты
plt.figure(figsize=(10, 8))
plt.title("Тепловая карта распределения звуков", fontsize=16)
plt.xlabel("X координата", fontsize=12)
plt.ylabel("Y координата", fontsize=12)

# Отображение тепловой карты
heatmap = plt.imshow(grid_intensities.T, extent=(0, 100, 0, 100), origin='lower', cmap='viridis', alpha=0.8)

# Добавление точек звуков
plt.scatter(x_coords, y_coords, c=intensities, cmap='viridis', edgecolor='white', s=100)

# Добавление цветовой шкалы
cbar = plt.colorbar(heatmap)
cbar.set_label("Интенсивность звука", fontsize=12)

# Отображение графика
plt.grid(False)
plt.show()
