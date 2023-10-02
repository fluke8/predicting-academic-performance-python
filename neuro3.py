from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


dataset = pd.read_csv('uspevaemost_nakop_bez_perevedennih_raw1.csv')
data = dataset.iloc[:, :-1]
target = dataset.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.1)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

lr = LogisticRegression(C=1000000.0, max_iter=1000000000)
lr.fit(X_train_std , y_train)
y_pred = lr.predict(X_test_std)

print("Число ошибочно классифицированных образцов логик регрессион: % d" % (y_test != y_pred).sum())
print(accuracy_score(y_test, y_pred))

myUspevaemost = pd.read_csv('uspevaemost_nakop_My.csv')

myUspevaemost = sc.transform(myUspevaemost)
print()
print('Логик регрессион')
print('Вероятность моего отчисления за первый семестр:',lr.predict_proba(myUspevaemost[:1,:])[:, 1] * 100)
print('Вероятность моего отчисления за второй семестр:',lr.predict_proba(myUspevaemost[1:2,:])[:, 1] * 100)
print('Вероятность моего отчисления за третий семестр:',lr.predict_proba(myUspevaemost[2:3,:])[:, 1] * 100)
print('Вероятность моего отчисления за четвертый семестр:',lr.predict_proba(myUspevaemost[3:4,:])[:, 1] * 100)
data_std = sc.transform(data)
y_prob = lr.predict_proba(data_std)[:, 1]

# Посчитайте средние вероятности для каждого семестра
semesters = range(1, len(X_test_std) + 1)
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





