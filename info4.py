# import pandas as pd

# df = pd.read_csv('uspevaemost.csv', encoding='cp1251')

# # Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
# desired_id = '2B2F594F58715179766342613567424C58306B4776513D3D'

# # Фильтрация строк по ID студента
# result = df[df['Студент'] == desired_id]

# # Вывод результатов
# result.to_csv('uspevaemost_1_studenta.csv')

import pandas as pd

df = pd.read_csv('tvorch_studenta1.csv')

# Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
desired_id = 'Творческий проект'

# Фильтрация строк по ID студента
result = df[df['Дисциплина'] == desired_id]

# Вывод результатов
result.to_csv('tvorch_studenta2.csv')


# import pandas as pd

# df = pd.read_csv('uspevaemost.csv', encoding='cp1251')

# # Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
# desired_id = 'Творческий проект'

# # Фильтрация строк по ID студента
# result = df[~((df['Дисциплина'] == desired_id) & (df['Оценка'] != 'незачет'))]

# # Вывод результатов
# result.to_csv('tvorch_studenta1.csv')