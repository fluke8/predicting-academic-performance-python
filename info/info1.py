import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('uspevaemost.csv', encoding='cp1251')


# Сортировка данных по студентам
sorted_data = df.sort_values(by='Студент')

# Вывод результатов (замените 'output_file.csv' на имя файла, в который хотите сохранить результаты)
sorted_data.to_csv('output_file.csv', index=False)