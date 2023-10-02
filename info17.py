import pandas as pd

df = pd.read_csv('uspevaemost_nakop_chisla.csv')

# Удаление записей, где статус равен "учащийся"
df = df[df['Статус'] != 'Учащийся']


# Сохранение результата в новый CSV файл
df.to_csv('uspevaemost_nakop_bez_uchash.csv', index=False)