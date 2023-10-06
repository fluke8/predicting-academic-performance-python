import pandas as pd

df = pd.read_csv('uspevaemost_nakop_bez_perevedennih_raw_cleaned.csv')
print(df.shape)
# Удаление записей, где статус равен "учащийся"
df = df[df['незачет сразу'] != 1]
df = df[df['Накоп незачет сразу'] != 1]

print(df.shape)

# Сохранение результата в новый CSV файл
df.to_csv('uspevaemost_nakop_bez_perevedennih_raw1_cleaned.csv', index=False)