import pandas as pd

# Загрузите CSV-файл в DataFrame
df = pd.read_csv('uspv_bez_neud.csv')
print(df.shape)
# Удалите дублирующиеся строки
df.drop_duplicates(inplace=True)
print(df.shape)
# Сохраните обновленный DataFrame обратно в CSV-файл
df.to_csv('uspevaemost_bez_D.csv', index=False)