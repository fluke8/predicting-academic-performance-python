from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression


dataset = pd.read_csv('uspevaemost_nakop_bez_perevedennih_raw.csv')
data = dataset.iloc[:, :-1]
target = dataset.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

lr = LogisticRegression(C=1000000.0, max_iter=1000000000)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)



print("Число ошибочно классифицированных образцов логик регрессион: % d" % (y_test != y_pred).sum())
print(accuracy_score(y_test, y_pred))

ppn = Perceptron(eta0=0.0000001, max_iter=10000000)
ppn.fit(X_train, y_train)
y_pred = ppn.predict(X_test_std)

print("Число ошибочно классифицированных образцов персептрон: % d" % (y_test != y_pred).sum())
print(accuracy_score(y_test, y_pred))


mlp = MLPClassifier(hidden_layer_sizes=(10), activation='relu', solver='adam', max_iter=1000000, learning_rate_init=0.00001)
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)
print("Число ошибочно классифицированных образцов млп: % d" % (y_test != y_pred).sum())
print(accuracy_score(y_test, y_pred))
print()
print('Логик регрессион')
print('Вероятность моего отчисления за первый семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[:1,:])[:, 1] * 100)
print('Вероятность моего отчисления за второй семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[1:2,:])[:, 1] * 100)
print('Вероятность моего отчисления за третий семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[2:3,:])[:, 1] * 100)
print('Вероятность моего отчисления за четвертый семестр:',lr.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[3:4,:])[:, 1] * 100)
print()
print('Млп')
print('Вероятность моего отчисления за первый семестр:',mlp.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[:1,:])[:, 1] * 100)
print('Вероятность моего отчисления за второй семестр:',mlp.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[1:2,:])[:, 1] * 100)
print('Вероятность моего отчисления за третий семестр:',mlp.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[2:3,:])[:, 1] * 100)
print('Вероятность моего отчисления за четвертый семестр:',mlp.predict_proba(pd.read_csv('uspevaemost_nakop_My.csv').iloc[3:4,:])[:, 1] * 100)