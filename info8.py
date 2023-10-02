import pandas as pd

# Загрузите данные из CSV файла
df = pd.read_csv('uspevaemost_studenta.csv')

df.drop_duplicates(inplace=True)

df = df[~(df['Оценка'] == 'неудовлетворительно') | ~(df.duplicated(subset=df.columns.difference(['Оценка']))) ]

df.to_csv('uspevaemost_studenta3.csv', index=False)

print(df.shape)
df = df.drop_duplicates(subset=df.columns.difference(['Оценка']), keep=False)

print(df.shape)

df.to_csv('uspevaemost_studenta_bez_izm.csv', index=False)


# import pandas as pd

# # Загрузите данные из CSV файла
# df = pd.read_csv('stud.csv')

# df.drop_duplicates(inplace=True)

# df = df[~(df['Оценка'] == 'неудовлетворительно') | ~(df.duplicated(subset=df.columns.difference(['Оценка']))) ]

# df.to_csv('stud1.csv', index=False)

# print(df.shape)
# df = df.drop_duplicates(subset=df.columns.difference(['Оценка']), keep=False)



# print(df.shape)

# df.to_csv('stud2.csv', index=False)

