import pandas as pd

df = pd.read_csv('uspevaemost_nakop_bez_perevedennih.csv')

df = df.drop(df[df.duplicated(subset=['Студент', 'Семестр'], keep=False)].index)

df.drop('Статус', axis=1, inplace=True)
df.drop('Студент', axis=1, inplace=True)
df.drop('Группа', axis=1, inplace=True)
df.drop('Специальность', axis=1, inplace=True)
df.drop('Учебный год', axis=1, inplace=True)

df.to_csv('uspevaemost_nakop_bez_perevedennih_raw_cleaned.csv', index=False)