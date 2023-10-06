# import pandas as pd

# # Загрузите данные из CSV файла
# df1 = pd.read_csv('.csv')
# df = pd.read_csv('.csv')


# filtered_df = df[~df.isin(df1)].dropna()

# print(filtered_df.shape)

# filtered_df.drop_duplicates(inplace=True)

# print(filtered_df.shape)
# # Вывод результатов (замените 'output_file.csv' на имя файла, в который хотите сохранить результаты)
# filtered_df.to_csv('uspevaemost5.csv', index=False)

import pandas as pd

# Загрузите данные из CSV файла
df2 = pd.read_csv('uspevaemost_studenta_bez_izm.csv')
df1 = pd.read_csv('uspevaemost_studenta3.csv')
print(df1.shape)
print(df2.shape)
merged_df = df1.merge(df2, indicator=True, how='outer').loc[lambda x: x['_merge'] == 'left_only']
print(merged_df.shape)
# Удалите столбец _merge, который был создан для пометки объединенных строк
merged_df = merged_df.drop(columns=['_merge']).drop_duplicates()

# Теперь merged_df содержит только строки, которых нет в df2
print(merged_df.shape)
# Вывод результатов (замените 'output_file.csv' на имя файла, в который хотите сохранить результаты)
merged_df.to_csv('uspevaemost_studenta_s_izm.csv', index=False)