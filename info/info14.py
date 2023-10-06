
import pandas as pd

# Загрузка данных из трех датасетов (пример)
df = pd.read_csv('uspevaemost_kolvo_all.csv')


df.fillna(0, inplace=True)

# Сохраняем объединенный датасет
df.to_csv('uspevaemost_kolvo_all_zero.csv', index=False)

