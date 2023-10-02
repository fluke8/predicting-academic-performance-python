import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense

# Загрузка данных
dataset = pd.read_csv('uspevaemost_nakop_bez_perevedennih_raw_stud_sumsem.csv')

dataset = dataset.sort_values(by=['отчислен'])

print(dataset.head)

data = dataset.iloc[:, :-1]
target = dataset.iloc[:, -1]

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.001)

# Масштабирование признаков
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Создание модели нейронной сети
model = Sequential()
model.add(Dense(1, input_dim=X_train_std.shape[1], activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучение модели
history = model.fit(X_train_std, y_train, epochs=20, batch_size=32, validation_data=(X_test_std, y_test))

# Оценка точности модели на тестовых данных
y_pred = (model.predict(X_test_std) > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))

# График изменения точности и функции потерь во время обучения
plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'], label='Точность на обучающем наборе')
plt.plot(history.history['val_accuracy'], label='Точность на валидационном наборе')
plt.plot(history.history['loss'], label='Функция потерь на обучающем наборе')
plt.plot(history.history['val_loss'], label='Функция потерь на валидационном наборе')
plt.xlabel('Эпохи')
plt.ylabel('Значения')
plt.legend()
plt.grid(True)
plt.show()

data_std = sc.transform(data)
y_prob = model.predict(data_std)

# Посчитайте средние вероятности для каждого семестра
semesters = range(1, len(data_std) + 1)
mean_probabilities = []

for semester in semesters:
    indices_for_semester = (data['Семестр'] == semester)
    mean_prob = np.mean(y_prob[indices_for_semester])
    mean_probabilities.append(mean_prob)

# Создайте диаграмму
plt.figure(figsize=(10, 6))
plt.plot(semesters, mean_probabilities, marker='o', linestyle='-')
plt.xlabel('Семестр')
plt.ylabel('Вероятность отчисления')
plt.title('Вероятность отчисления студентов по семестрам')
plt.grid(True)
plt.show()



