from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd

dataset = pd.read_csv('uspevaemost_nakop_raw1.csv')
data = dataset.iloc[:, :-1]
target = dataset.iloc[:, -1]

# Разделите данные на обучающий, валидационный и тестовый наборы
X_train, X_temp, y_train, y_temp = train_test_split(data, target, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Создайте сетку значений C для перебора
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 100000, 1000000, 100000000]}

# Создайте модель логистической регрессии
logreg = LogisticRegression(max_iter=1000000000)

# Используйте GridSearchCV для поиска оптимального C
grid_search = GridSearchCV(logreg, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Получите лучший параметр C
best_C = grid_search.best_params_['C']

# Оцените производительность модели с лучшим C на валидационном наборе
best_model = LogisticRegression(C=best_C)
best_model.fit(X_train, y_train)
validation_accuracy = best_model.score(X_val, y_val)

# Оцените модель на тестовом наборе данных
test_accuracy = best_model.score(X_test, y_test)

print(f'Лучший C: {best_C}')
print(f'Точность на валидации: {validation_accuracy}')
print(f'Точность на тесте: {test_accuracy}')
