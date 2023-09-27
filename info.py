import pandas as pd

df = pd.read_csv('uspevaemost.csv', encoding='cp1251')

# Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
desired_id = '2B2F397249583175764B6A74722B373239642F7053413D3D'

# Фильтрация строк по ID студента
result = df[df['Студент'] == desired_id]

# Вывод результатов
result.to_csv('uspevaemost_1_studenta.csv')