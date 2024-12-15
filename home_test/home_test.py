# Импортируем необходимые библиотеки
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем датасет (укажите путь к файлу, если необходимо)
df = pd.read_csv('home_test/supermarket.csv')

# Приводим поля Date и Time к типу datetime
df['Date'] = pd.to_datetime(df['Date'])

# Для поля Time, если оно имеет формат "%H:%M", то преобразуем его так:
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')

# Проверяем наличие пропусков в датасете
has_missing_values = df.isnull().any().any()

# Выводим результат: True, если есть пропуски, False, если нет
print(has_missing_values)

# Группировка по типу товара и подсчет суммы количества
product_sales = df.groupby('Product line')['Quantity'].sum().reset_index()

# Поиск типа товара с максимальным количеством
top_product_type = product_sales.loc[product_sales['Quantity'].idxmax(), 'Product line']

# Вывод результата
print(f"Тип товара, который больше всего купили: {top_product_type.lower()}")

# Подсчет количества покупателей в каждой категории (Member и Normal)
customer_counts = df['Customer type'].value_counts(normalize=True)

# Нормализованная доля для каждой группы
member_percentage = customer_counts.get('Member', 0)  # Доля покупателей-членов программы
normal_percentage = customer_counts.get('Normal', 0)  # Доля обычных покупателей

# Округление результата до трех знаков после запятой
member_percentage = round(member_percentage, 3)
normal_percentage = round(normal_percentage, 3)

# Вывод результата
print(f"Доля покупателей-членов бонусной программы: {member_percentage}")
print(f"Доля обычных покупателей: {normal_percentage}")

# Группировка по платежному методу и вычисление среднего чека
average_check = df.groupby('Payment')['Total'].mean()

# Округление результата до двух знаков после запятой
average_check_rounded = average_check.round(2)

# Вывод результата
print(average_check_rounded)

# Добавление столбца с номером недели
df['Week'] = df['Date'].dt.isocalendar().week

# Группировка данных по неделе и платежному методу, вычисление среднего чека
weekly_avg_check = df.groupby(['Week', 'Payment'])['Total'].mean().reset_index()

# Фильтрация данных для 3-й недели
week_3 = weekly_avg_check[weekly_avg_check['Week'] == 3]

# Нахождение платежного метода с наименьшим средним чеком на 3-й неделе
min_payment_method = week_3.loc[week_3['Total'].idxmin(), 'Payment']

# Вывод результата
print(min_payment_method)