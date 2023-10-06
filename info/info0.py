import pandas as pd

df = pd.read_csv('csv/uspevaemost.csv', encoding='cp1251')
# Вывод результатов
df.to_csv('csv/uspevaemost2.csv', index=False)