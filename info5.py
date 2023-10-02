import pandas as pd

# Загрузите CSV файл
df = pd.read_csv('tvorch_studenta2.csv')

# Преобразуйте столбец с датой (предположим, что он называется 'год') в формат datetime, если он еще не в таком формате

# Отсортируйте DataFrame по столбцу 'год'
df_sorted = df.sort_values(by='Учебный год')

# Сохраните отсортированный DataFrame в новый CSV файл
df_sorted.to_csv('tvorch_studenta_po_godam.csv', index=False)

print("CSV файл успешно отсортирован по годам.")