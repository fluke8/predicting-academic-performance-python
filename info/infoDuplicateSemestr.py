

import pandas as pd

df = pd.read_csv('uspevaemost4.csv')

duplicate_semesters = df.groupby(['Студент', 'Семестр', 'Учебный год', 'Дисциплина']).size().reset_index(name='Повторяющиеся семестры')
students_with_duplicate_semesters = duplicate_semesters[duplicate_semesters['Повторяющиеся семестры'] > 1]


# Вывод результатов
students_with_duplicate_semesters.to_csv('beee.csv', index=False)

