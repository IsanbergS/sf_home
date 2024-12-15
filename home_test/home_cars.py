import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from sklearn.preprocessing import LabelEncoder
# Загрузка данных
df = pd.read_csv('home_test\Electric Car.csv')


# Создание объекта LabelEncoder и выполнение кодирования для столбца BodyStyle
# Создание объекта LabelEncoder и выполнение кодирования для столбца BodyStyle
label_encoder = LabelEncoder()
df['BodyStyle_encoded'] = label_encoder.fit_transform(df['BodyStyle'])

# Найдем сумму кодированных значений
sum_encoded = df['BodyStyle_encoded'].sum()

# Найдем количество уникальных категорий в столбце BodyStyle_encoded
cat_count = df['BodyStyle_encoded'].nunique()

# Печатаем результат
print(sum_encoded + cat_count == 429)