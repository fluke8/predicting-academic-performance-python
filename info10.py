import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('uspevaemost3.csv')

df = df.iloc[:, :1]

df = df.drop_duplicates()

# Вывод результатов (замените 'output_file.csv' на имя файла, в который хотите сохранить результаты)
df.to_csv('studenti_bez_ispravleni.csv', index=False)