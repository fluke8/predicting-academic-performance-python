import pandas as pd

# Загрузите CSV-файл в DataFrame
df = pd.read_csv('beee.csv')

df = df.drop(df.columns[1], axis=1)
df = df.drop(df.columns[2], axis=1)
# Сохраните обновленный DataFrame обратно в CSV-файл
df.to_csv('beee1.csv', index=False)