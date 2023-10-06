import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('uspevaemost_nakop_bez_perevedennih_raw_stud.csv')
print(df.shape)

df = df.groupby(['Студент', 'Семестр']).sum()

# Вывод отфильтрованных данных
print(df)

df.to_csv('uspevaemost_nakop_bez_perevedennih_raw_stud_sumsem.csv', index=False)