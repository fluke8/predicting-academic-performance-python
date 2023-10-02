import pandas as pd

df = pd.read_csv('uspevaemost_bez_izm_chisl.csv')

# Группировка по студенту и подсчет оценок каждой категории
result = df.groupby(['Студент', 'Группа', 'Семестр', 'Учебный год', 'Специальность', 'Форма обучения', 'Квалификация', 'Статус'])['Оценка'].value_counts().unstack(fill_value=0)

result.to_csv('uspevaemost_bez_izm_kolvo.csv', index=True)

# import pandas as pd

# df = pd.read_csv('uspevaemost_izm_max.csv')

# # Группировка по студенту и подсчет оценок каждой категории
# result = df.groupby(['Студент', 'Группа', 'Семестр', 'Учебный год', 'Специальность', 'Форма обучения', 'Квалификация', 'Статус'])['Оценка'].value_counts().unstack(fill_value=0)

# result.to_csv('uspevaemost_izm_max_kolvo.csv', index=True)

# import pandas as pd

# df = pd.read_csv('uspevaemost_izm_min.csv')

# # Группировка по студенту и подсчет оценок каждой категории
# result = df.groupby(['Студент', 'Группа', 'Семестр', 'Учебный год', 'Специальность', 'Форма обучения', 'Квалификация', 'Статус'])['Оценка'].value_counts().unstack(fill_value=0)

# result.to_csv('uspevaemost_izm_min_kolvo.csv', index=True)