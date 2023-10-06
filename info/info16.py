import pandas as pd
df = pd.read_csv('uspevaemost_nakop_target.csv')


df = df[df['Квалификация'] != 'Слушатель программ довузовской подготовки']

df['Квалификация'] = df['Квалификация'].map({
    'Аспирант': 3,
    'Магистр': 2,
    'Специалист': 1,
    'Бакалавр': 0,
})

df['Форма обучения'] = df['Форма обучения'].map({
    'Заочная': 2,
    'Очная': 0,
   'Очно-заочная': 1
})

df.to_csv('uspevaemost_nakop_chisla.csv', index=False)