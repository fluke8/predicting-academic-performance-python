import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('uspevaemost_bez_anomalii_tvorcha.csv')

student_ids = df['Студент'].unique()
student_id_mapping = {student_id: student_num for student_num, student_id in enumerate(student_ids, start=1)}

df['Студент'] = df['Студент'].map(student_id_mapping)

# Преобразование оценок в числовой формат
df['Оценка'] = df['Оценка'].map({
    'отлично': 10,
    'хорошо': 7,
    'удовлетворительно': 4,
    'неудовлетворительно': 2,
    'зачтено': True,  # Можете указать другой балл за зачет
    'незачет': False  # Можете указать другой балл за незачет
})

# Группировка данных по студентам и семестрам и агрегация оценок
grouped = df.groupby(['Студент', 'Семестр'])['Оценка'].agg([
    ('Отлично', lambda x: (x == 10).mean()),
    ('Хорошо', lambda x: (x == 7).mean()),
    ('Удовлетворительно', lambda x: (x == 4).mean()),
    ('Неудовлетворительно', lambda x: (x == 2).mean()),
    ('Зачет', lambda x: (x == 7).mean()),  # Можете указать другой балл за зачет
    ('Незачет', lambda x: (x == 2).mean())  # Можете указать другой балл за незачет
]).reset_index()



# Замена идентификаторов студентов на числа

# Вывод результатов
grouped.to_csv('output_file_bez_anomalii_tvorcha1.csv', index=False)