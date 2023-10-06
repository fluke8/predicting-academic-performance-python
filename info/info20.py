import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('uspevaemost_nakop_bez_uchash.csv')
print(df.shape)
# Фильтрация строк
filtered_df = df[~((df['Квалификация'] == 0)  # Бакалавриат
                  & (df['отчислен'] == 0)  # Отчислен = 0
                  & (df.groupby('Студент')['Семестр'].transform('count') < 8))]  # Меньше 4 семестров

filtered_df = df[~((df['Квалификация'] == 1)  # Специалист
                  & (df['отчислен'] == 0)  # Отчислен = 0
                  & (df.groupby('Студент')['Семестр'].transform('count') < 10))]  # Меньше 10 семестров

filtered_df = df[~((df['Квалификация'] == 2)  # Магистрант
                  & (df['отчислен'] == 0)  # Отчислен = 0
                  & (df.groupby('Студент')['Семестр'].transform('count') < 3))]  # Меньше 3 семестров

# Вывод отфильтрованных данных
print(filtered_df)

filtered_df.to_csv('uspevaemost_nakop_bez_perevedennih.csv', index=False)