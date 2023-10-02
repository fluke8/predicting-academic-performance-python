import pandas as pd
df = pd.read_csv('uspevaemost_studenta_bez_izm.csv')

df['Оценка'] = df['Оценка'].map({
    'отлично': 5,
    'хорошо': 4,
    'удовлетворительно': 3,
    'зачтено': 2, 
    'незачет': 1 
})

df.to_csv('uspevaemost_studenta_bez_izm_chisl.csv', index=False)

# max_indices = df.groupby(['Студент', 'Группа', 'Дисциплина', 'Семестр', 'Учебный год', 'Специальность', 'Форма обучения', 'Квалификация', 'Статус'])['Оценка'].idxmax(skipna=True)
# result_df = df.loc[max_indices]

# result_df.to_csv('uspevaemost_izm_max.csv', index=False)

# min_indices = df.groupby(['Студент', 'Группа', 'Дисциплина', 'Семестр', 'Учебный год', 'Специальность', 'Форма обучения', 'Квалификация', 'Статус'])['Оценка'].idxmin(skipna=True)
# result_df = df.loc[min_indices]

# result_df.to_csv('uspevaemost_izm_min.csv', index=False)


# import pandas as pd

# # Загрузка данных из CSV файла
# df = pd.read_csv('uspevaemost6.csv')

# # student_ids = df['Студент'].unique()
# # student_id_mapping = {student_id: student_num for student_num, student_id in enumerate(student_ids, start=1)}

# # df['Студент'] = df['Студент'].map(student_id_mapping)

# # Преобразование оценок в числовой формат
# df['Оценка'] = df['Оценка'].map({
#     'отлично': 5,
#     'хорошо': 4,
#     'удовлетворительно': 3,
#     'зачтено': 2,  # Можете указать другой балл за зачет
#     'незачет': 1  # Можете указать другой балл за незачет
# })

# # Группировка данных по студентам и семестрам и агрегация оценок
# max_indices = df.groupby(['Студент', 'Группа', 'Дисциплина', 'Семестр', 'Учебный год', 'Специальность', 'Форма обучения', 'Квалификация', 'Статус'])['Оценка'].idxmax()
# result_df = df.loc[max_indices]

# # Замена идентификаторов студентов на числа

# # Вывод результатов
# result_df.to_csv('uspevaemost7.csv', index=False)