import pandas as pd

df = pd.read_csv('uspevaemost.csv', encoding='cp1251')
# Вывод результатов
df.to_csv('uspevaemost2.csv', index=False)