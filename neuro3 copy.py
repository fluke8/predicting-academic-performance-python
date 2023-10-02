from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


dataset = pd.read_csv('uspevaemost_nakop_bez_perevedennih_raw1_stud.csv')
data = dataset.iloc[:, 1:-1]
target = dataset.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=0)

# feature_names = ['Семестр','Форма обучения','Квалификация', 'незачет сразу', 'зачет сразу', 'удовлетворительно сразу', 'хорошо сразу',
#          'отлично сразу', 'зачет с исправлением', 'удовлетворительно с исправлением',
#          'хорошо с исправлением', 'отлично с исправлением', 'незачет до исправления',
#          'зачет до исправления', 'удовлетворительно до исправления','Накоп незачет сразу','Накоп зачет сразу','Накоп удовлетворительно сразу',
#          'Накоп хорошо сразу','Накоп отлично сразу','Накоп зачет с исправлением','Накоп удовлетворительно с исправлением','Накоп хорошо с исправлением',
#          'Накоп отлично с исправлением','Накоп незачет до исправления','Накоп зачет до исправления','Накоп удовлетворительно до исправления']


sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

lr = LogisticRegression(C=1000000.0, max_iter=1000000000)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

print("Число ошибочно классифицированных образцов логик регрессион: % d" % (y_test != y_pred).sum())
print(accuracy_score(y_test, y_pred))

print()
print('Логик регрессион')
print('Вероятность моего отчисления за первый семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[:1,:])[:, 1] * 100)
print('Вероятность моего отчисления за второй семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[1:2,:])[:, 1] * 100)
print('Вероятность моего отчисления за третий семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[2:3,:])[:, 1] * 100)
print('Вероятность моего отчисления за четвертый семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[3:4,:])[:, 1] * 100)

graph_data = dataset.iloc[:, 1:-1]

predictions = np.empty((len(graph_data), 1), dtype="float32")


i = 0
for line in graph_data.values.tolist():
    probability = lr.predict_proba(np.array(line).reshape(1, -1))[:, 1] * 100
    predictions[i] = probability
    i+=1

graph_data_with_predictions = np.hstack((dataset.iloc[:, :-1], predictions))

graph_data_with_predictions = np.delete(graph_data_with_predictions, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], axis=1)

# graph_data_with_predictions = graph_data_with_predictions[500:100]


student_ids = np.unique(graph_data_with_predictions[:100, 0])

fig, ax = plt.subplots()

plt.figure(figsize=(10, 6))

for student_id in student_ids:
    student_data = graph_data_with_predictions[graph_data_with_predictions[:, 0] == student_id]
    semesters = student_data[:, 1].astype(int)
    probabilities = student_data[:, 2].astype(float)
    plt.plot(semesters, probabilities, label=f'Student {student_id}')

plt.xlabel('Семестр')
plt.ylabel('Вероятность отчисления')
plt.title('Вероятность отчисления по семестрам для разных студентов')

plt.grid(True)
plt.show()
