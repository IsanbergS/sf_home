import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# 1. Загрузка данных и выбор нужных столбцов
data = pd.read_csv('home_machine_learning/Electric_Car.csv')
columns_to_keep = ["AccelSec", "TopSpeed_KmH", "Range_Km", "PriceEuro"]
data = data[columns_to_keep]
# 2. Оптимальное количество кластеров (определите по графику локтя, например, 4)
optimal_clusters = 4

# 3. Реализация K-means
kmeans = KMeans(n_clusters=optimal_clusters, random_state=0)
kmeans.fit(data)

# 4. Координаты центров кластеров
centers = kmeans.cluster_centers_

# 5. Вычисление нормы
norm = np.linalg.norm(centers)

# Округление нормы до трёх знаков
result = round(norm, 3)

# Вывод результата
print(result)
