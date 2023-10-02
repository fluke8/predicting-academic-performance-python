import pandas as pd

df = pd.read_csv('uspevaemost2.csv')

# Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
desired_id = 'неудовлетворительно'

# Фильтрация строк по ID студента
result = df[df['Оценка'] != desired_id]

# Вывод результатов
result.to_csv('uspv_bez_neud.csv', index=False)

# import pandas as pd

# df = pd.read_csv('uspevaemost_bez_anomalii_tvorcha.csv')

# # Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
# desired_id = 'Информатика 1.1'

# # Фильтрация строк по ID студента
# result = df[df['Дисциплина'] == desired_id]

# # Вывод результатов
# result.to_csv('tvorch_studenta2.csv')


# import pandas as pd

# df = pd.read_csv('uspevaemost.csv', encoding='cp1251')

# # Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
# desired_id = 'Творческий проект'

# # Фильтрация строк по ID студента
# result = df[~((df['Дисциплина'] == desired_id) & (df['Оценка'] != 'незачет'))]

# # Вывод результатов
# result.to_csv('tvorch_studenta1.csv')