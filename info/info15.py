import pandas as pd

df = pd.read_csv('uspevaemost_nakop.csv')

# Преобразование значений "незачет сразу" в числа (1 и 0)
df['незачет сразу'] = df['незачет сразу'].apply(lambda x: 1 if x >= 1 else 0)

# Группировка по студенту и проверка на наличие "незачет сразу" в любой из строк
df['отчислен'] = df.groupby('Студент')['незачет сразу'].transform('max')

print(df)
df.to_csv('uspevaemost_nakop_target.csv', index=False)