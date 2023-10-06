import pandas as pd

# Загрузка данных из трех датасетов (пример)
df1 = pd.read_csv('uspevaemost_bez_izm_kolvo.csv')
df2 = pd.read_csv('uspevaemost_izm_max_kolvo.csv')
df3 = pd.read_csv('uspevaemost_izm_min_kolvo.csv')


# Объединяем датасеты по общим столбцам
merged_df = pd.merge(df1, df2, on=['Студент','Группа','Семестр','Учебный год','Специальность','Форма обучения','Квалификация','Статус'], how='outer')
merged_df = pd.merge(merged_df, df3, on=['Студент','Группа','Семестр','Учебный год','Специальность','Форма обучения','Квалификация','Статус'], how='outer')

# Сохраняем объединенный датасет
merged_df.to_csv('uspevaemost_kolvo_all.csv', index=False)