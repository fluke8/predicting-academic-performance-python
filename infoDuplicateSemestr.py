

import pandas as pd

df = pd.read_csv('uspevaemost_bez_anomalii_tvorcha.csv')

duplicate_semesters = df.groupby(['Студент', 'Семестр', 'Учебный год', 'Дисциплина']).size().reset_index(name='Повторяющиеся семестры')
students_with_duplicate_semesters = duplicate_semesters[duplicate_semesters['Повторяющиеся семестры'] > 1]


# Вывод результатов
students_with_duplicate_semesters.to_csv('duplicati_BA.csv')

