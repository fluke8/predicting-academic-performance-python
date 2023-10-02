import pandas as pd

df = pd.read_csv('uspevaemost2.csv')

# Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
desired_id = '42477A384446554E566E55587779514855326A5674413D3D'

# Фильтрация строк по ID студента
result = df[df['Студент'] == desired_id]
# Вывод результатов
result.to_csv('uspevaemost_studenta.csv', index=False)

# import pandas as pd

# df = pd.read_csv('uspevaemost2.csv')

# # Замените 'desired_id' на идентификатор (ID) студента, который вас интересует
# desired_id = 'Учащийся'

# # Фильтрация строк по ID студента
# result = df[df['Статус'] == desired_id]
# # Вывод результатов
# result.to_csv('beee.csv', index=False)